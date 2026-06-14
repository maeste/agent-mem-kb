---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [multi-agent-memory, multimodal-memory, memory-system, long-term-memory]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Yu Wang, Xi Chen** (MIRIX AI), arXiv:2507.07957, Jul 2025.

## Summary

MIRIX è un sistema di memoria modulare multi-agent che ridefinisce l'architettura della memoria per agenti LLM, superando le limitazioni degli approcci flat e text-centric. Si compone di **sei tipi di memoria distinti**: Core Memory, Episodic Memory, Semantic Memory, Procedural Memory, Resource Memory, e Knowledge Vault, coordinati da un framework multi-agent con un Meta Memory Manager per il routing dei task.

## Key Claims

- Su **ScreenshotVQA** (~20K screenshot ad alta risoluzione per sequenza), MIRIX raggiunge **35% di accuratezza in più** rispetto al baseline RAG riducendo i requisiti di storage del **99.9%** [[wiki/sources/wang-2025-mirix]](raw/papers/arxiv-2507.07957.pdf).
- Su **LOCOmo** (benchmark conversazionali long-form), MIRIX raggiunge **85.4%**, superando ampiamente i baseline esistenti [[wiki/sources/wang-2025-mirix]](raw/papers/arxiv-2507.07957.pdf).
- La struttura a sei componenti abilita memorie multimodali (immagini, schermate) che i sistemi text-only non possono gestire [[wiki/sources/wang-2025-mirix]](raw/papers/arxiv-2507.07957.pdf).
