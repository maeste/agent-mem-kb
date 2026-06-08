---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-reasoning, causal-reasoning, memory-graph, conflict-detection]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging Memory Retrieval and Reasoning in LLM Agents

**Xiaohui Zhang et al.** (Nanjing University, Alibaba) — arXiv:2603.00026, Feb 2026

## Summary

ActMem affronta il gap fondamentale tra **recuperare** la memoria e **usarla efficacemente**. I framework memoria esistenti trattano gli agenti come "recorder" passivi che recuperano informazioni senza comprenderne le implicazioni profonde. ActMem integra retrieval con **causal reasoning attivo**, trasformando la storia dialogica non strutturata in un grafo causale e semantico.

Meccanismi chiave:
- **Counterfactual reasoning**: deduce vincoli impliciti tra stati passati e intenzioni correnti
- **Commonsense completion**: risolve potenziali conflitti
- **Grafo causale semantico**: struttura per ragionamento logic-driven

Introduce **ActMemEval**, dataset per valutare capabilities di reasoning in scenari logic-driven (oltre al fact-retrieval dei benchmark esistenti). Risultati: supera SOTA in task memory-dependent complessi.

## Key claims
- Il recall non basta: serve causal reasoning sulla memoria ([§Abstract](raw/papers/arxiv-2603.00026.pdf))
- I sistemi attuali falliscono nel detect conflitti e decisioni complesse ([§1](raw/papers/arxiv-2603.00026.pdf))
- ActMemEval sposta il focus da fact-retrieval a reasoning con memoria ([§4](raw/papers/arxiv-2603.00026.pdf))

## Connections
- [[wiki/sources/actmem]] — fonte primaria
- [[wiki/pages/memory-reasoning]] — integrazione memoria-ragionamento
