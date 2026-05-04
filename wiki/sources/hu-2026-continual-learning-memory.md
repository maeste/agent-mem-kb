---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, continual-learning, experience-reuse, stability-plasticity]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents

**Autori:** Qisheng Hu, Quanyu Long, Wenya Wang (NTU Singapore)
**Data:** 2026-04-29

## Summary

Dimostra che la memoria esterna non risolve il problema del continual learning ma lo riposiziona: il collo di bottiglia si sposta dall'aggiornamento parametrico al retrieval sotto finestra di contesto finita. Introduce un framework (k, v) che disaccoppia come l'esperienza è rappresentata (k) e come è organizzata per il retrieval (v).

Su ALFWorld e BabyAI: memorie procedurali astratte si trasferiscono più affidabilmente delle traiettorie dettagliate; il negative transfer danneggia sproporzionatamente i casi hard; organizzazione più fine della memoria non è universalmente benefica e può indurre grave forgetting. Il dilemma stabilità-plasticità persiste, solo in una forma diversa.

[[wiki/pages/experience-reuse-continual-learning]] [[wiki/pages/llm-agent-memory]]
