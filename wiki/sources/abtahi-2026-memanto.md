---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [typed-memory, semantic-memory, information-theoretic-retrieval, no-indexing]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Seyed Moein Abtahi et al.** (Moorcheh AI, EdgeAI Innovations), arXiv:2604.22085, Apr 2026.

## Summary

Memanto è un **universal memory layer** per agentic AI che sfida l'assunto che la complessità dei knowledge graph sia necessaria per alta fedeltà della memoria. Integra uno schema di memoria semantica tipizzata con 13 categorie predefinite, un meccanismo automatico di risoluzione conflitti, e versioning temporale. Usa **Moorcheh's Information Theoretic Search engine**, un database semantico no-indexing con retrieval deterministico sotto i 90ms.

## Key Claims

- Su LongMemEval e LoCoMo, Memanto raggiunge **89.8%** e **87.1%** rispettivamente, superando tutti i sistemi ibridi graph e vector-based valutati [[wiki/sources/abtahi-2026-memanto]](raw/papers/arxiv-2604.22085.pdf).
- Richiede solo una singola chiamata LLM (vs multiple chiamate per sistemi graph-based) [[wiki/sources/abtahi-2026-memanto]](raw/papers/arxiv-2604.22085.pdf).
- Elimina il ritardo di ingestione grazie all'approccio no-indexing [[wiki/sources/abtahi-2026-memanto]](raw/papers/arxiv-2604.22085.pdf).
