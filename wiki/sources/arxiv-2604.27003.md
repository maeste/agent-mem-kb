---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [continual-learning, memory-reuse, experience-transfer, stability-plasticity]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Autori:** Hu, Long, Wang (NTU Singapore) | **arXiv:** 2604.27003 | **Apr 2026**

## Summary

Mostra che la memoria esterna negli agenti LLM non elimina il problema del continual learning ma lo **riloca**: da interference nello spazio dei parametri a competition durante il retrieval sotto finestra di contesto limitata. Introduce un framework (k, v) che disentangle due assi di design:

- **k (representation)**: come l'esperienza è rappresentata (traiettorie dettagliate vs memorie procedurali astratte)
- **v (organization)**: come è organizzata per il retrieval

## Key claims

- Le memorie procedurali astratte transferiscono più affidabilmente delle traiettorie dettagliate [[wiki/pages/continual-learning-memory]]
- Il negative transfer danneggia sproporzionatamente i casi difficili
- Organizzazione memory fine-grained non è universalmente benefica: design con forte forward transfer possono simultaneamente indurre severe forgetting
