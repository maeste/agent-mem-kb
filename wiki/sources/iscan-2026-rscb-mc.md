---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [coding-agents, memory-retrieval, contextual-bandits, risk-sensitive, abstention]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

**Mehmet Iscan** (Yildiz Technical University), arXiv:2604.27283, Apr 2026.

## Summary

Riformula l'uso di issue-memory in coding agenti LLM come problema di **controllo risk-sensitive** selettivo piuttosto che puro top-k retrieval. Introduce **RSCB-MC**, un memory controller contextual bandit risk-sensitive che decide se usare nessuna memoria, iniettare la top resolution, riassumere candidati multipli, fare high-precision/high-recall retrieval, astenersi, o chiedere feedback.

## Key Claims

- In validazione smoke-scale deterministica, RSCB-MC raggiunge **62.5% offline replay success rate** con **0.0% false-positive rate** [[wiki/sources/iscan-2026-rscb-mc]](raw/papers/arxiv-2604.27283.pdf).
- In validazione hotpath 200-case: **60.5% proxy success**, **0.0% false positives**, **331.466 µs p95 decision latency** [[wiki/sources/iscan-2026-rscb-mc]](raw/papers/arxiv-2604.27283.pdf).
- Per coding-agent memory, la domanda principale non è solo quale memoria è più simile, ma **se qualsiasi memoria recuperata è abbastanza sicura** da influenzare la trajectory di debugging [[wiki/sources/iscan-2026-rscb-mc]](raw/papers/arxiv-2604.27283.pdf).
