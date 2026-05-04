---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, reinforcement-learning, unified-memory]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management

**Autori:** Yi Yu et al. (Wuhan University, Alibaba Group)
**Data:** 2026-04-30 (v2)

## Summary

AgeMem unifica gestione di LTM e STM direttamente nella policy dell'agente, esponendo operazioni di memoria come azioni tool-based (store, retrieve, update, summarize, discard). Addestra questi comportamenti con una strategia RL progressiva in tre fasi e step-wise GRPO per rewards sparsi e discontinui indotti dalle operazioni di memoria.

Su cinque benchmark long-horizon, supera consistentemente baseline memory-augmented con miglior task performance, memoria LTM di qualità superiore e uso più efficiente del contesto. Dimostra che apprendere le decisioni di memoria end-to-end supera approcci euristici e controllori ausiliari separati.

[[wiki/pages/memory-architectures-retrieval]] [[wiki/pages/llm-agent-memory]]
