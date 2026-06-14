---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [lightweight-memory, small-language-models, memory-retrieval, efficiency]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Jiaquan Zhang et al.** (UESTC et al.), arXiv:2604.07798, Apr 2026.

## Summary

LightMem è un sistema di memoria **lightweight** per agenti LLM che usa **Small Language Models (SLMs)** per guidare le operazioni di memoria. Modularizza retrieval, writing e long-term consolidation, separando processing online da consolidation offline. Organizza memoria in STM (contesto conversazionale immediato), MTM (riassunti interazioni riutilizzabili), e LTM (conoscenza consolidata).

## Key Claims

- Miglioramento medio **F1 di ~2.5** su A-MEM su LoCoMo, con latenza mediana di **83ms per retrieval** e **581ms end-to-end** [[wiki/sources/zhang-2026-lightmem]](raw/papers/arxiv-2604.07798.pdf).
- I sistemi retrieval-based soffrono instabilità dovuta a limitata query construction e candidate filtering; i sistemi LLM-driven accumulano latenza su interazioni lunghe [[wiki/sources/zhang-2026-lightmem]](raw/papers/arxiv-2604.07798.pdf).
- La separazione online/offline abilita efficiente invocazione memoria sotto compute limitato [[wiki/sources/zhang-2026-lightmem]](raw/papers/arxiv-2604.07798.pdf).
