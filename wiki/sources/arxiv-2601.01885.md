---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, unified-memory, reinforcement-learning, ltm, stm]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory (AgeMem): Learning Unified LTM and STM Management

**Autori:** Yi Yu, Liuyi Yao, Yuexiang Xie et al. (Wuhan University, Alibaba)
**arXiv:** 2601.01885 | Aprile 2026

## Riassunto

AgeMem propone un framework unificato che integra gestione long-term memory (LTM) e short-term memory (STM) direttamente nella policy dell'agente, superando l'approccio tradizionale di trattarle come componenti separate con euristiche o controller ausiliari.

Il sistema espone le operazioni di memoria come azioni tool-based: l'agente LLM decide autonomamente cosa e quando memorizzare, recuperare, aggiornare, riassumere o scartare informazioni. Per trainare questi comportamenti unificati, introduce una strategia reinforcement learning a tre stadi progressivi e uno step-wise GRPO per address sparse rewards indotte dalle operazioni di memoria.

Sperimentato su cinque benchmark long-horizon, AgeMem supera consistentemente i baselines memory-augmented su backbone LLM multipli, con miglior task performance, memoria LTM di qualità superiore e uso del contesto più efficiente.

## Claim chiave

- Unificare LTM e STM nella policy dell'agente supera approcci a componenti separate [[wiki/sources/arxiv-2601.01885.md]]
- Le operazioni memory come tool actions abilitano ottimizzazione end-to-end via RL [[wiki/sources/arxiv-2601.01885.md]]
- Step-wise GRPO addressa il problema delle rewards sparse e discontinue nelle operazioni di memoria [[wiki/sources/arxiv-2601.01885.md]]

## Collegamenti

- Alternativa unificata a [[wiki/sources/huang-2026-ama.md]] (AMA) che usa multi-agent collaboration
- Approccio complementare a [[wiki/sources/zhang-2026-lightmem.md]] (LightMem) che usa SLM per memory ops
- Relazionato a [[wiki/pages/memory-systems]]
