---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, agents, theory, critique, CLS, generalization]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Xu, Dai & Zhang (2026)** — CUHK / Zhejiang University

## Summary

Questo paper argomenta che i sistemi di memoria agente attuali (vector store, RAG, scratchpad, context-window management) implementano **lookup**, non vera memoria. Gli autori definiscono questa confusione una *category error* con conseguenze provabili:

- **Generalizzazione**: il retrieval generalizza per similarità a casi memorizzati; la memoria basata su pesi generalizza applicando regole astratte a input mai visti. Conflare i due produce agenti che accumulano note senza sviluppare expertise.
- **Soffitto di generalizzazione compositiva**: nessun aumento della dimensione del context o qualità del retrieval può superare questo limite su task composizionalmente nuovi.
- **Vulnerabilità al poisoning**: contenuto iniettato si propaga in tutte le sessioni future.

Gli autori richiamano la teoria dei **Complementary Learning Systems (CLS)** dalle neuroscienze: l'intelligenza biologica risolve il problema accoppiando storage esemplare ippocampale (veloce) con consolidamento neocorticale (lento). Gli agenti AI attuali implementano solo la prima metà.

## Taxonomy proposta

Il paper introduce una tassonomia a 4 tipi: Working (context window), Episodic (external store), Semantic, ed **Experiential** (model weights da esperienza vissuta). L'ultima riga è il gap identificato.

## Claim chiave

- I sistemi agenti attuali occupano solo la riga "Episodic" della tassonomia [[wiki/sources/arxiv-2604.27707]]
- Il retrieval non è un sostituto sufficiente per l'apprendimento [[wiki/sources/arxiv-2604.27707]]
- La vulnerabilità al memory poisoning è strutturale, non incidentale [[wiki/sources/arxiv-2604.27707]]
