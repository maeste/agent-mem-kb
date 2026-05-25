---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [actionable-memory, causal-reasoning, counterfactual-reasoning, conflict-detection]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents

**Autori:** vari | **arXiv:** 2603.00026 | **Marzo 2026**

## Sintesi

ActMem affronta il divario tra ricordare e usare efficacemente la memoria. I framework esistenti trattano gli agent come "recorder" passivi che recuperano informazioni senza comprenderne le implicazioni profonde. ActMem integra retrieval con **ragionamento causale attivo**.

## Architettura

- Trasforma la storia di dialogo non strutturata in un **grafo causale e semantico**
- Usa **counterfactual reasoning** e **commonsense completion** per dedurre vincoli impliciti
- Risolve potenziali conflitti tra stati passati e intenzioni correnti
- Introduce **ActMemEval**, dataset per valutare ragionamento logic-driven in scenari memory-dependent

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — approccio causal-graph alla memoria agent
