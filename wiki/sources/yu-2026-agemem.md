---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [unified-memory, long-term-memory, short-term-memory, reinforcement-learning]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory (AgeMem): Learning Unified LTM and STM Management

**Yi Yu et al.** (Wuhan University, Alibaba), arXiv:2601.01885, Apr 2026.

## Summary

AgeMem è un framework unificato che integra gestione **long-term memory (LTM)** e **short-term memory (STM)** direttamente nella policy dell'agente. Espone operazioni di memoria come azioni tool-based, permettendo all'agente LLM di decidere autonomamente cosa e quando memorizzare, recuperare, aggiornare, riassumere o scartare informazioni. Usa una strategia RL a tre stadi progressivi con step-wise GRPO per gestire reward sparse e discontinue indotte dalle operazioni memoria.

## Key Claims

- AgeMem supera consistentemente i baseline memory-augmented su **5 benchmark long-horizon** con multiple LLM backbones [[wiki/sources/yu-2026-agemem]](raw/papers/arxiv-2601.01885.pdf).
- Migliora task performance, qualità della LTM e uso efficiente del contesto rispetto a sistemi che trattano LTM e STM come componenti separati [[wiki/sources/yu-2026-agemem]](raw/papers/arxiv-2601.01885.pdf).
- L'approccio unificato elimina la necessità di euristiche o controller ausiliari per la gestione memoria [[wiki/sources/yu-2026-agemem]](raw/papers/arxiv-2601.01885.pdf).
