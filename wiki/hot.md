---
type: page
created: 2026-07-22
updated: 2026-08-01
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-08-01: Cron daily fetch + ingest. 6/9 URLs fetched (3 failed: need Playwright). Cluster dominante: agent harness + context management. Tre fonti convergenti (OpenAI ARC-AGI-3, Anthropic Claude 5, Harness Handbook) ribadiscono che l'harness è la variabile misurata, non solo il modello. PRO-LONG introduce programmatic memory come quarto paradigma oltre L1/L2/L3. harness-design page ora ha 5 visioni invece di 3. Vault: 20 sources, 9 pages touched in W30.

2026-07-31: Inkling-Small ingested. 14 sources total.

2026-07-26: Weekly review W30 generated. 15 sources, 6 conceptual pages, 1 comparison view. 5 cross-source connections documented.

2026-07-25 (cron): Fetched 2 URLs (arxiv-2607.13285 Harness Handbook + Anthropic Claude Opus 5). Created source pages, added 4th perspective to harness-design page.

2026-07-24: Pragmatic Engineer code review bottleneck. 13 sources.

2026-07-23: Bulk ingest + 6 conceptual pages. Vault structure established.

## Open threads

- 3 inbox URLs failed (agentbehavior.dev, danielmiessler.com, kaitchup.substack.com): need Playwright fallback in interactive session
- Cron path bug: prompt says `fetch_inbox.py` but script is at `.claude/skills/inbox-fetcher/scripts/fetch_inbox.py` — broken since Jul 27, needs cron prompt fix
- Inbox format drift: was `- URL`, fetcher requires `- [ ] URL` — converted today, may regress
- Weekly review W30 scheduled Saturday 13:00 (first run today at 13:00)
- Pages with no conceptual home yet: gemini-robotics-er-2 (embodied reasoning), openai-gpt-5-6-pricing (pricing/efficiency)
- PRO-LONG + OpenAI ARC-AGI-3 + Harness Handbook: emerging thread on behavior localization as the real bottleneck of agent systems, not capability generation
- Compass.md vuoto: `/reflect` non ancora eseguito
- Lint non ancora eseguito sul vault
