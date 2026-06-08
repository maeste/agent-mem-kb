---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [multi-agent-memory, adaptive-retrieval, memory-consistency, hierarchical-memory]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Weiquan Huang et al.** (HKUST-Guangzhou) — arXiv:2601.20352, Apr 2026

## Summary

AMA (Adaptive Memory via Multi-Agent Collaboration) è un framework che usa agenti coordinati per gestire memoria a multiple granularità. Il problema chiave affrontato: gli approcci esistenti usano granularità di retrieval rigida, creando mismatch tra informazioni memorizzate e esigenze di reasoning task-specific.

Architettura gerarchica con ruoli specializzati:
- **Constructor** e **Retriever**: costruzione e routing multi-granularità adattivo
- **Judge**: verifica rilevanza e consistenza del contenuto recuperato, triggera re-iterazione se insufficiente
- **Refresher**: enforce consistenza tramite update target o rimozione entry outdated

Risultati su benchmark long-context: supera significativamente SOTA con ~80% riduzione token consumption vs metodi full-context. La granularità di retrieval si allina dinamicamente con la complessità del task.

## Key claims
- La granularità statica della memoria crea mismatch informativo ([§Abstract](raw/papers/arxiv-2601.20352.pdf))
- Multi-agent collaboration permette gestione memoria più sofisticata ([§3](raw/papers/arxiv-2601.20352.pdf))
- Il Judge component è critico per detectare conflitti logici ([§4](raw/papers/arxiv-2601.20352.pdf))

## Connections
- [[wiki/sources/huang-2026-ama]] — fonte primaria
- [[wiki/pages/multi-agent-memory]] — pattern multi-agent per memoria
