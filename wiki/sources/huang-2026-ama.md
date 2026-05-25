---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [multi-agent-memory, adaptive-retrieval, hierarchical-memory, memory-consistency]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Autori:** Weiquan Huang et al. (HKUST-Guangzhou, Shandong NTU, SUSTech) | **arXiv:** 2601.20352 | **Gennaio 2026**

## Sintesi

AMA (Adaptive Memory via multi-Agent collaboration) usa agent coordinati per gestire memoria a multiple granularita, superando le limitazioni di retrieval rigido e aggiornamenti grossolani dei sistemi esistenti.

## Architettura multi-agent

- **Constructor + Retriever:** costruzione e adaptive query routing a multi-granularita
- **Judge:** verifica rilevanza e consistenza del contenuto recuperato; triggera iterative retrieval se insufficiente
- **Refresher:** aggiorna o rimuove entry outdated quando il Judge rileva conflitti logici

## Design chiave

- **Hierarchical memory:** allinea dinamicamente la granularita di retrieval con la complessita del task
- Mantiene consistenza logica nel tempo evitando accumulo di inconsistenze

## Risultati

- Supera SOTA baselines su benchmark long-context
- Riduzione token consumption ~**80%** vs metodi full-context
- Mantenimento di retrieval precision e consistenza long-term

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — approccio multi-agent alla gestione memoria adattiva
