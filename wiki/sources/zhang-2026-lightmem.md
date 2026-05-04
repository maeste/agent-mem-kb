---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, lightweight, small-language-models, efficient]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Autori:** Jiaquan Zhang et al. (UESTC, Kyung Hee U., CityU HK, Oxford)
**Data:** 2026-04-22

## Summary

LightMem usa Small Language Models per operazioni di memoria (retrieval, writing, consolidation) separando processing online da consolidamento offline. Organizza memoria in STM (contesto conversazionale), MTM (riepiloghi interazione riutilizzabili) e LTM (conoscenza consolidata). Supporta identificatori utente per retrieval indipendente in setting multi-utente.

Online: budget di retrieval fisso, recupero in due stadi (vector coarse + semantic consistency re-ranking). Offline: astrazione di evidenze di interazione e integrazione incrementale nella LTM. +2.5 F1 medio su LoCoMo vs. A-MEM, latenza 83ms retrieval, 581ms end-to-end.

[[wiki/pages/memory-architectures-retrieval]]
