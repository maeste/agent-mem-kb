---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, agents, semantic-memory, information-theory, retrieval]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Abtahi et al. (2026)** — Moorcheh AI / EdgeAI Innovations

## Summary

Memanto è un **universal memory layer per agentic AI** che sfida l'assunto che la complessità dei knowledge graph sia necessaria per memoria agente ad alta fedeltà. Integra uno schema di memoria semantica tipizzata con 13 categorie predefinite, un meccanismo automatico di risoluzione conflitti, e versioning temporale.

Il motore sottostante è Moorcheh's **Information Theoretic Search**, un database semantico no-indexing che fornisce retrieval deterministico con latenza sub-90ms e nessun ritardo di ingestione.

## Risultati

- LongMemEval: **89.8%** accuracy (SOTA)
- LoCoMo: **87.1%** accuracy (SOTA)
- Supera tutti i sistemi ibridi graph+vector valutati con una singola query retrieval, zero costo di ingestione, complessità operazionale sostanzialmente inferiore

## Claim chiave

- La complessità dei knowledge graph non è necessaria per memoria agente ad alta fedeltà [[wiki/sources/arxiv-2604.22085]]
- Il retrieval informativo-teorico può eguagliare o superare architetture ibride con minore overhead [[wiki/sources/arxiv-2604.22085]]
