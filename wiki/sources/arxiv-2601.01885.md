---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [agentic-memory, unified-memory, reinforcement-learning, ltm-stm]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory (AgeMem): Unified LTM/STM Management

**Autori:** Yu et al. (Wuhan University, Alibaba) | **arXiv:** 2601.01885 | **Apr 2026**

## Summary

AgeMem è un framework unificato che integra gestione di long-term memory (LTM) e short-term memory (STM) direttamente nella policy dell'agente, invece di gestirle come componenti separate con euristiche o controller ausiliari. Espone le operazioni di memoria come azioni tool-based, permettendo all'agente LLM di decidere autonomamente cosa e quando memorizzare, recuperare, aggiornare, summarizzare o scartare informazioni.

Per training di comportamenti unificati, propone una strategia RL a tre stadi progressivi con step-wise GRPO per address sparse rewards indotte dalle operazioni memoria.

## Key claims

- L'unificazione LTM/STM nella policy agent supera baselines memory-augmented su 5 benchmark long-horizon [[wiki/pages/agemem]]
- Step-wise GRPO address il problema delle rewards sparse e discontinue nelle operazioni memoria
- Miglior task performance, qualità LTM superiore, uso contesto più efficiente
