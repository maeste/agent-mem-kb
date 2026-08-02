---
type: page
created: 2026-07-22
updated: 2026-08-01
tags: [log]
---

# Log

Append-only log of vault operations.

Format: `## [YYYY-Www] YYYY-MM-DD | op | title`

Week runs Saturday 13:00 → next Saturday 12:59 (custom week boundary).

## [W30/2026] 2026-07-22 | cleanup | Vault v2 reset: cleared all raw/papers, wiki/pages, wiki/sources. Reset inbox, index, hot, log, compass to empty templates. Added time-tracking fields (ingested), weekly views, Sat-Sat week boundary.

## [W30/2026] 2026-07-23 | ingest | Bulk ingest of 8 new sources (12 total). Sources created: addy-osmani-software-factories, akash-bajwa-sparse-by-design, alex-zhang-harness-2026, arxiv-2607-09197-routing-meaningful, arxiv-2607-09510-failure-as-process, arxiv-2607-12227-harness-evaluation, arxiv-2607-12747-oat-failure-attribution, arxiv-2607-16621-msce-memory-skills. Index updated with topic grouping. Inbox cleared after successful fetch (prior session).

## [W30/2026] 2026-07-23 | ingest | Created 6 conceptual pages: harness-design, comprehension-debt, compositional-generalization, moe-sparsity, agent-failure-analysis, memory-skills-co-evolution. Each page cross-references 2-4 sources. Graph now has real nodes and edges.

## [W30/2026] 2026-07-23 | view | Created comparison view: comparison-graph-vs-loop. Maps all-grafo vs all-loop across 8 dimensions, identifies 4 unresolved tensions (routing vs observation, visibility vs prevention, design vs search, structure vs bitter lesson). Based on 4 pages + 5 sources.

## [W30/2026] 2026-07-24 | ingest | Fetched + ingested 1 source: pragmatic-engineer-code-review-load (Orosz on the code review bottleneck shift since Q1 2026). Updated comprehension-debt page with industrial evidence section. Index updated.

## [W30/2026] 2026-07-25 | ingest | Cron run. Fetched 2 URLs via inbox-fetcher skill (web_extract backend unavailable, used script directly): arxiv-2607.13285 (Harness Handbook, PDF) + anthropic-claude-opus-5 (HTML). Created 2 source pages. Updated harness-design page with 4th perspective (behavior localization). Index + timeline updated. X.com URL remains walled (needs interactive Playwright).

## [W30/2026] 2026-07-25 | weekly | First weekly review generated (2026-W30.md). 15 sources, 6 pages, 1 comparison view. Harness design identified as convergent fulcrum across 5 sources. 4 unresolved tensions mapped. 5 sources still without conceptual pages. Index + hot.md updated.

## [W30/2026] 2026-07-31 | ingest | Cron daily fetch + ingest. Fetched 1 source: thinking-machines-inkling-small (Inkling-Small MoE 276B/12B, Thinking Machines Lab Jul 30 2026). Created source page + updated moe-sparsity page with new data point (12B/276B, ~4.4% attivi, reasoning effort controllabile). Index updated (W30 now 14 sources / 7 pages touched). Inbox empty again.

## [W30/2026] 2026-08-01 | ingest | Cron daily fetch + ingest. Fetched 6/9 URLs (3 failed: agentbehavior.dev, danielmiessler.com, kaitchup.substack.com — need Playwright, deferred). Created 6 source pages: gemini-robotics-er-2 (embodied reasoning), openai-gpt-5-6-pricing (Luna -80%, Sol auto-kernels), openai-arc-agi-3-harness (retained reasoning + compaction = 3x score), anthropic-claude-5-context-engineering (80% system prompt removed), arxiv-2607.13285-harness-handbook (behavior localization), arxiv-2607.20064-pro-long (programmatic memory). Updated harness-design page (+3 sections: harness as measured variable, behavior localization, less prescriptive harnesses) and memory-skills-co-evolution page (+PRO-LONG programmatic memory, +Claude 5 auto-memory). Inbox fix: converted `- URL` to `- [ ] URL` format (checkbox trap). Index updated (W30 now 20 sources / 9 pages touched). Fixed cron path bug: fetch_inbox.py lives at .claude/skills/inbox-fetcher/scripts/, not vault root.
