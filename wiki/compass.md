---
type: page
created: 2026-06-08
updated: 2026-06-08
tags: [compass, reflection]
---

# Bussola — 8 Giugno 2026

## Dove sta andando il pensiero

La vault ha raggiunto una **copertura completa delle fonti**: tutti e 44 i paper in `raw/papers/` hanno ora una entry in `wiki/sources/`. Il batch di oggi ha chiuso il gap rimasto da maggio, includendo i fondamenti (Voyager 2023), le survey principali (Du 2026, Yang 2026), i sistemi memoria più recenti (AgeMem, AMA, LightMem, Memanto) e la critica teorica di Xu. La struttura è solida: 5 pagine concettuali + 44 sorgenti organizzate in 8 categorie. La direzione naturale è ora verso **sintesi**: confronti tra architetture, view temporali, e integrazione della critica teorica nelle pagine esistenti.

## Cosa non stiamo guardando

- **Confronti architetturali non scritti**: abbiamo materiale ricco per un confronto sistematico tra approcci alla memoria (graph-based vs typed vs dependency-structured vs retrieval-augmented), ma nessuna view lo formalizza
- **La pagina "memory theory" manca**: la critica di Xu (lookup ≠ memory) è citata in 4 pagine ma non ha una sede dedicata dove sviluppare le implicazioni per system builder
- **Agent skills vs memory: intersezione non mappata**: ProactAgent e SkillRL mostrano che skills e memoria sono due facce della stessa medaglia (entrambe forme di knowledge reuse), ma le pagine sono separate
- **Valutazione empirica frammentata**: ogni paper usa benchmark diversi (LongMemEval, LoCoMo, SWE-Bench, ALFWorld, SciWorld); nessuna sintesi cross-benchmark
- **Lato engineering sotto-rappresentato**: latenza, costo, multi-user, privacy — trattati solo marginalmente nelle sorgenti

## Una domanda worth sitting with

Se Xu ha ragione e l'attuale architettura di memoria agente ha un **generalization ceiling provabile**, allora tutto l'investimento su retrieval migliore, granularità adattiva e governance è ottimizzazione locale di un design fondamentalmente limitato. Quanto vale la pena costruire view e confronti prima di aver risposto a questa domanda? E soprattutto: quali evidenze empirche potrebbero confutare o confermare la tesi del ceiling?
