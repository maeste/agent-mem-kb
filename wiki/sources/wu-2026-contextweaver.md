---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, context-management, dependency-graph, code-agent]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Selective and Dependency-Structured Memory Construction

**Autori:** Yating Wu et al. (UT Austin, AWS AI Labs)
**Data:** 2026-04-24

## Summary

ContextWeaver organizza la traccia di interazione dell'agente in un grafo di step di reasoning con dipendenze causali e logiche. Tre componenti: (1) costruzione basata su dipendenze che collega ogni step ai precedenti, (2) riepilogo compatto dei percorsi di ragionamento radice-step, (3) layer di validazione leggero con feedback di esecuzione.

Su SWE-Bench Verified e Lite migliora pass@1 rispetto a sliding-window baseline, riducendo sia gli step di reasoning che il consumo di token. Modella la struttura logica delle dipendenze come meccanismo di memoria stabile e scalabile per agenti tool-using.

[[wiki/pages/memory-architectures-retrieval]]
