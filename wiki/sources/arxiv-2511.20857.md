---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, benchmark, self-evolving, test-time-learning, streaming]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-Time Learning with Self-Evolving Memory

**Autori:** Tianxin Wei, Noveen Sachdeva, Benjamin Coleman et al. (UIUC, Google DeepMind)
**arXiv:** 2511.20857 | Novembre 2025

## Riassunto

Evo-Memory è un benchmark e framework comprehensivo per valutare la memoria self-evolving in agenti LLM. A differenza delle valutazioni statiche conversazionali esistenti (dove la memoria è passivamente recuperata), Evo-Memory struttura dataset in stream sequenziali di task, richiedendo agli LLM di cercare, adattare ed evolvere la memoria dopo ogni interazione.

Implementa e valuta oltre 10 moduli memory rappresentativi su 10 dataset diversi (multi-turn goal-oriented, single-turn reasoning, QA). Introduce due baseline:
- **ExpRAG**: metodo per recuperare e utilizzare esperienza precedente
- **ReMem**: pipeline action-think-memory refine che integra strettamente reasoning, azioni task e memory refinement

Il benchmark espone il gap tra memoria statica e capacità di apprendimento continuo durante deployment.

## Claim chiave

- Le valutazioni memory statiche sottostimano le capacità richieste per agenti in ambienti streaming reali [[wiki/sources/arxiv-2511.20857.md]]
- L'evoluzione della memoria durante il test-time (non solo retrieval) è necessaria per performance sostenute [[wiki/sources/arxiv-2511.20857.md]]
- Unificare reasoning, azioni e memory refinement in un'unica pipeline migliora rispetto a approcci separati [[wiki/sources/arxiv-2511.20857.md]]

## Collegamenti

- Benchmark complementare a [[wiki/sources/du-2026-memory-survey.md]] che survey meccanismi di valutazione
- Relazionato a [[wiki/pages/memory-systems]]
- ReMem come approccio alternativo a [[wiki/sources/actmem.md]] (ActMem)
