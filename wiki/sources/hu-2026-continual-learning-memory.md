---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [continual-learning, experience-reuse, memory-representation, transfer-learning]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Qisheng Hu, Quanyu Long, Wenya Wang** (NTU Singapore) — arXiv:2604.27003, Apr 2026

## Summary

Questo paper mostra che la memoria esterna **non elimina** il problema del continual learning ma lo **riloca**: dallo spazio dei parametri allo spazio della memoria. Introduce un framework (k, v) che disentangle due assi di design fondamentali:
- **k (representation)**: come l'esperienza è rappresentata (traiettorie dettagliate vs procedure astratte)
- **v (organization)**: come è organizzata per il retrieval

Esperimenti su task sequenziali in ALFWorld e BabyAI rivelano che:
- Le memorie procedurali astratte trasferiscono più affidabilmente delle traiettorie dettagliate
- Il negative transfer danneggia sproporzionatamente i casi difficili
- L'organizzazione fine-grained non è universalmente benefica: design con forte forward transfer possono simultaneamente indurre severe forgetting

La conclusione: la memoria esterna reshapes il continual learning in un problema di representation e retrieval design.

## Key claims
- La competizione tra vecchia e nuova esperienza nel contesto window è il nuovo bottleneck ([§Abstract](raw/papers/arxiv-2604.27003.pdf))
- Le memorie procedurali astratte > traiettorie dettagliate per transfer ([§3](raw/papers/arxiv-2604.27003.pdf))
- Fine-grained organization può peggiorare forgetting ([§3](raw/papers/arxiv-2604.27003.pdf))

## Connections
- [[wiki/sources/hu-2026-continual-learning-memory]] — fonte primaria
- [[wiki/pages/continual-learning]] — apprendimento continuo in agenti con memoria
