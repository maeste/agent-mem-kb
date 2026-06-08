---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [unified-memory, reinforcement-learning, ltm-stm, agentic-memory]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory (AgeMem): Learning Unified LTM and STM Management

**Yi Yu et al.** (Wuhan University, Alibaba) — arXiv:2601.01885, Apr 2026

## Summary

AgeMem è un framework unificato che integra la gestione di memoria a lungo termine (LTM) e a breve termine (STM) direttamente nella policy dell'agente, esponendo le operazioni di memoria come azioni tool-based. A differenza dei metodi esistenti che trattano LTM e STM come componenti separate con euristiche o controller ausiliari, AgeMem permette all'LLM di decidere autonomamente cosa/quando memorizzare, recuperare, aggiornare, riassumere o scartare.

Per training di comportamenti unificati, propone una strategia **three-stage progressive RL** con **step-wise GRPO** per affrontare ricompense sparse e discontinue indotte dalle operazioni di memoria. Valutato su 5 benchmark long-horizon: supera consistentemente le baseline memory-augmented su multipli backbone LLM, con miglior task performance, memoria LTM di qualità superiore e uso del contesto più efficiente.

## Key claims
- LTM e STM dovrebbero essere gestite in modo unificato, non come moduli separati ([§Abstract](raw/papers/arxiv-2601.01885.pdf))
- Le operazioni di memoria possono essere imparate come azioni tool-based ([§3](raw/papers/arxiv-2601.01885.pdf))
- Step-wise GRPO affronta il problema delle ricompense sparse nelle operazioni memoria ([§4](raw/papers/arxiv-2601.01885.pdf))

## Connections
- [[wiki/sources/yu-2026-agemem]] — fonte primaria
- [[wiki/pages/unified-memory]] — gestione unificata LTM/STM
