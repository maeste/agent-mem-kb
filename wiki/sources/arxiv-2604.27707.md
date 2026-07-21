---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [agentic-memory, critique, retrieval-vs-memory, generalization-ceiling]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Autori:** Xu, Dai, Zhang (CUHK, Zhejiang Univ) | **arXiv:** 2604.27707 | **Apr 2026**

## Summary

Posizione critica forte: i sistemi di memoria agente attuali (vector store, RAG, scratchpad, context-window management) **non implementano memoria, implementano lookup**. L'autore argomenta che trattare lookup come memoria è un **category error** con conseguenze provabili:

1. **Nessuna expertise development**: gli agenti accumulano note indefinitamente senza sviluppare competenza
2. **Generalization ceiling provabile** su task composizionalmente novelli che nessun aumento di contesto o qualità retrieval può superare
3. **Vulnerabilità strutturale** a memory poisoning persistente

Si basa su Complementary Learning Systems theory dalla neuroscienza: l'intelligenza biologica risolve il problema accoppiando fast hippocampal exemplar storage con slow neocortical weight consolidation. Gli agenti attuali implementano solo la prima metà.

## Key claims

- Retrieval generalizza per similarità a casi memorizzati; memoria weight-based generalizza applicando regole astratte a input mai visti [[wiki/pages/contextual-agentic-memory]]
- La conflazione dei due produce agenti con ceiling insormontabile
- Proposal di co-esistenza tra retrieval (veloce, reversibile) e consolidamento parametrico (lento, generalizzante)
