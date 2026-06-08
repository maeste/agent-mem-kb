---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-retrieval, contextual-bandits, coding-agents, abstention, safety]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

**Mehmet Iscan** (Yildiz Technical University) — arXiv:2604.27283, Apr 2026

## Summary

RSCB-MC (Risk-Sensitive Contextual Bandit Memory Controller) affronta un problema pratico critico: **quando la memoria recuperata è pericolosa**. Nei coding agenti LLM, similarità superficiale tra errori può indurre l'agente ad applicare fix precedenti inappropriati, peggiorando la situazione. Il paper reframa l'uso della memoria issue come problema di **controllo risk-sensitive** piuttosto che puro top-k retrieval.

Il sistema:
- Memorizza knowledge issue-reusable tramite schema **pattern-variant-episode**
- Converte evidence retrieval in stato contestuale a 16 feature: rilevanza, incertezza, compatibilità strutturale, feedback history, false-positive risk, latenza, token cost
- **Penalizza fortemente false-positive memory injection** più del missed reuse
- Supporta azioni: no-memory, top-resolution injection, multi-candidate summary, high-precision/recall retrieval, abstention, ask-feedback

Risultati: 62.5% offline replay success rate (non-oracle), 0.0% false-positive rate, 331.466µs p95 decision latency.

## Key claims
- La domanda principale non è "quale memoria è più simile" ma "è abbastanza sicura?" ([§Abstract](raw/papers/arxiv-2604.27283.pdf))
- La superficial similarity nel debugging è attivamente dannosa ([§1](raw/papers/arxiv-2604.27283.pdf))
- Abstention e non-injection devono essere first-class safety actions ([§3](raw/papers/arxiv-2604.27283.pdf))

## Connections
- [[wiki/sources/iscan-2026-rscb-mc]] — fonte primaria
- [[wiki/pages/memory-safety]] — sicurezza nel retrieval memoria
