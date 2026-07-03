---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, multi-agent, adaptive-retrieval, hierarchical-memory]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Autori:** Weiquan Huang, Zixuan Wang, Hehai Lin et al. (HKUST-Guangzhou, Shandong, NTU, SUSTech)
**arXiv:** 2601.20352 | Aprile 2026

## Riassunto

AMA (Adaptive Memory via Multi-Agent Collaboration) affronta le limitazioni dei sistemi memory esistenti: granularità di retrieval rigida, strategie di maintenance accumulation-heavy, e meccanismi di update coarse-grained. Usa agenti coordinati per gestire la memoria a multiple granularità.

Architettura con ruoli specializzati:
- **Constructor** e **Retriever**: abilitano costruzione e retrieval multi-granularità con routing adattivo
- **Judge**: verifica rilevanza e consistenza del contenuto recuperato, triggera iterative retrieval o invoca il Refresher
- **Refresher**: forza consistenza della memoria tramite update targetizzati o rimozione entry outdated

Su benchmark long-context, AMA supera significativamente lo SOTA riducendo il consumo di token di circa l'80% rispetto ai baselines.

## Claim chiave

- La collaborazione multi-agent con ruoli specializzati supera approcci memory single-system [[wiki/sources/arxiv-2601.20352.md]]
- Il routing adattivo della granularità di retrieval allinea la memoria alla complessità del task [[wiki/sources/arxiv-2601.20352.md]]
- Un Judge dedicato per consistenza/rilevanza previene accumulazione di inconsistencies [[wiki/sources/arxiv-2601.20352.md]]

## Collegamenti

- Confronta con [[wiki/sources/yu-2026-agemem.md]] (AgeMem): AMA usa multi-agent, AgeMem usa unified RL
- Relazionato a [[wiki/pages/memory-systems]]
- Approccio gerarchico complementare a [[wiki/sources/yang-2026-graph-memory.md]] (survey graph-based memory)
