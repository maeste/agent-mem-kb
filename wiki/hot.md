---
type: page
created: 2026-07-22
updated: 2026-08-29
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-08-29 (cron weekly W35): Review W35 generata (periodo 22-29 ago): settimana vuota verificata. 0 ingest (inbox vuota dall'8 ago), 0 pagine, 0 backlog nascosto (check raw/ ↔ sources/ pulito, nessun branch stranded). 44 sources. Prima settimana senza divergence metadati/contenuti dal reset di luglio. ⚠️ PR #22 compie due settimane (aperta 15 ago): contiene W33+W34+W35 review + daily 20 ago; main ferma al 9 ago, Quartz serve contenuti vecchi finché non si mergea + synca (`git checkout main && git pull && systemctl --user restart quartz.service`).

2026-08-22 (cron weekly W34): Review W34 generata (periodo 15-22 ago): 1 source recuperata dal backlog (vtrivedy-eval-engineering, fetched 25 lug ma mai ingestata), ottava visione in harness-design ("harness che produce eval", formato Harbor, verifier design is hard). 44 sources totali.

2026-08-15 (cron weekly W33): Settimana senza ingest (inbox vuota dall'8 ago). Review W33 generata. RECUPERATO incidente: il lavoro del daily cron 7-8 ago (15 source pages W31, 7a visione harness-design, ByteDance in moe-sparsity, ~20 raw dirs) era rimasto su branch locale vault/2026-08-07-daily mai pushato; index e view in main li referenziavano come dead link. Ripristinati con checkout dal branch. Vault ora integra: 43 sources su disco (26 W30 + 17 W31), 0 W33. Lint eseguito per la prima volta (report .lint/report.md).

## Open threads

- ⚠️ MERGE PR #22: aperta 15 ago, DUE SETTIMANE di vita. Contiene W33 review + daily 20 ago + W34 review + W35 review. Dopo merge: git checkout main && git pull && systemctl --user restart quartz.service
- ROBUSTEZZA CRON: commit_and_pr.sh non verifica l'esito del push (già causato incidente 7-8 ago). Aggiungere retry/errore esplicito + guardia "branch locali non pushati" nel weekly
- Ingest fermo dall'8 ago: due settimane senza input. Verificare se pausa voluta o intoppo nel flusso di aggiunta URL → inbox
- memory-skills page manca Zero-Mem (quarto paradigma non propagato)
- agent-failure-analysis page manca 3 fonti W31 (More-Reflect-Less, Uber ADR, HF Black Hat)
- 6 fonti senza casa concettuale: diffusiongemma, openai-astra-math, openai-gpt-live, xiaomi-robotics-1, firecrawl-anydoc, hassabis-dean-exit
- Comparison view (23 lug) pesantemente outdated: mancano tutte le fonti harness W30-W31
- Compass.md vuoto: `/reflect` non eseguito
- Branch locali non mergiati (vault/2026-05-*, giugno, luglio): molti con contenuto unico pre-reset, da potare dopo verifica
- Fetch vuote/parziali da rifetchare o scartare: alex-l-zhang-...-compositional-generalizers, raw/web/antirez
