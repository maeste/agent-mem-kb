---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [dependency-structured-memory, context-management, reasoning-graph, swe-bench]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Selective and Dependency-Structured Memory Construction

**Yating Wu et al.** (UT Austin, AWS AI Labs) — arXiv:2604.23069, Apr 2026

## Summary

ContextWeaver è un framework di memoria **dependency-structured** che organizza la traccia di interazione di un agente in un grafo di step di reasoning e seleziona il contesto rilevante per azioni future. A differenza degli approcci esistenti (sliding window, prompt compression, retrieval-based) che selezionano contenuto basandosi su recency/salience/similarity semantica, ContextWeaver cattura la **struttura di dipendenza** che collega ogni reasoning step ai precedenti.

Tre componenti:
1. **Dependency-based construction**: linka ogni reasoning step agli step precedenti da cui dipende
2. **Compact dependency summarization**: condensa path root-to-step in unità riutilizzabili
3. **Lightweight validation layer**: incorpora feedback di esecuzione

Valutato su SWE-Bench Verified e Lite: migliora pass@1 vs sliding-window baseline, riducendo reasoning steps e token usage. L'osservazione chiave: modellare dipendenze logiche fornisce un meccanismo di memoria stabile e scalabile per agenti che usano tools.

## Key claims
- I segnali recency/salience non catturano dipendenze tra reasoning steps ([§Abstract](raw/papers/arxiv-2604.23069.pdf))
- La perdita di dipendenze causa piani rotti, ripetizione explorazione, passi inconsistenti ([§1](raw/papers/arxiv-2604.23069.pdf))
- Il grafo di dipendenza è più stabile dello sliding window per task multi-step ([§4](raw/papers/arxiv-2604.23069.pdf))

## Connections
- [[wiki/sources/wu-2026-contextweaver]] — fonte primaria
- [[wiki/pages/structured-context]] — contesto strutturato per agenti
