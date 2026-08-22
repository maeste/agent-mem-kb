---
type: page
created: 2026-07-22
updated: 2026-08-22
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-08-22 (cron weekly W34): Review W34 generata (periodo 15-22 ago): 1 source recuperata dal backlog (vtrivedy-eval-engineering, fetched 25 lug ma mai ingestata), ottava visione in harness-design ("harness che produce eval", formato Harbor, verifier design is hard). 44 sources totali. ⚠️ PR #22 aperta dal 15 ago e NON mergiata: contiene W33 review + daily 20 ago + W34 review; main ferma al 9 ago, Quartz serve contenuti vecchi finché non si mergea + synca (`git checkout main && git pull && systemctl --user restart quartz.service`).

2026-08-20 (cron daily W34): Inbox vuota, ma check incrociato raw/ ↔ sources/ ha scovato un backlog: thread X Trivedy/LangChain eval-engineering (fetched 25 lug, mai ingestato) ora in wiki/sources/ + sezione "Harness che produce eval" in harness-design. the-next-chapter-of-our-ai-momentum = copia ufficiale dell'annuncio già coperto da hassabis-dean-exit (campo canonical). 44 sources. alex-l-zhang-...-compositional-generalizers e raw/web/antirez sono fetch vuote/parziali (solo assets): da rifetchare o scartare.

2026-08-15 (cron weekly W33): Settimana senza ingest (inbox vuota dall'8 ago). Review W33 generata. RECUPERATO incidente: il lavoro del daily cron 7-8 ago (15 source pages W31, 7a visione harness-design, ByteDance in moe-sparsity, ~20 raw dirs) era rimasto su branch locale vault/2026-08-07-daily mai pushato; index e view in main li referenziavano come dead link. Ripristinati con checkout dal branch. Vault ora integra: 43 sources su disco (26 W30 + 17 W31), 0 W33. Lint eseguito per la prima volta (report .lint/report.md).

2026-08-09: Creata slides view self-improvement-continuous-learning (12 slide, 14 based_on): due superfici di miglioramento (modello vs harness/memoria), 3+3 path, 4 paradigmi memoria, self-reflection debunked, WHAT/HOW, back pressure.

## Open threads

- ⚠️ MERGE PR #22: aperta 15 ago, contiene 3 settimane di lavoro (W33 review + daily 20 ago + W34 review). Dopo merge: git checkout main && git pull && systemctl --user restart quartz.service
- ROBUSTEZZA CRON: commit_and_pr.sh non verifica l'esito del push (già causato incidente 7-8 ago). Aggiungere retry/errore esplicito + guardia "branch locali non pushati" nel weekly
- memory-skills page manca Zero-Mem (quarto paradigma non propagato)
- agent-failure-analysis page manca 3 fonti W31 (More-Reflect-Less, Uber ADR, HF Black Hat)
- 6 fonti senza casa concettuale: diffusiongemma, openai-astra-math, openai-gpt-live, xiaomi-robotics-1, firecrawl-anydoc, hassabis-dean-exit
- Comparison view (23 lug) pesantemente outdated: mancano tutte le fonti harness W30-W31
- Compass.md vuoto: `/reflect` non eseguito
- Branch locali non mergiati (vault/2026-05-*, giugno, luglio): molti con contenuto unico pre-reset, da potare dopo verifica
- Fetch vuote/parziali da rifetchare o scartare: alex-l-zhang-...-compositional-generalizers, raw/web/antirez
