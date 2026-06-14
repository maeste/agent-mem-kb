---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [memory-reasoning, causal-reasoning, memory-graph, conflict-detection]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging Memory Retrieval and Reasoning in LLM Agents

**ActMem authors**, arXiv:2603.00026, Mar 2026.

## Summary

ActMem è un framework di **actionable memory** che integra retrieval memoria con ragionamento causale attivo. Trasforma la storia dialogica non strutturata in un grafo causale e semantico, usando counterfactual reasoning e commonsense completion per dedurre vincoli impliciti e risolvere conflitti tra stati passati e intenzioni correnti. Introduce il dataset **ActMemEval** per valutare capacità di ragionamento logic-driven in scenari memory-dependent.

## Key Claims

- I framework memoria esistenti trattano gli agenti come "recorder" passivi che recuperano informazioni senza comprenderne le implicazioni profonde [[wiki/sources/actmem]](raw/papers/arxiv-2603.00026.pdf).
- ActMem supera significativamente gli SOTA baselines su task complessi dipendenti dalla memoria [[wiki/sources/actmem]](raw/papers/arxiv-2603.00026.pdf).
- Il benchmark ActMemEval sposta il focus dal fact-retrieval al reasoning logic-driven con dipendenza dalla memoria [[wiki/sources/actmem]](raw/papers/arxiv-2603.00026.pdf).
