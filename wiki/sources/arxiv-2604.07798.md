---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [lightweight-memory, small-language-models, multi-tier-memory, efficiency, locomo]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight Agent Memory with Small Language Models

**Zhang, Zhang, Chen, Huang, Zheng, Wang, Guo, Mo, Bae, Zou, Wei, Yang** (UESTC, Kyung Hee U, CityU HK, Oxford) — arXiv:2604.07798, Apr 2026

## Summary

LightMem è un sistema di memoria lightweight per agent LLM che usa **Small Language Models (SLMs)** per le operazioni di memory ad alta frequenza, separando online processing da offline consolidation.

## Claim principali

- **Trade-off esistente**: retrieval-based external memory = basso overhead online ma accuracy instabile; LLM-based operations = alta accuracy ma latenza cumulativa su interazioni lunghe [[raw/papers/arxiv-2604.07798.pdf]].
- **Separazione online/offline**: mantenere lightweight le decisioni di memoria ad alta frequenza, deferire heavy abstraction e consolidation a offline processing. SLMs rendono questa separazione pratica [[raw/papers/arxiv-2604.07798.pdf]].
- **Architettura a 3 tier**: (1) **STM** (Short-Term Memory): contesto conversazionale immediato; (2) **MTM** (Mid-Term Memory): riassunti di interazione riutilizzabili; (3) **LTM** (Long-Term Memory): conoscenza consolidata [[raw/papers/arxiv-2604.07798.pdf]].
- **Pipeline modulare con SLMs**: (1) Controller (SLM-1): intent routing e query planning; (2) Selector (SLM-2): candidate verification e compression; (3) Writer (SLM-3): incremental memory writing [[raw/papers/arxiv-2604.07798.pdf]].
- **Two-stage retrieval**: vector-based coarse retrieval → semantic consistency re-ranking sotto fixed budget [[raw/papers/arxiv-2604.07798.pdf]].
- **Multi-user support**: user identifiers per independent retrieval e incremental maintenance con isolamento logico per-user [[raw/papers/arxiv-2604.07798.pdf]].
- **Risultati**: +2.5 F1 medio vs A-MEM su LoCoMo, latency mediana 83ms per retrieval, 581ms end-to-end. Gains consistenti across model scales [[raw/papers/arxiv-2604.07798.pdf]].

## Posizione nel dibattito

Approccio pragmatico all'efficienza della memoria agentic. Rilevante per deployment production dove contano latenza e costi. La separazione SLM/LLM e online/offline è un pattern architetturale riutilizzabile.
