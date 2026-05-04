---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, risk-sensitive, coding-agent, contextual-bandit, debugging]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

**Autore:** Mehmet Iscan (Yildiz Technical University)
**Data:** 2026-04-30

## Summary

Riformula l'uso della memoria issue per agenti coding come problema di controllo risk-sensitive piuttosto che retrieval top-k puro. Il sistema decide tra: nessuna memoria, top resolution, sommario multipli, alta precisione, alto recall, astensione, o richiesta feedback. Schema pattern-variant-episode per organizzare issue knowledge. Stato contestuale a 16 feature (rilevanza, incertezza, compatibilità, storia feedback, falso-positivo risk, latenza, costo token).

Risultati: 62.5% replay success rate (non-oracle), 0.0% false-positive rate, 331µs p95 latenza decisionale. Il principio chiave: penalizza più fortemente false-positivi che mancati riutilizzi, rendendo non-iniezione e astensione azioni di sicurezza primarie.

[[wiki/pages/forgetting-memory-governance]] [[wiki/pages/memory-architectures-retrieval]]
