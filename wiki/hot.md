---
type: page
created: 2026-07-22
updated: 2026-08-08
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-08-08 (cron weekly): Weekly review W31 riscritta completamente. La versione precedente elencava fonti W30 con date errate. Nuova versione: 16 fonti reali W31 (2-8 ago), 2 pagine modificate (harness-design +7 visioni, moe-sparsity +Qwen/ByteDance), 6 connessioni documentate. Cluster harness esploso: 6 nuove fonti lungo lo spettro auto-prodotto (Qwen) ↔ externalizzato (LoopX), con continual (Prime, Muse) e standalone (Kiro) in mezzo. Agent security emerso come dominio (HF Black Hat + Uber ADR). Self-reflection empiricamente debunked. 42 sources totali.

2026-08-08 (cron daily): 3 new URLs fetched: ByteDance 10T (~10T params pre-training), LoopX (state kernel provider-neutral), Google Pichai blog (fonte primaria Hassabis/Dean exit). 2 new source pages, 1 arricchito.

2026-08-07: 9 source pages created (cron batch): hassabis-dean-exit, prime-agent, zero-mem, kiro-agent-harness, meta-muse-code-spark-1-2, openai-gpt-live, openai-astra-math, diffusiongemma, firecrawl-anydoc, uber-adr, xiaomi-robotics-1, openai-hf-black-hat-debrief, arxiv-2607.28576-more-reflect-less.

2026-08-04: Qwen3.8-Max ingested. 2.4T/95B MoE, harness auto-prodotto (6a visione).

2026-08-01: Weekly review W31 (versione errata, poi corretta). 24 sources, 6 pages, 1 view.

## Open threads

- memory-skills page manca Zero-Mem (quarto paradigma non propagato)
- agent-failure-analysis page manca 3 fonti W31 (More-Reflect-Less, Uber ADR, HF Black Hat)
- 6 fonti senza casa concettuale: diffusiongemma, openai-astra-math, openai-gpt-live, xiaomi-robotics-1, firecrawl-anydoc, hassabis-dean-exit. Pagine candidate: agent-security, diffusion-architecture, realtime-systems
- Comparison view (23 lug) pesantemente outdated: mancano tutte le 7 fonti harness W30-W31
- Compass.md vuoto: `/reflect` non eseguito
- Lint non ancora eseguito sul vault
- 3 inbox URLs failano nel cron (JS rendering): serve fallback Playwright
