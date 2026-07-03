---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, multi-agent, multimodal, multi-agent-memory]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Autori:** Yu Wang, Xi Chen (MIRIX AI / UCSD / NYU)
**arXiv:** 2507.07957 | Luglio 2025

## Riassunto

MIRIX è un sistema di memoria modulare multi-agent che supera le limitazioni delle soluzioni memory flat esistenti. Si distingue per supportare esperienze multimodali (non solo testo) e per un'architettura a sei tipi di memoria distinti: Core, Episodic, Semantic, Procedural, Resource Memory e Knowledge Vault. Un framework multi-agent coordina dinamicamente aggiornamenti e retrieval.

Validato su due benchmark:
- **ScreenshotVQA**: ~20.000 screenshot ad alta risoluzione per sequenza, +35% accuratezza vs RAG baseline, -99.9% requisiti storage
- **LOCOMO**: benchmark conversazioni long-form single-modal, 85.4% SOTA (superamento significativo dei baselines)

Fornisce anche un'applicazione packagata che monitora lo schermo in tempo reale e costruisce memo personalizzati.

## Claim chiave

- La memoria multi-modale (visual + textual) supera significativamente i baseline text-only RAG [[wiki/sources/arxiv-2507.07957.md]]
- Una architettura a sei tipi di memoria con coordinamento multi-agent scala meglio di approcci flat [[wiki/sources/arxiv-2507.07957.md]]
- La compressione della memoria visuale (-99.9% storage) preserva l'accuratezza su task di comprensione contestuale [[wiki/sources/arxiv-2507.07957.md]]

## Collegamenti

- Confronta con [[wiki/sources/wang-2025-mirix.md]] (stesso lavoro, entry esistente)
- Approccio alternativo a [[wiki/sources/yu-2026-agemem.md]] (AgeMem, unified LTM/STM)
- Relazionato a [[wiki/pages/memory-systems]]
