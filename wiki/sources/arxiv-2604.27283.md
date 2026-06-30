---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, coding-agents, contextual-bandits, retrieval, safety]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# Learning When to Remember: RSCB-MC for Coding Agent Memory

**Iscan (2026)** — Yildiz Technical University

## Summary

RSCB-MC (Risk-Sensitive Contextual Bandit Memory Controller) affronta un problema pratico nei coding agenti basati su LLM: il **retrieval di memoria per similarità superficiale può essere dannoso** in debugging. Stack trace simili, errori di terminal, o sintomi configurativi possono avere cause radicalmente diverse; iniettare una "fix" precedente basata solo sulla somiglianza di superficie può spingere l'agente su una strategia di riparazione errata.

Il sistema introduce uno schema **pattern-variant-episode** per memorizzare knowledge riutilizzabile e converte l'evidenza di retrieval in uno stato contestuale a 16 feature (rilevanza, incertezza, compatibilità strutturale, storia feedback, rischio falso positivo, latenza, costo token). Il reward design penalizza i falsi positivi più dei miss.

## Risultati

- Offline replay success rate: **62.5%** con **0.0% false-positive rate**
- Hot-path validation (200 casi): **60.5%** proxy success, **0.0% false positives**, p95 latency **331.466 µs**

## Claim chiave

- Per la memoria dei coding agenti, la domanda centrale non è "quale memoria è più simile" ma "se qualsiasi memoria recuperata è abbastanza sicura da influenzare la traiettoria di debug" [[wiki/sources/arxiv-2604.27283]]
- L'abstention (non usare memoria) deve essere una first-class action di sicurezza [[wiki/sources/arxiv-2604.27283]]
