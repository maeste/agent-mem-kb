---
type: page
created: 2026-07-22
updated: 2026-07-31
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-07-31: Cron daily fetch + ingest. Inkling-Small (Thinking Machines Lab, MoE 276B/12B) fetched from inbox and ingested. Updated moe-sparsity page: adds 4.4% activation data point alongside Mixtral/Kimi. Source connects to existing sparsity thread. 14 sources total now.

2026-07-26: Weekly review W30 generated. 15 sources, 6 conceptual pages, 1 comparison view. 5 cross-source connections documented. Vault has real structure now: sources cluster around agentic engineering / harness design, with secondary clusters in model scaling (MoE) and multi-model routing.

2026-07-25 (cron): Fetched 2 URLs (web_extract backend down, used fetch_inbox.py core): arxiv-2607.13285 Harness Handbook + Anthropic Claude Opus 5. Created source pages, added 4th perspective to harness-design page (behavior localization as prerequisite to evolution). X.com URL walled, left for interactive session. 15 sources total now.

2026-07-24 (cron): Fetched Pragmatic Engineer article on code review load bottleneck. Created source page + linked to comprehension-debt page (industrial evidence). 13 sources total now.

2026-07-24: Last ingest was pragmatic-engineer-code-review-load (Orosz). Confirmed comprehension-debt thesis with industrial data.

## Open threads

- 5 fonti senza pagina concettuale: google-gemini-3-6-flash, anthropic-claude-opus-5, qwen-image-3, openai-hf-security-incident, antirez-news-170
- X.com URL in inbox è walled (needs interactive Playwright session)
- Quartz UI live at https://hermes-server.tail732fb8.ts.net/ (needs Tailscale on device)
- Weekly review W30 scheduled Saturday 13:00 (first run)
- Inbox empty, ready for new URLs
- Pages to expand: antirez-news-170, google-gemini-3-6-flash, openai-hf-security-incident, qwen-image-3 have no page references yet
- Inkling-Small reasoning effort controllabile: potenziale spunto per nuove pagine su test-time compute scaling
- Comparison view (graph-vs-loop) ha 4 tensioni irrisolte: candidata per espansione quando nuove fonti le indirizzeranno
- Routing multi-model (arxiv-2607-09197) sola nel cluster: da monitorare
- Compass.md vuoto: `/reflect` non ancora eseguito
- Lint non ancora eseguito sul vault
