---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [lightweight-memory, small-language-models, multi-tier-memory, retrieval-efficiency, locomo]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Autori:** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng, Zhicheng Wang, Ping Guo, Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, Yang Yang (UESTC, Kyung Hee, CityU Oxford)  
**Data:** Aprile 2026 | arXiv:2604.07798

## Sintesi

LightMem propone un sistema di memoria **lightweight** per agent LLM che usa Small Language Models (SLM) per le operazioni di memory ad alta frequenza, separando il processing online dalla consolidazione offline.

### Il problema

I sistemi di memoria per agent cadono in due categorie con trade-off:
- **Retrieval-based external memory:** basso overhead online ma accuracy instabile (query construction limitata, candidate filtering debole)
- **LLM-driven memory operations:** maggiore accuracy ma latenza accumulata su interazioni lunghe (ripetuti model invocations)

### Architettura three-tier

1. **STM (Short-Term Memory):** contesto conversazionale immediato
2. **MTM (Mid-Term Memory):** sommari di interazione riutilizzabili
3. **LTM (Long-Term Memory):** conoscenza consolidata

### Online vs Offline separation

- **Online (SLM-driven):**
  - Oper sotto un **fixed retrieval budget**
  - Two-stage procedure: vector-based coarse retrieval + semantic consistency re-ranking
  - User identifiers per supportare multi-user independent retrieval
- **Offline:** astrae evidenza di interazione riutilizzabile e incrementalmente la integra in LTM

### Risultati

- Average F1 improvement di ~2.5 punti su A-MEM su LoCoMo
- Higher efficiency e low median latency
- **83 ms** per retrieval
- **581 ms** end-to-end
- Gains consistenti across model scales

## Claim chiave

- La separazione online/offline con SLM per decisioni ad alta frequenza risolve l'efficiency-effectiveness trade-off [[wiki/pages/memory-fundamentals]]
- Il two-stage retrieval (coarse vector + semantic re-rank) bilancia velocita' e precisione
- I SLM sono adeguati per task strutturati di memory management (intent routing, query construction, semantic filtering)

## Posizione nelvault

Sistema memory pragmatico orientato alla deployabilità. Rappresenta l'approccio "tiered" ottimizzato per latenza, complementare a sistemi più teorici come Memanto o ActMem.
