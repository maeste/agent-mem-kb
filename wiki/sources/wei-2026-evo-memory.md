---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-benchmark, test-time-learning, self-evolving-memory, lifelong-learning]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-Time Learning with Self-Evolving Memory

**Tianxin Wei et al.** (UIUC, Google DeepMind) — arXiv:2511.20857, Nov 2025

## Summary

Evo-Memory è un benchmark comprehensivo per valutare la memoria auto-evolvente in agenti LLM durante task streaming. A differenza delle valutazioni esistenti che si focalizzano sul recall statico da dialoghi, Evo-Memory richiede agli LLM di cercare, adattare ed evolvere la memoria dopo ogni interazione in flussi di task sequenziali.

Implementa e valuta oltre 10 moduli memoria rappresentativi su 10 dataset diversi (multi-turn goal-oriented, single-turn reasoning, QA). Introduce due contributi metodologici:
- **ExpRAG**: baseline per recuperare e riutilizzare esperienza passata
- **ReMem**: pipeline action-think-memory refine che integra strettamente reasoning, azioni task e aggiornamenti memoria per miglioramento continuo

Il paper argomenta che i sistemi memoria attuali sono statici: recuperano informazioni passivamente invece di evolversi attraverso l'uso. Gli agenti "ricordano cosa è stato detto" ma non "cosa è stato imparato".

## Key claims
- Il reuse di esperienza è distinto dal recall conversazionale ([§1](raw/papers/arxiv-2511.20857.pdf))
- I sistemi memoria esistenti falliscono nell'apprendere da esperienze accumulate ([§1](raw/papers/arxiv-2511.20857.pdf))
- La pipeline ReMem integra reasoning, azioni e aggiornamenti memoria in modo tight ([§3](raw/papers/arxiv-2511.20857.pdf))

## Connections
- [[wiki/sources/wei-2026-evo-memory]] — fonte primaria
- [[wiki/pages/memory-benchmark]] — benchmark per sistemi memoria
