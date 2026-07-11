---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [semantic-memory, typed-memory, information-theoretic-retrieval, long-horizon-agents, benchmarking]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval

**Abtahi, Rahnema, Patel, Patel, Fekri, Khani** (Moorcheh AI, EdgeAI) — arXiv:2604.22085, Apr 2026

## Summary

Memanto è un layer di memoria universale per agent AI che sfida l'assunto che la complessità dei knowledge graph sia necessaria per alta fedeltà di memoria, usando invece semantic retrieval information-theoretic con schema di memoria tipizzata.

## Claim principali

- **Tesi**: i sistemi attuali dipendono da architetture hybrid semantic graph con overhead computazionale sostanziale (LLM-mediated entity extraction, explicit graph schema maintenance, multi-query retrieval pipelines). Questo non è necessario [[raw/papers/arxiv-2604.22085.pdf]].
- **Architettura**: (1) **13 predefined memory categories** (typed semantic memory schema); (2) **Automated conflict resolution mechanism**; (3) **Temporal versioning**; tutto abilitato da Moorcheh's Information Theoretic Search engine (no-indexing semantic database) [[raw/papers/arxiv-2604.22085.pdf]].
- **Information Theoretic Search**: deterministic retrieval in <90ms latency, zero ingestion delay, nessun indexing richiesto [[raw/papers/arxiv-2604.22085.pdf]].
- **Risultati**: SOTA su LongMemEval (89.8%) e LoCoMo (87.1%), superando tutti i sistemi hybrid graph e vector valutati con una singola query di retrieval, zero ingestion cost, complessità operazionale sostanzialmente inferiore [[raw/papers/arxiv-2604.22085.pdf]].
- **Ablation study a 5 stadi**: quantifica il contributo di ogni componente architetturale [[raw/papers/arxiv-2604.22085.pdf]].

## Posizione nel dibattito

Posizione pragmatica/ingegneristica: dimostra che retrieval semantico ottimizzato + typing strutturato può competere o superare architetture più complesse. Rilevante per deployment production dove latenza e complessità operazionale contano.
