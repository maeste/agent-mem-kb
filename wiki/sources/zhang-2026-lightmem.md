---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [lightweight-memory, small-language-models, multi-tier-memory, retrieval-efficiency]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Autori:** Jiaquan Zhang et al. (UESTC, Kyung Hee, CityU HK, Oxford) | **arXiv:** 2604.07798 | **Aprile 2026**

## Sintesi

LightMem propone un sistema di memoria leggero per agent LLM basato su **Small Language Models (SLMs)** per ridurre la latenza online mantenendo accuratezza elevata. Modularizza retrieval, scrittura e consolidamento a lungo termine, separando processing online da consolidamento offline.

## Architettura a tre livelli

- **STM (Short-Term Memory):** contesto conversazionale immediato
- **MTM (Mid-Term Memory):** sommari di interazione riutilizzabili
- **LTM (Long-Term Memory):** conoscenza consolidata
- Supporto multi-user tramite identificatori utente per retrieval indipendente

## Retrieval

- Budget fisso di retrieval con procedura a due stadi:
  1. Coarse retrieval vettoriale
  2. Re-ranking per consistenza semantica

## Risultati

- F1 medio +2.5 su A-MEM su LoCoMo
- Latenza mediana: **83ms** retrieval, **581ms** end-to-end
- Guadagni consistenti across scale di modello

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — approccio SLM-based per efficienza operativa
