---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [semantic-memory, information-theory, retrieval, typed-memory]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Autori:** Abtahi et al. (Moorcheh AI, EdgeAI Innovations) | **arXiv:** 2604.22085 | **Apr 2026**

## Summary

Memanto è un memory layer universale per agentic AI che sfida l'assunto che la complessità dei knowledge graph sia necessaria per alta fedeltà della memoria agentica. Integra:

1. **Schema memoria semantica tipizzata**: 13 categorie di memoria predefinite
2. **Meccanismo di risoluzione conflitti automatico**
3. **Versioning temporale**

Tutto abilitato da Moorcheh's Information Theoretic Search engine, un database semantico no-indexing con retrieval deterministico sotto i 90ms e zero ingestion delay.

## Key claims

- LongMemEval: 89.8% accuracy, LoCoMo: 87.1% accuracy, superando tutti i sistemi graph+vector valutati [[wiki/pages/memanto]]
- Singola query retrieval, zero costo di ingestione, complessità operazionale sostanzialmente inferiore
- Ablation study a 5 stadi quantifica il contributo di ogni componente architettonica
