---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [dependency-structured-memory, context-management, reasoning-graph, tool-use]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Selective and Dependency-Structured Memory Construction

**Yating Wu et al.** (UT Austin, AWS AI Labs), arXiv:2604.23069, Apr 2026.

## Summary

ContextWeaver è un framework di memoria **selective e dependency-structured** che organizza la traccia di interazione di un agente in un grafo di passaggi di ragionamento e seleziona il contesto rilevante per azioni future. Supporta: (1) costruzione e traversamento basati su dipendenze, (2) riassunti compatti delle dipendenze, (3) un layer lightweight di validazione con feedback di esecuzione.

## Key Claims

- Su **SWE-Bench Verified e Lite**, ContextWeaver migliora performance rispetto a sliding-window baseline in **pass@1**, riducendo reasoning steps e token usage [[wiki/sources/wu-2026-contextweaver]](raw/papers/arxiv-2604.23069.pdf).
- I segnali di recency/salience/semantic similarity non catturano la struttura di dipendenza che collega un passo di ragionamento al successivo [[wiki/sources/wu-2026-contextweaver]](raw/papers/arxiv-2604.23069.pdf).
- La modellazione delle dipendenze logiche fornisce un meccanismo di memoria stabile e scalabile per agenti LLM che usano tools [[wiki/sources/wu-2026-contextweaver]](raw/papers/arxiv-2604.23069.pdf).
