---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [multi-agent-memory, multimodal-memory, memory-system, benchmark]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM Agents

**Autori:** Wang, Chen (MIRIX AI, UCSD, NYU) | **arXiv:** 2507.07957 | **Lug 2025**

## Summary

MIRIX è un sistema di memoria modulare multi-agent che supera le soluzioni esistenti basate su memoria flat e narrow-scope. Si distingue per supportare esperienze visive e multimodali oltre al testo. Comprende sei tipi di memoria distinti:

1. **Core Memory**: identità e preferenze base dell'utente
2. **Episodic Memory**: eventi specifici nel tempo
3. **Semantic Memory**: conoscenza generalizzata e fatti
4. **Procedural Memory**: skill e procedure
5. **Resource Memory**: riferimenti a risorse esterne
6. **Knowledge Vault**: knowledge base strutturata

Un framework multi-agent coordina dinamicamente aggiornamenti e retrieval.

## Key claims

- Su ScreenshotVQA (~20K screenshot ad alta risoluzione per sequenza), MIRIX raggiunge +35% accuracy vs RAG baseline con -99.9% requisiti di storage [[wiki/pages/mirix]]
- Su LOCOmo (conversazioni lunghe single-modal), 85.4% accuracy, SOTA rispetto a baselines esistenti
- L'architettura multi-agent per il controllo della memoria scala meglio di approcci monolitici
