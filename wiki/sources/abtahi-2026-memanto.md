---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [semantic-memory, information-theoretic-retrieval, typed-memory, memory-engine]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Seyed Moein Abtahi et al.** (Moorcheh AI) — arXiv:2604.22085, Apr 2026

## Summary

Memanto è un **universal memory layer** per agentic AI che sfida l'assunto prevalente che la complessità dei knowledge graph sia necessaria per memoria agente high-fidelity. Integra:

1. **Schema di memoria semantica tipizzata**: 13 categorie di memoria predefinite
2. **Meccanismo automatico di conflict resolution**
3. **Temporal versioning** delle entry

Tutto abilitato da **Moorcheh's Information Theoretic Search engine**, un database semantico no-indexing con retrieval deterministico in <90ms latenza e zero ingestion delay.

Risultati su LongMemEval (89.8%) e LoCoMo (87.1%): supera tutti i sistemi hybrid-graph e vector-based valutati con una singola query retrieval, nessun costo di ingestione, complessità operazionale sostanzialmente inferiore. Ablation study a 5 stadi quantifica il contributo di ogni componente architetturale.

## Key claims
- La complessità dei grafi non è necessaria per memoria agente efficace ([§Abstract](raw/papers/arxiv-2604.22085.pdf))
- L'information theoretic search abilita retrieval sub-90ms senza indexing ([§3](raw/papers/arxiv-2604.22085.pdf))
- Le 13 categorie tipizzate + conflict resolution sostituiscono schema management esplicito ([§Abstract](raw/papers/arxiv-2604.22085.pdf))

## Connections
- [[wiki/sources/abtahi-2026-memanto]] — fonte primaria
- [[wiki/pages/semantic-memory]] — memoria semantica strutturata
