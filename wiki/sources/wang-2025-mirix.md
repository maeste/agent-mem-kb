---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, multi-agent, multimodal, benchmark]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Autori:** Yu Wang, Xi Chen (MIRIX AI)
**Data:** 2025-07-10

## Summary

MIRIX propone un sistema di memoria modulare multi-agente con sei componenti distinte: Core, Episodica, Semantica, Procedurale, Resource Memory e Knowledge Vault. Un Meta Memory Manager instrada le operazioni ai sei Memory Manager specializzati. Il sistema supporta input multimodali (testo, immagini, schermate) e gestisce dati utente a scala.

Raggiunge SOTA su LOCOMO (85.4%) e su ScreenshotVQA (+35% accuracy vs. RAG baseline) con riduzione dello storage del 99.9%. La validazione su benchmark multimodali dimostra che l'architettura multi-tipo supera significativamente le memorie flat come Letta e Mem0.

[[wiki/pages/llm-agent-memory]] [[wiki/pages/memory-architectures-retrieval]]
