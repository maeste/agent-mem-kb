---
type: source
created: 2026-06-11
updated: 2026-06-11
tags: [memory, multi-agent, multimodal, llm-agents]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

Wang, Chen (MIRIX AI), July 2025.

MIRIX è un sistema di memoria modulare multi-agent che affronta il problema della memoria persistente in agenti LLM. Introduce sei tipi di memoria distinti: Core, Episodic, Semantic, Procedural, Resource Memory e Knowledge Vault, coordinati da un framework multi-agent per aggiornamenti e reperimento dinamici. A differenza degli approcci precedenti basati su testo piatto, MIRIX supporta esperienze visive e multimodali. Valutato su ScreenshotVQA (~20k screenshot ad alta risoluzione per sequenza): +35% accuracy rispetto a RAG baseline con -99.9% requisiti storage. Su LOCOMO (benchmark conversazioni long-form): 85.4% SOTA, superando ampiamente le baseline esistenti. Include un'applicazione packaged che monitora lo schermo in tempo reale, costruisce una memoria personalizzata e offre visualizzazione con storage locale sicuro.
