---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [memory-benchmark, test-time-learning, self-evolving-memory, lifelong-agents]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-Time Learning

**Autori:** Wei et al. (UIUC, Google DeepMind) | **arXiv:** 2511.20857 | **Nov 2025**

## Summary

Evo-Memory è un benchmark streaming per valutare memoria self-evolving in agenti LLM. Struttura dataset come stream sequenziali di task, richiedendo agli LLM di cercare, adattare e far evolvere la memoria dopo ogni interazione. Implementa e valuta oltre 10 moduli memoria rappresentativi su 10 dataset multi-turn goal-oriented e single-turn reasoning/QA.

Include due contributi metodologici:
- **ExpRAG**: baseline per recuperare e riutilizzare esperienza precedente
- **ReMem**: pipeline action-think-memory refine che integra strettamente reasoning, azioni task e aggiornamenti memoria per miglioramento continuo

## Key claims

- Le valutazioni esistenti si focalizzano su setting conversazionali statici, ignorando la capacità dinamica di accumulare e riutilizzare esperienza [[wiki/pages/evo-memory]]
- Il benchmark copre 10 dataset diversificati con oltre 10 architetture memoria implementate
- ReMem dimostra che l'integrazione stretta tra reasoning e update memoria supera approcci di retrieval passivo
