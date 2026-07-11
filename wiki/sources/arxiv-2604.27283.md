---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [coding-agents, memory-retrieval, contextual-bandits, risk-sensitive, abstention, debugging]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

**Iscan** (Yildiz Technical University) — arXiv:2604.27283, Apr 2026

## Summary

RSCB-MC è un controllore di memoria basato su contextual bandit per agent di coding che decide **se** e **come** usare la memoria passata durante il debugging, trattando l'iniezione di memoria come problema di controllo risk-sensitive piuttosto che puro top-k retrieval.

## Claim principali

- **Problema reale**: nel debugging, similarità superficiale è ingannevole. Diverse root cause possono produrre stack trace quasi identici (es. SQLite locked vs stale migration, wrong venv vs wrong PYTHONPATH). Retrieval by similarity può attivamente peggiorare la situazione [[raw/papers/arxiv-2604.27283.pdf]].
- **Architettura RSCB-MC**: decide tra 7 azioni: no memory, inject top resolution, summarize candidates, high-precision retrieval, high-recall retrieval, **abstain**, ask for feedback. Lo stato contestuale ha 16 feature fisse (rilevanza, incertezza, compatibilità strutturale, history feedback, false-positive risk, latenza, token cost) [[raw/papers/arxiv-2604.27283.pdf]].
- **Reward design**: penalizza false-positive memory injection più forte del missed reuse. Non-injection e abstention sono azioni di safety first-class [[raw/papers/arxiv-2604.27283.pdf]].
- **Pattern-Variant-Episode schema**: organizza knowledge issue riutilizzabile con varianti di pattern [[raw/papers/arxiv-2604.27283.pdf]].
- **Risultati**: 62.5% offline replay success rate (non-oracle), 0.0% false-positive rate. In validazione hotpath 200-case: 60.5% proxy success, 0.0% false positives, 331µs p95 decision latency [[raw/papers/arxiv-2604.27283.pdf]].
- **Claim centrale**: per coding-agent memory, la domanda principale non è "quale memoria è più simile" ma "**qualsiasi memoria recuperata è abbastanza sicura da influenzare la trajectory?**" [[raw/papers/arxiv-2604.27283.pdf]].

## Posizione nel dibattito

Primo lavoro a trattare false-positive memory injection come evento di safety first-class nel debugging agentic. Complementa i lavori su RAG selettivo focalizzandosi specificamente sul setting operativo del coding agent.
