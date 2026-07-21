---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [lightweight-memory, slm, memory-retrieval, efficiency]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight Memory System for LLM Agents

**Autori:** Zhang et al. | **arXiv:** 2604.07798 | **Apr 2026**

## Summary

LightMem è un sistema di memoria lightweight per agenti LLM basato su Small Language Models (SLM). Modularizza retrieval, scrittura e consolidamento long-term, separando processing online da consolidamento offline per enable memory invocation efficiente con compute limitato.

Organizza la memoria in tre livelli:
1. **STM**: contesto conversazionale immediato
2. **MTM**: summary di interazioni riutilizzabili
3. **LTM**: conoscenza consolidata

Online opera sotto budget fisso con retrieval a due stadi (vettoriale coarse + re-ranking semantico). Offline astrae evidenza interattiva e la integra incrementalmente in LTM.

## Key claims

- F1 medio +2.5 vs A-MEM su LoCoMo, con latenza mediana 83ms retrieval e 581ms end-to-end [[wiki/pages/lightmem]]
- Supporta multi-user con user identifiers per retrieval indipendente e manutenzione incrementale
- Gli SLM possono gestire operazioni memoria complesse con latenza prevedibile
