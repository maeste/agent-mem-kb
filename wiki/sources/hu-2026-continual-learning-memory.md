---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [continual-learning, experience-reuse, memory-representation, negative-transfer]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Qisheng Hu et al.** (NTU Singapore), arXiv:2604.27003, Apr 2026.

## Summary

Studio di come il **continual learning** si manifesta in agenti memoria-augmented. Mostra che la memoria esterna non elimina la sfida stability-plasticità ma la **relocalizza al livello della memoria**: sotto una context window limitata, esperienze vecchie e nuove competono durante retrieval. Introduce un framework (k, v) che disentangle rappresentazione dell'esperienza e organizzazione per retrieval.

## Key Claims

- Le memorie procedurali astratte transferiscono più affidabilmente delle traiettorie dettagliate [[wiki/sources/hu-2026-continual-learning-memory]](raw/papers/arxiv-2604.27003.pdf).
- Il **negative transfer** danneggia sproporzionatamente i casi difficili [[wiki/sources/hu-2026-continual-learning-memory]](raw/papers/arxiv-2604.27003.pdf).
- L'organizzazione a granularità fine non è universalmente benefica: design che producono strong forward transfer possono simultaneamente indurre severe forgetting [[wiki/sources/hu-2026-continual-learning-memory]](raw/papers/arxiv-2604.27003.pdf).
