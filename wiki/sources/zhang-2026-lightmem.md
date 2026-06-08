---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [lightweight-memory, small-language-models, memory-efficiency, multi-user]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Jiaquan Zhang et al.** (UESTC, Kyung Hee Univ, CityU HK, Oxford) — arXiv:2604.07798, Apr 2026

## Summary

LightMem è un sistema di memoria lightweight per agenti LLM che usa **Small Language Models (SLMs)** per le operazioni di memoria online, separando il processing online dalla consolidazione offline. Il problema affrontato: i sistemi retrieval-based hanno instabile accuracy; i sistemi LLM-driven accumulano latenza su interazioni lunghe.

Architettura a tre livelli:
- **STM** (Short-Term Memory): contesto conversazionale immediato
- **MTM** (Mid-Term Memory): riassunti interazioni riutilizzabili
- **LTM** (Long-Term Memory): conoscenza consolidata

Online opera sotto un **fixed retrieval budget** con procedura a due stadi: vector-based coarse retrieval + semantic consistency re-ranking. Offline astrae evidenze interazione riutilizzabili e le integra incrementalmente in LTM. Supporta multi-user tramite user identifiers per retrieval indipendente.

Risultati: +2.5 F1 medio vs A-MEM su LoCoMo, latenza mediana 83ms retrieval / 581ms end-to-end.

## Key claims
- Gli SLMs sono adeguati per operazioni di memoria online strutturate ([§Abstract](raw/papers/arxiv-2604.07798.pdf))
- La separazione online/offline abilita efficienza senza sacrificare qualità ([§3](raw/papers/arxiv-2604.07798.pdf))
- Il fixed retrieval budget controlla il costo computazionale ([§4](raw/papers/arxiv-2604.07798.pdf))

## Connections
- [[wiki/sources/zhang-2026-lightmem]] — fonte primaria
- [[wiki/pages/lightweight-memory]] — sistemi memoria efficienti
