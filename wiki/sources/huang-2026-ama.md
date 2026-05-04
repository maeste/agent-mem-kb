---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, multi-agent, consistency, hierarchical]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Autori:** Weiquan Huang et al. (HKUST(GZ), Shandong University, NTU)
**Data:** 2026-04-15 (v3)

## Summary

AMA usa agenti coordinati (Constructor, Retriever, Judge, Refresher) per gestire memoria multi-granularità. Il Constructor e Retriever abilitano costruzione e routing adattivo; il Judge verifica rilevanza e consistenza, triggerando retrieval iterativo o refresh; il Refresher esegue aggiornamenti mirati e rimozione di entry obsolete.

Supera SOTA su benchmark long-context con ~80% riduzione consumo token vs. full-context. Il contributo chiave è il rilevamento automatico di contraddizioni logiche e il refresh selettivo, risolvendo il problema dell'accumulo incontrollato di incoerenze nella memoria.

[[wiki/pages/memory-architectures-retrieval]]
