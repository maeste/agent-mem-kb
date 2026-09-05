---
type: page
created: 2026-07-22
updated: 2026-09-05
tags: [hot-cache]
---

# Hot Cache

Short rolling memory of recent sessions. Rewritten at session end.
Read by the agent at session start.

## Current state

2026-09-05 (cron weekly W36): Review W36 generata (periodo 29 ago-5 set): TERZA settimana consecutiva vuota. 0 ingest (inbox vuota dall'8 ago), 0 pagine, 0 recuperi (check raw/ ↔ sources/ pulito, solo i 6 falsi orfani noti). 44 sources (26 W30 + 17 W31 + 1 W34), 6 pages. Tre settimane = regime, non anomalia: collo della bottiglia a monte (flusso URL → inbox). ⚠️ PR #22 compie TRE settimane (aperta 15 ago): contiene W33+W34+W35 review + daily 20 ago, si aggiunge la W36. Main ferma al 9 ago: Quartz serve contenuti freschi da disco locale, ma main è indietro di 4 settimane e il rischio perdita (crash disco senza push) cresce. Dopo merge: `git checkout main && git pull && systemctl --user restart quartz.service`.

2026-08-29 (cron weekly W35): Review W35 generata (periodo 22-29 ago): settimana vuota verificata. 0 ingest (inbox vuota dall'8 ago), 0 pagine, 0 backlog nascosto. Prima settimana senza divergence metadati/contenuti dal reset di luglio.

2026-08-22 (cron weekly W34): Review W34 generata: 1 source recuperata dal backlog (vtrivedy-eval-engineering, fetched 25 lug ma mai ingestata), ottava visione in harness-design ("harness che produce eval", formato Harbor). 44 sources totali.

## Open threads

- ⚠️ MERGE PR #22: aperta 15 ago, TRE SETTIMANE di vita. Contiene W33 review + daily 20 ago + W34 review + W35 review + W36 review. Dopo merge: git checkout main && git pull && systemctl --user restart quartz.service
- ⚠️ Ingest fermo dall'8 ago: TRE settimane senza input. Verificare se pausa voluta o intoppo nel flusso di aggiunta URL → inbox
- ROBUSTEZZA CRON: commit_and_pr.sh non verifica l'esito del push (già causato incidente 7-8 ago). Aggiungere retry/errore esplicito + guardia "branch locali non pushati" nel weekly
- memory-skills page manca Zero-Mem (quarto paradigma non propagato)
- agent-failure-analysis page manca 3 fonti W31 (More-Reflect-Less, Uber ADR, HF Black Hat)
- 6 fonti senza casa concettuale: diffusiongemma, openai-astra-math, openai-gpt-live, xiaomi-robotics-1, firecrawl-anydoc, hassabis-dean-exit
- Comparison view (23 lug) pesantemente outdated: mancano tutte le fonti harness W30-W31
- Compass.md vuoto: `/reflect` non eseguito
- Branch locali non mergiati (vault/2026-05-*, giugno, luglio): molti con contenuto unico pre-reset, da potare dopo verifica
- Fetch vuote/parziali da rifetchare o scartare: alex-l-zhang-...-compositional-generalizers, raw/web/antirez
