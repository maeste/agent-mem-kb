---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [typed-memory, semantic-retrieval, information-theory, long-horizon-agents, memanto]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Autori:** Seyed Moein Abtahi et al. (Moorcheh AI, EdgeAI Innovations) | **arXiv:** 2604.22085 | **Aprile 2026**

## Sintesi

Memanto sfida l'assunto che la complessita dei knowledge graph sia necessaria per memoria agent ad alta fedelta. Integra uno schema di memoria semantica tipizzata (13 categorie predefinite), un meccanismo automatico di risoluzione conflitti, e versioning temporale, tutto abilitato da un motore di ricerca **Information Theoretic Search** senza indicizzazione.

## Caratteristiche chiave

- **13 categorie di memoria** predefinite (typed semantic memory schema)
- **Information Theoretic Vector Compression:** retrieval deterministico con latenza sub-90ms
- **Nessun costo di ingestione** (no indexing), singola query di retrieval
- Risoluzione automatica conflitti + versioning temporale

## Risultati

- **89.8%** su LongMemEval, **87.1%** su LoCoMo — state-of-the-art
- Supera tutti i sistemi ibridi graph e vector valutati
- Complessita operazionale sostanzialmente inferiore
- Ablation study a 5 stadi che quantifica il contributo di ogni componente

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — evidenza che retrieval semantico ottimizzato puo superare architetture graph complesse
