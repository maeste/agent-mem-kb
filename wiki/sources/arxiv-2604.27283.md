---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [memory-retrieval, contextual-bandits, coding-agents, abstention]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Bandits for Memory Retrieval in Coding Agents

**Autore:** Mehmet Iscan (Yildiz Technical University) | **arXiv:** 2604.27283 | **Apr 2026**

## Summary

Riformula l'uso della memoria issue negli agenti coding come problema di controllo risk-sensitive piuttosto che puro top-k retrieval. Il problema operativo: stack trace simili possono avere root cause diverse, e unsafe memory injection anchor l'agente su strategie repair errate.

**RSCB-MC** è un contextual bandit memory controller che decide se usare nessuna memoria, injectare la top resolution, summarizzare candidati multipli, fare retrieval high-precision/high-recall, astenersi, o chiedere feedback. Usa 16 feature di stato contestuale (relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, token cost). Penalizza fortemente false-positive più di missed reuse.

## Key claims

- Offline replay success rate 62.5% (non-oracle migliore) con 0.0% false-positive rate [[wiki/pages/rscb-mc]]
- Hotpath validation 200-case: 60.5% proxy success, 0.0% false positives, p95 latency 331.466 µs
- Per coding-agent memory, la domanda principale non è "quale memoria è più simile" ma "qualsiasi memoria recuperata è abbastanza sicura da influenzare la trajectory"
