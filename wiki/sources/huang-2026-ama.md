---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [multi-agent-memory, adaptive-memory, memory-consistency, multi-granularity]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Weiquan Huang et al.** (HKUST-Guangzhou), arXiv:2601.20352, Apr 2026.

## Summary

AMA (Adaptive Memory via Multi-Agent Collaboration) è un framework che usa agenti coordinati per gestire memoria su **multiple granularità**. Impiega una gerarchia di memoria che allinea dinamicamente la granularità di retrieval con la complessità del task. Il Constructor e Retriever abilitano costruzione e routing adattivo; il Judge verifica rilevanza e consistenza; il Refresher esegue aggiornamenti targetizzati o rimuove entry obsolete.

## Key Claims

- AMA supera significativamente gli SOTA baselines riducendo il **consumo di token di circa l'80%** rispetto a metodi full-context [[wiki/sources/huang-2026-ama]](raw/papers/arxiv-2601.20352.pdf).
- La granularità statica crea un mismatch persistente tra informazioni memorizzate e esigenze di ragionamento task-specific [[wiki/sources/huang-2026-ama]](raw/papers/arxiv-2601.20352.pdf).
- L'architettura multi-agent previene l'accumulo non controllato di inconsistenze logiche nel tempo [[wiki/sources/huang-2026-ama]](raw/papers/arxiv-2601.20352.pdf).
