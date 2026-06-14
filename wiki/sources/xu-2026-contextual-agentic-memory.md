---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [memory-theory, lookup-vs-memory, generalization-ceiling, complementary-learning-systems]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Binyan Xu, Xilin Dai, Kehuan Zhang** (CUHK, Zhejiang University), arXiv:2604.27707, Apr 2026.

## Summary

Paper teorico che argomenta che i sistemi memoria agentici attuali (vector store, RAG, scratchpad, context-window management) **implementano lookup, non memoria**. La retrieval generalizza per similarità a casi memorizzati; la memoria basata su pesi generalizza applicando regole astratte a input mai visti. Conflare i due produce agenti che accumulano note indefinitamente senza sviluppare expertise. Si basa sulla teoria dei Complementary Learning Systems dalla neuroscienza.

## Key Claims

- Trattare lookup come memoria è un **category error** con conseguenze provabili per capability, learning a lungo termine e sicurezza [[wiki/sources/xu-2026-contextual-agentic-memory]](raw/papers/arxiv-2604.27707.pdf).
- Gli agenti built esclusivamente su retrieval affrontano un **generalization ceiling provabile** su task composizionalmente novel che nessun aumento di context window o qualità retrieval può superare [[wiki/sources/xu-2026-contextual-agentic-memory]](raw/papers/arxiv-2604.27707.pdf).
- Gli agenti attuali implementano solo "metà" del sistema biologico: fast hippocampal exemplar storage (retrieval), ma mancano slow neocortical weight consolidation [[wiki/sources/xu-2026-contextual-agentic-memory]](raw/papers/arxiv-2604.27707.pdf).
- I sistemi di retrieval sono strutturalmente vulnerabili al **persistent memory poisoning** in cui contenuto iniettato propaga attraverso tutte le sessioni future [[wiki/sources/xu-2026-contextual-agentic-memory]](raw/papers/arxiv-2604.27707.pdf).
