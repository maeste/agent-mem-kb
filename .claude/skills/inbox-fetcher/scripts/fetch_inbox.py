#!/usr/bin/env python3
"""
fetch_inbox.py — Process inbox.md and populate raw/web/ (and raw/papers/ for PDFs).

Usage:
    python fetch_inbox.py                    # uses current dir as vault
    python fetch_inbox.py --vault /path      # explicit vault path
    python fetch_inbox.py --dry-run          # shows what would be done

Reads `inbox.md` from the vault root, finds unchecked URL entries,
fetches each, and writes clean markdown + images to raw/web/<slug>/.
PDFs go to raw/papers/<slug>.pdf.

Idempotent: already-processed URLs are skipped.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, urljoin

# --- Dependency check with friendly error -----------------------------------

MISSING_DEPS = []
try:
    import requests
except ImportError:
    MISSING_DEPS.append("requests")
try:
    import trafilatura
except ImportError:
    MISSING_DEPS.append("trafilatura")
try:
    from slugify import slugify
except ImportError:
    MISSING_DEPS.append("python-slugify")

if MISSING_DEPS:
    print("Missing dependencies. Install with:", file=sys.stderr)
    print(f"  pip install {' '.join(MISSING_DEPS)}", file=sys.stderr)
    sys.exit(1)


# --- Data types -------------------------------------------------------------

@dataclass
class InboxEntry:
    url: str
    line_index: int
    raw_line: str


@dataclass
class FetchResult:
    url: str
    ok: bool
    kind: str  # "html" | "pdf" | "failed"
    out_path: Path | None = None
    reason: str | None = None


# --- Constants --------------------------------------------------------------

HTML_TIMEOUT = 20
PDF_TIMEOUT = 60
MAX_PDF_SIZE_MB = 50

USER_AGENT = (
    "Mozilla/5.0 (compatible; InboxFetcher/1.0; "
    "+https://github.com/anthropic/skills)"
)

UNCHECKED_PATTERN = re.compile(r"^- \[ \] (https?://\S+)")
IMG_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

# YouTube domains
YOUTUBE_DOMAINS = frozenset({
    "youtube.com",
    "www.youtube.com",
    "youtu.be",
    "m.youtube.com",
})

# Path to the youtube-content skill's transcript fetcher
YOUTUBE_TRANSCRIPT_SCRIPT = Path.home() / ".hermes" / "skills" / "media" / "youtube-content" / "scripts" / "fetch_transcript.py"

# Domains known to block plain HTTP fetchers (auth walls, aggressive
# anti-bot, or JS-only rendering). X/Twitter is handled by OpenCLI
# (fetch_x_thread) instead of being walled. Others are skipped upfront
# and marked for agent-driven Playwright MCP fallback.
OPENCLI_DOMAINS = frozenset({
    "x.com",
    "twitter.com",
    "mobile.twitter.com",
})

WALLED_DOMAINS = frozenset({
    "threads.net",
    "linkedin.com",
    "www.linkedin.com",
    "facebook.com",
    "www.facebook.com",
    "m.facebook.com",
    "instagram.com",
    "www.instagram.com",
})

PLAYWRIGHT_HINT = "try playwright"


# --- Core operations --------------------------------------------------------

def find_unchecked_entries(inbox_text: str) -> list[InboxEntry]:
    """Parse inbox.md and return list of unchecked URL entries.
    
    Only processes URLs under a '## To process' section.
    HTML comments (<!-- ... -->) are stripped before parsing so example
    URLs inside comments are not picked up.
    """
    # Strip HTML comments (including multi-line) before parsing
    stripped = re.sub(r"<!--.*?-->", "", inbox_text, flags=re.DOTALL)
    # After stripping, some lines may have trailing whitespace from comment removal
    entries = []
    in_to_process = False
    for i, line in enumerate(stripped.splitlines()):
        # Track sections
        section_match = re.match(r"^##\s+(.+)$", line)
        if section_match:
            section_name = section_match.group(1).strip().lower()
            in_to_process = section_name in ("to process",)
            continue
        # Only match URLs in the "To process" section
        if not in_to_process:
            continue
        match = UNCHECKED_PATTERN.match(line)
        if match:
            entries.append(InboxEntry(
                url=match.group(1).strip(),
                line_index=i,
                raw_line=line,
            ))
    return entries


def is_pdf_url(url: str) -> bool:
    """Heuristic: URL path ends in .pdf."""
    return Path(urlparse(url).path).suffix.lower() == ".pdf"


def is_youtube_url(url: str) -> bool:
    """Check if URL is a YouTube video."""
    host = urlparse(url).netloc.lower()
    return host in YOUTUBE_DOMAINS


def fetch_youtube(url: str, web_dir: Path) -> FetchResult:
    """Fetch YouTube transcript and save as markdown."""
    import json
    import subprocess

    if not YOUTUBE_TRANSCRIPT_SCRIPT.exists():
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"youtube-content skill not found at {YOUTUBE_TRANSCRIPT_SCRIPT}")

    try:
        result = subprocess.run(
            ["python3", str(YOUTUBE_TRANSCRIPT_SCRIPT), url, "--text-only"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            err = result.stderr.strip() or result.stdout.strip()
            return FetchResult(url=url, ok=False, kind="failed",
                               reason=f"transcript fetch failed: {err}")
    except subprocess.TimeoutExpired:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason="transcript fetch timed out")
    except Exception as e:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"transcript fetch error: {e}")

    # Parse JSON output
    data: dict | None = None
    try:
        parsed = json.loads(result.stdout)
        if isinstance(parsed, dict):
            data = parsed
            if data.get("error"):
                return FetchResult(url=url, ok=False, kind="failed",
                                   reason=data["error"])
            full_text = data.get("full_text", "").strip()
            if not full_text:
                return FetchResult(url=url, ok=False, kind="failed",
                                   reason="transcript empty (likely disabled)")
        else:
            full_text = str(parsed).strip()
    except json.JSONDecodeError:
        # Script might output plain text
        full_text = result.stdout.strip()

    if not full_text:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason="transcript output empty")

    # Extract metadata if we have JSON
    title = data.get("title", "") if data else ""
    video_id = data.get("video_id", "") if data else ""

    slug = slug_from(url, title or f"youtube-{video_id}")
    out_dir = web_dir / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    frontmatter_lines = [
        "---",
        f"source_url: {url}",
        f"title: {yaml_escape(title) if title else 'YouTube Video'}",
        f"video_id: {video_id}" if video_id else "",
        f"fetched: {date.today().isoformat()}",
        "---",
    ]
    frontmatter = "\n".join(filter(None, frontmatter_lines)) + "\n\n"

    body = f"# {title or 'YouTube Video'}\n\n{full_text}\n"
    (out_dir / "index.md").write_text(frontmatter + body, encoding="utf-8")

    return FetchResult(url=url, ok=True, kind="youtube", out_path=out_dir)


def is_walled(url: str) -> bool:
    """Preflight check: URL host is in the walled-domain list."""
    host = urlparse(url).netloc.lower()
    return host in WALLED_DOMAINS


def is_opencli(url: str) -> bool:
    """Check: URL host is an OpenCLI-backed domain (X/Twitter)."""
    host = urlparse(url).netloc.lower()
    return host in OPENCLI_DOMAINS


def extract_tweet_id(url: str) -> str | None:
    """Extract the tweet ID from an X/Twitter URL."""
    # Matches: x.com/user/status/123, twitter.com/user/status/123,
    # x.com/i/status/123
    m = re.search(r"/status/(\d+)", url)
    if m:
        return m.group(1)
    # Bare ID: x.com/i/123
    m = re.match(r"https?://(?:x|twitter)\.com/i/(\d+)", url)
    if m:
        return m.group(1)
    return None


def fetch_x_thread(url: str, web_dir: Path) -> FetchResult:
    """Fetch an X/Twitter thread via OpenCLI and save as markdown."""
    import json
    import subprocess

    tweet_id = extract_tweet_id(url)
    if not tweet_id:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason="could not extract tweet ID from URL")

    try:
        result = subprocess.run(
            ["opencli", "twitter", "thread", url],
            capture_output=True, text=True, timeout=30,
        )
    except subprocess.TimeoutExpired:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason="opencli timeout (30s)")
    except FileNotFoundError:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason="opencli not found in PATH")
    except Exception as e:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"opencli error: {e}")

    if result.returncode != 0 or not result.stdout.strip():
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"opencli returned empty or error: {result.stderr[:200]}")

    # OpenCLI returns YAML. Parse it.
    raw = result.stdout.strip()

    # Try YAML parse for structured data, fallback to raw text
    try:
        import yaml
        docs = list(yaml.safe_load_all(raw))
        # OpenCLI returns a single YAML doc that is a list of tweet objects
        if docs and isinstance(docs[0], list):
            tweet_list = docs[0]
        else:
            tweet_list = docs

        if tweet_list and isinstance(tweet_list[0], dict):
            author = tweet_list[0].get("author", "unknown")
            text = tweet_list[0].get("text", "")
            created_at = tweet_list[0].get("created_at", "")
            likes = tweet_list[0].get("likes", 0)
            retweets = tweet_list[0].get("retweets", 0)

            # Build full thread markdown
            md_parts = [text]
            for reply in tweet_list[1:]:
                if isinstance(reply, dict):
                    r_author = reply.get("author", "unknown")
                    r_text = reply.get("text", "")
                    md_parts.append(f"\n\n---\n\n**@{r_author}** (reply):\n\n{r_text}")
        else:
            raise ValueError("unexpected YAML structure")
    except Exception:
        # Fallback: use raw output
        author = "unknown"
        created_at = ""
        likes = 0
        retweets = 0
        md_parts = [raw]

    body = "\n".join(md_parts)
    slug = f"{author}-{tweet_id}"

    out_dir = web_dir / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    frontmatter_lines = [
        "---",
        f"source_url: {url}",
        f"title: @{author} — X thread {tweet_id}",
        f"author: {author}",
    ]
    if created_at:
        frontmatter_lines.append(f"published: {created_at}")
    frontmatter_lines.append(f"likes: {likes}")
    frontmatter_lines.append(f"retweets: {retweets}")
    frontmatter_lines.append(f"fetched: {date.today().isoformat()}")
    frontmatter_lines.append("fetched_via: opencli")
    frontmatter_lines.append("---")
    frontmatter = "\n".join(frontmatter_lines) + "\n\n"

    md_content = f"# @{author} — X thread ({tweet_id})\n\n{body}\n"
    (out_dir / "index.md").write_text(frontmatter + md_content, encoding="utf-8")

    return FetchResult(url=url, ok=True, kind="html", out_path=out_dir)


def rewrite_url_for_fetch(url: str) -> tuple[str, str | None]:
    """Rewrite a user-supplied URL into a better fetch target.

    Returns (fetch_url, slug_override). When slug_override is non-None
    it is used as the raw-file slug verbatim (bypassing slugify) so
    canonical identifiers like arxiv paper IDs survive intact.

    Arxiv abstract and HTML URLs are rewritten to the PDF endpoint so
    we archive the paper itself instead of the landing page.
    """
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    if host in ("arxiv.org", "export.arxiv.org"):
        m = re.match(r"^/(?:abs|html|pdf)/(.+?)(?:\.pdf)?$", parsed.path)
        if m:
            paper_id = m.group(1)
            slug = f"arxiv-{paper_id.replace('/', '-')}"
            return f"https://arxiv.org/pdf/{paper_id}.pdf", slug
    return url, None


def slug_from(url: str, title: str | None) -> str:
    """Generate a filesystem-safe slug, preferring the title."""
    if title and title.strip():
        s = slugify(title)[:80]
        if s:
            return s
    host = urlparse(url).netloc.replace("www.", "")
    h = hashlib.sha1(url.encode()).hexdigest()[:8]
    return f"{slugify(host)}-{h}"


def fetch_pdf(url: str, papers_dir: Path,
              slug_override: str | None = None) -> FetchResult:
    """Download a PDF directly to raw/papers/."""
    try:
        r = requests.get(
            url,
            timeout=PDF_TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            stream=True,
        )
        r.raise_for_status()
    except Exception as e:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"pdf download failed: {e}")

    size = int(r.headers.get("Content-Length", 0))
    if size > MAX_PDF_SIZE_MB * 1024 * 1024:
        print(f"  ⚠ large PDF ({size // 1024 // 1024} MB): {url}")

    slug = slug_override or slug_from(url, None)
    out_path = papers_dir / f"{slug}.pdf"
    papers_dir.mkdir(parents=True, exist_ok=True)

    with open(out_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    return FetchResult(url=url, ok=True, kind="pdf", out_path=out_path)


def fetch_html(url: str, web_dir: Path) -> FetchResult:
    """Fetch an HTML article, extract clean markdown, download images."""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"fetch returned empty (network / 403 / paywall) — {PLAYWRIGHT_HINT}")

    result = trafilatura.extract(
        downloaded,
        output_format="markdown",
        with_metadata=True,
        include_images=True,
        include_links=True,
        include_tables=True,
    )
    if not result or not result.strip():
        return FetchResult(url=url, ok=False, kind="failed",
                           reason=f"extraction empty (likely paywall or JS-rendered) — {PLAYWRIGHT_HINT}")

    meta = trafilatura.extract_metadata(downloaded)
    title = getattr(meta, "title", None) if meta else None
    author = getattr(meta, "author", None) if meta else None
    pub_date = getattr(meta, "date", None) if meta else None
    language = getattr(meta, "language", None) if meta else None

    slug = slug_from(url, title)
    out_dir = web_dir / slug
    assets_dir = out_dir / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(exist_ok=True)

    md_with_local_images = download_images(result, assets_dir, base_url=url)

    frontmatter_lines = [
        "---",
        f"source_url: {url}",
        f"title: {yaml_escape(title) if title else 'Untitled'}",
    ]
    if author:
        frontmatter_lines.append(f"author: {yaml_escape(author)}")
    if pub_date:
        frontmatter_lines.append(f"published: {pub_date}")
    if language:
        frontmatter_lines.append(f"language: {language}")
    frontmatter_lines.append(f"fetched: {date.today().isoformat()}")
    frontmatter_lines.append("---")
    frontmatter = "\n".join(frontmatter_lines) + "\n\n"

    body = f"# {title or 'Untitled'}\n\n{md_with_local_images}\n"
    (out_dir / "index.md").write_text(frontmatter + body, encoding="utf-8")

    return FetchResult(url=url, ok=True, kind="html", out_path=out_dir)


def download_images(md: str, assets_dir: Path, base_url: str) -> str:
    """Download all images referenced in md, rewrite paths to local assets/."""

    def replace(match: re.Match) -> str:
        alt, src = match.group(1), match.group(2)
        # Resolve relative URLs against the page URL
        if not src.startswith(("http://", "https://")):
            src_abs = urljoin(base_url, src)
        else:
            src_abs = src
        try:
            r = requests.get(
                src_abs,
                timeout=HTML_TIMEOUT,
                headers={"User-Agent": USER_AGENT},
            )
            r.raise_for_status()
        except Exception:
            return match.group(0)  # keep original link on failure

        ext = Path(urlparse(src_abs).path).suffix or ".png"
        if len(ext) > 6:  # weird extension, fallback
            ext = ".png"
        name = hashlib.sha1(src_abs.encode()).hexdigest()[:12] + ext
        (assets_dir / name).write_bytes(r.content)
        return f"![{alt}](assets/{name})"

    return IMG_PATTERN.sub(replace, md)


def yaml_escape(s: str) -> str:
    """Minimal YAML string escape: quote if it contains special chars."""
    if any(c in s for c in ":#\"'\n"):
        return '"' + s.replace('"', '\\"').replace("\n", " ") + '"'
    return s


# --- Inbox rewriting --------------------------------------------------------

def update_inbox(
    inbox_path: Path,
    inbox_text: str,
    results: list[FetchResult],
) -> str:
    """
    Rewrite inbox.md:
    - successful URLs are moved under '## Done'
    - failed URLs stay with a ⚠ reason appended inline
    """
    lines = inbox_text.splitlines()
    today = date.today().isoformat()

    # Build result lookup by URL
    result_by_url = {r.url: r for r in results}

    # Remove the processed unchecked lines; collect new "Done" entries
    new_done_lines: list[str] = []
    out_lines: list[str] = []

    for line in lines:
        match = UNCHECKED_PATTERN.match(line)
        if not match:
            # Also try matching lines with HTML comments after the URL
            comment_match = re.match(r"^- (?:\[ \] )?(https?://\S+)\s*<!--.*?-->\s*$", line)
            if not comment_match:
                out_lines.append(line)
                continue
            url = comment_match.group(1).strip()
        else:
            url = match.group(1).strip()

        if url not in result_by_url:
            out_lines.append(line)
            continue

        result = result_by_url[url]
        if result.ok and result.out_path:
            # vault-relative path for readability
            try:
                rel = result.out_path.relative_to(inbox_path.parent)
            except ValueError:
                rel = result.out_path
            new_done_lines.append(
                f"- {url} → `{rel}` ({today})"
            )
        else:
            out_lines.append(f"- {url} ⚠ {result.reason}")

    # Append new entries to "## Done" section
    final_lines = list(out_lines)
    if new_done_lines:
        final_lines.extend(new_done_lines)

    return "\n".join(final_lines) + ("\n" if inbox_text.endswith("\n") else "")


# --- Orchestration ----------------------------------------------------------

def process_vault(vault: Path, dry_run: bool = False) -> int:
    inbox_path = vault / "inbox.md"
    if not inbox_path.exists():
        print(f"ERROR: inbox.md not found at {inbox_path}", file=sys.stderr)
        return 1

    web_dir = vault / "raw" / "web"
    papers_dir = vault / "raw" / "papers"

    inbox_text = inbox_path.read_text(encoding="utf-8")
    entries = find_unchecked_entries(inbox_text)

    if not entries:
        print("Inbox empty. Nothing to do.")
        return 0

    print(f"Found {len(entries)} URL(s) to process.")
    if dry_run:
        for e in entries:
            print(f"  would fetch: {e.url}")
        return 0

    results: list[FetchResult] = []
    for e in entries:
        fetch_url, slug_override = rewrite_url_for_fetch(e.url)
        if fetch_url != e.url:
            print(f"\n→ {e.url}\n  (fetching as → {fetch_url})")
        else:
            print(f"\n→ {e.url}")

        if is_pdf_url(fetch_url):
            r = fetch_pdf(fetch_url, papers_dir, slug_override=slug_override)
        elif is_youtube_url(fetch_url):
            r = fetch_youtube(fetch_url, web_dir)
        elif is_opencli(fetch_url):
            r = fetch_x_thread(fetch_url, web_dir)
        elif is_walled(fetch_url):
            host = urlparse(fetch_url).netloc.lower()
            r = FetchResult(
                url=fetch_url, ok=False, kind="failed",
                reason=f"walled domain ({host}) — {PLAYWRIGHT_HINT}",
            )
        else:
            r = fetch_html(fetch_url, web_dir)

        # Track by the original inbox URL, not the rewritten fetch URL,
        # so update_inbox can match the line back.
        r.url = e.url
        results.append(r)
        if r.ok:
            print(f"  ✓ {r.kind} → {r.out_path}")
        else:
            print(f"  ⚠ {r.reason}")

    new_text = update_inbox(inbox_path, inbox_text, results)
    inbox_path.write_text(new_text, encoding="utf-8")

    # Summary
    n_html = sum(1 for r in results if r.ok and r.kind == "html")
    n_pdf = sum(1 for r in results if r.ok and r.kind == "pdf")
    n_yt = sum(1 for r in results if r.ok and r.kind == "youtube")
    n_fail = sum(1 for r in results if not r.ok)
    print()
    print(f"Processed {len(results)} URLs:")
    print(f"  ✓ {n_html} HTML article(s) → raw/web/")
    print(f"  ✓ {n_pdf} PDF(s) → raw/papers/")
    if n_yt:
        print(f"  ✓ {n_yt} YouTube transcript(s) → raw/web/")
    if n_fail:
        print(f"  ⚠ {n_fail} failed (see inbox.md for reasons)")

    return 0 if n_fail == 0 else 2  # 2 = partial success


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch URLs from inbox.md into raw/ as markdown."
    )
    parser.add_argument(
        "--vault",
        type=Path,
        default=Path.cwd(),
        help="Path to vault root (default: current directory).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List URLs that would be fetched, don't download.",
    )
    args = parser.parse_args()

    if not args.vault.is_dir():
        print(f"ERROR: vault path is not a directory: {args.vault}",
              file=sys.stderr)
        return 1

    return process_vault(args.vault, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
