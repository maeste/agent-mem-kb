---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [memory-benchmark, test-time-learning, self-evolving-memory, lifelong-learning]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-Time Learning with Self-Evolving Memory

**Tianxin Wei et al.** (UIUC, Google DeepMind), arXiv:2511.20857, Nov 2025.

## Summary

Evo-Memory è un benchmark e framework comprehensivo per valutare **self-evolving memory** in agenti LLM. Struttura dataset in stream sequenziali di task, richiedendo alle LLM di cercare, adattare ed evolvere la memoria dopo ogni interazione. Implementa oltre 10 moduli memoria rappresentativi e li valuta su 10 dataset multi-turn goal-oriented, single-turn reasoning e QA. Propone **ReMem**, un pipeline action-think-memory refine che integra ragionamento, azioni task e aggiornamenti memoria per miglioramento continuo.

## Key Claims

- I sistemi memoria esistenti sono largamente statici: recuperano informazioni passivamente piuttosto che evolversi attraverso l'uso [[wiki/sources/wei-2026-evo-memory]](raw/papers/arxiv-2511.20857.pdf).
- Gli agenti "ricordano cosa è stato detto" ma non "cosa hanno imparato": la conversational recall recupera fatti passati, mentre l'experience reuse astrae strategie di ragionamento per task futuri [[wiki/sources/wei-2026-evo-memory]](raw/papers/arxiv-2511.20857.pdf).
- ReMem dimostra che l'integrazione stretta tra ragionamento, azioni e aggiornamenti memoria abilita miglioramento continuo [[wiki/sources/wei-2026-evo-memory]](raw/papers/arxiv-2511.20857.pdf).
