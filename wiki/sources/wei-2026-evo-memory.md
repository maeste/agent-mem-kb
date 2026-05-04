---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, benchmark, self-evolving, test-time-learning]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory

**Autori:** Tianxin Wei et al. (UIUC, Google DeepMind)
**Data:** 2025-11-25

## Summary

Evo-Memory è un benchmark e framework per valutare memoria self-evolving in agenti LLM. Struttura dataset in stream sequenziali di task, richiedendo ricerca, adattamento ed evoluzione della memoria dopo ogni interazione. Implementa >10 moduli di memoria rappresentativi valutati su 10 dataset multi-turno e single-turn.

Introduce due baseline: ExpRAG per retrieval di esperienza priore, e ReMem, una pipeline action-think-memory-refine che integra reasoning, azioni e aggiornamenti di memoria per miglioramento continuo. Il benchmark espone il gap tra recall conversazionale statica e riutilizzo dell'esperienza per reasoning futuro.

[[wiki/pages/experience-reuse-continual-learning]] [[wiki/pages/llm-agent-memory]]
