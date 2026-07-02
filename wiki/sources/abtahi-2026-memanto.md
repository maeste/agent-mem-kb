---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [semantic-memory, typed-memory, information-theoretic-retrieval, no-indexing, long-horizon-agents]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Autori:** Seyed Moein Abtahi, Rasa Rahnema, Hetkumar Patel, Neel Patel, Majid Fekri, Tara Khani (Moorcheh AI, EdgeAI Innovations)  
**Data:** Aprile 2026 | arxiv:2604.22085

## Sintesi

Memanto e' un memory layer universale per agentica AI che sfida l'assunto prevalente che la complessita' dei knowledge graph sia necessaria per memoria agentica ad alta fedelta'.

### Architettura

1. **Typed semantic memory schema:** 13 categorie di memoria predefinite (factual, episodic, procedural, etc.)
2. **Automated conflict resolution:** meccanismo per gestire contraddizioni tra memorie
3. **Temporal versioning:** versionamento temporale delle memorie
4. **Information Theoretic Search engine (Moorcheh):** database semantico **no-indexing** basato su Information Theoretic Vector Compression
   - Retrieval deterministico in <90ms
   - Zero ingestion delay (nessun costo di indicizzazione)
   - Single query retrieval (niente multi-query pipelines)

### Risultati

- **LongMemEval: 89.8% accuracy** (SOTA)
- **LoCoMo: 87.1% accuracy** (SOTA)
- Supera tutti i sistemi ibridi graph e vector valutati
- Richiede una singola query di retrieval, zero costo di ingestione, complessita' operazionale sostanzialmente inferiore
- Ablation study a 5 stadi che quantifica il contributo di ogni componente

## Claim chiave

- L'information-theoretic vector compression puo' sostituire architetture ibride graph+vector con minore complessita' [[wiki/pages/memory-fundamentals]]
- Il typing semantico delle memorie + conflict resolution supera la gestione esplicita dello schema dei knowledge graph
- L'assenza di indexing elimina il collo di bottiglia dell'ingestione nei sistemi di memoria production-grade

## Posizione nel vault

Sistema memory completo con risultati SOTA. Rappresenta l'approccio "semantic typed" alla memoria agentica, alternativo sia ai grafi puri che al vector store puro.
