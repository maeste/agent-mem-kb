---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [multi-agent-memory, multimodal-memory, memory-system, mirix]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Yu Wang, Xi Chen** (MIRIX AI) — arXiv:2507.07957, Jul 2025

## Summary

MIRIX è un sistema di memoria modulare multi-agent che ridefinisce la memoria per agenti LLM, superando le limitazioni delle soluzioni flat e narrowly scoped esistenti. Si distingue per il supporto a esperienze visive e multimodali, rendendo la memoria genuinamente utile in scenari real-world.

L'architettura comprende **sei tipi di memoria** distinti, ciascuno gestito da un Memory Manager dedicato:
- **Core Memory**: preferenze e identità utente
- **Episodic Memory**: eventi ed esperienze specifiche dell'utente
- **Semantic Memory**: concetti ed entità nominate
- **Procedural Memory**: istruzioni step-by-step per task
- **Resource Memory**: documenti, file e media condivisi
- **Knowledge Vault**: informazioni critiche da preservare verbatim (indirizzi, credenziali)

Un Meta Memory Manager coordina il routing tra i sei manager. Valutato su ScreenshotVQA (~20K screenshot ad alta risoluzione): +35% accuracy vs RAG baseline con -99.9% storage. Su LOCoMo: 85.4% SOTA.

## Key claims
- Sei tipi di memoria specializzati superano le architetture flat ([§1](raw/papers/arxiv-2507.07957.pdf))
- Il supporto multimodale è critico per la memoria in scenari reali ([§Abstract](raw/papers/arxiv-2507.07957.pdf))
- L'architettura multi-agent gestisce efficacemente la complessità della memoria eterogenea ([§3](raw/papers/arxiv-2507.07957.pdf))

## Connections
- [[wiki/sources/wang-2025-mirix]] — fonte primaria
- [[wiki/pages/multi-agent-memory]] — pattern multi-agent per gestione memoria
