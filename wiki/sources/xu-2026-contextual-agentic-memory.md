---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-theory, category-error, cls-theory, weight-consolidation, memory-poisoning]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Binyan Xu, Xilin Dai, Kehuan Zhang** (CUHK, Zhejiang Univ) — arXiv:2604.27707, Apr 2026

## Summary

Questo paper argomenta che i sistemi memoria agente attuali (vector store, RAG, scratchpad, context-window management) **non implementano memoria**: implementano **lookup**. Trattare lookup come memoria è un **category error** con conseguenze provabili per capability, learning e sicurezza.

Tesi centrale basata su Complementary Learning Systems (CLS) dalla neuroscience:
- L'intelligenza biologica risolve il problema accoppiando **fast hippocampal exemplar storage** con **slow neocortical weight consolidation**
- Gli agenti AI attuali implementano solo la prima metà

Consequenze identificate:
1. Gli agenti accumulano note indefinitamente senza sviluppare expertise
2. Esiste un **generalization ceiling provabile** su task compositionally novel che nessun aumento di context o retrieval quality può superare
3. Vulnerabilità strutturale a **persistent memory poisoning**: injected content propaga attraverso tutte le future sessioni

Il paper formalizza queste limitazioni, affronta 4 view alternative, e propone una co-existence proposal.

## Key claims
- Retrieval generalizza per similarità; weight-based memory generalizza per regole astratte ([§Abstract](raw/papers/arxiv-2604.27707.pdf))
- Il ceiling di generalizzazione è provabile, non empirico ([§3](raw/papers/arxiv-2604.27707.pdf))
- La memoria corrente converte transient prompt injection in persistent compromise ([§Abstract](raw/papers/arxiv-2604.27707.pdf))

## Connections
- [[wiki/sources/xu-2026-contextual-agentic-memory]] — fonte primaria
- [[wiki/pages/memory-theory]] — fondamenti teorici della memoria agente
