---
type: source
created: 2026-07-24
updated: 2026-07-24
tags: [code-review, ai-code-generation, verification, comprehension-debt, bottleneck, industry-trends]
source_path: raw/web/pragmatic-engineer-code-review-load/index.md
ingested: 2026-W30 (Sat-Sat)
---

# The Pulse: Massive Increase in Code Review Load

**Author:** Gergely Orosz (The Pragmatic Engineer) | **Date:** Jul 23, 2026 | **URL:** https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-concern-about

## Summary

Orosz reports an industry-wide shift: since early 2026 (Opus 4.5, GPT 5.4 generating more and better code), the bottleneck of building software has moved from **coding to code review**. Engineering leaders are scrambling for solutions. The result is a boom in AI code review tools and in-house review automation, but solutions remain experimental and unproven.

## Key Points

### The Bottleneck Shift
- AI code generation (Opus 4.5, GPT 5.4) increased code volume starting January 2026.
- Directors report the software-building bottleneck moved from writing code to reviewing it.

### AI Code Review Tool Boom
- Dedicated tools: CodeRabbit, Greptile, Qodo, SonarQube/Gitar.
- Harness-integrated: Claude Code review, Cursor review, GitHub Copilot review.
- Contextual tools entering the space: Sentry Seer, Linear code reviews.

### In-House Solutions at Scale
- **Uber Code Inbox**: smart assignment, risk profiles estimating change impact.
- **Cloudflare** (AI Code Reviewer), **Faire** (Fairey), **HubSpot** (Sidekick).
- Pattern: in-house implementations outperform vendor integrations for large companies.

### Verify Instead of Review
- Shift from reviewing code to **verifying** it: thorough testing, fuzz testing, formal methods, observability.
- Open question: how much testing counts as "thorough"?

### The Human Cost
- Excessive review load is **burning out engineers**.
- Devs increasingly rubber-stamp PRs when AI reviewers flag nothing — reviewing without intent.
- Reviewers who maintain rigor feel overloaded by "AI slop PRs."

## Connections

- Directly evidences [[wiki/pages/comprehension-debt]]: the gap between code volume and human understanding is widening as review quality degrades.
- Supports [[wiki/sources/addy-osmani-software-factories]] back pressure thesis: autonomy can't expand beyond verification capacity.
- Connects to [[wiki/pages/harness-design]]: the review gate is the choke point in the factory model.
