---
type: source
created: 2026-06-11
updated: 2026-06-11
tags: [memory, agents, llm, small-language-models, efficiency]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

Zhang, Zhang, Chen, Huang, Zheng, Wang, Guo, Mo, Bae, Zou, Wei, Yang (UESTC, Kyung Hee, CityU Oxford), April 2026.

LightMem è un sistema di memoria lightweight per agenti LLM guidato da Small Language Models (SLM). Modula retrieval, scrittura e consolidamento a lungo termine, separando processing online da consolidamento offline. Organizza la memoria in tre livelli: STM (short-term per contesto conversazionale immediato), MTM (mid-term per riassunti di interazioni riutilizzabili), LTM (long-term per conoscenza consolidata). Online: opera sotto un budget fisso di retrieval con procedura a due stadi (vector-based coarse retrieval + semantic consistency re-ranking) gestito da SLM specializzati (Controller per intent/query planning, Selector per candidate verification, Writer per incremental memory writing). Offline: astrazione e consolidamento gestiti da large-context model. Risultati: F1 medio +2.5 su A-MEM in LoCoMo, latenza mediana 83ms retrieval / 581ms end-to-end. Supporta multi-user tramite user identifiers per retrieval indipendente e manutenzione incrementale.
