---
type: page
created: 2026-07-22
updated: 2026-08-15
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-08-15 (cron weekly W33): Settimana senza ingest (inbox vuota dall'8 ago). Review W33 generata. RECUPERATO incidente: il lavoro del daily cron 7-8 ago (15 source pages W31, 7a visione harness-design, ByteDance in moe-sparsity, ~20 raw dirs) era rimasto su branch locale vault/2026-08-07-daily mai pushato; index e view in main li referenziavano come dead link. Ripristinati con checkout dal branch. Vault ora integra: 43 sources su disco (26 W30 + 17 W31), 0 W33. Lint eseguito per la prima volta (report .lint/report.md).

2026-08-09: Creata slides view self-improvement-continuous-learning (12 slide, 14 based_on): due superfici di miglioramento (modello vs harness/memoria), 3+3 path, 4 paradigmi memoria, self-reflection debunked, WHAT/HOW, back pressure.

2026-08-08: Weekly review W31 riscritta con periodo corretto (1-8 ago, 17 fonti reali). Cluster harness a 7 visioni. Dwarkesh continual learning ingested (ultima fonte).

## Open threads

- ROBUSTEZZA CRON: commit_and_pr.sh non verifica l'esito del push. Il push del 7-8 ago è fallito/saltato silenziosamente. Aggiungere retry/errore esplicito + guardia "branch locali non pushati" nel weekly
- Dopo merge PR: git checkout main && git pull && systemctl --user restart quartz.service (sennò il sito serve contenuti vecchi)
- memory-skills page manca Zero-Mem (quarto paradigma non propagato)
- agent-failure-analysis page manca 3 fonti W31 (More-Reflect-Less, Uber ADR, HF Black Hat)
- 6 fonti senza casa concettuale: diffusiongemma, openai-astra-math, openai-gpt-live, xiaomi-robotics-1, firecrawl-anydoc, hassabis-dean-exit
- Comparison view (23 lug) pesantemente outdated: mancano tutte le fonti harness W30-W31
- Compass.md vuoto: `/reflect` non eseguito
- Branch locali non mergiati (vault/2026-05-*, giugno, luglio): molti con contenuto unico pre-reset, da potare dopo verifica
- Convenzione label settimane: 1-8 ago = W31 ovunque (inaugurale); da Aug 8-15 in poi label ISO (%V del sabato). Nessun contenuto W32
