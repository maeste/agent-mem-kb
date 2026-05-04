---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, proactive-retrieval, lifelong-learning, reinforcement-learning]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Ask Only When Needed — Proactive Retrieval for Lifelong Agents

**Autori:** Yuxuan Cai et al. (East China Normal U., Shanghai AI Lab)
**Data:** 2026-04-22

## Summary

ProactAgent insegna all'agente quando recuperare esperienza dalla memoria in modo proattivo, piuttosto che solo all'inizio del task o dopo ogni step. Due componenti: (1) Experience-Enhanced Online Evolution (EXPONEVO) per miglioramento continuo via policy update e memory refinement, con experience base strutturata (factual, episodic, behavioral skills); (2) Proactive RL-based Retrieval (PROACTRL) che modella il retrieval come azione esplicita di policy, apprendendo quando e cosa recuperare via paired-branch process rewards.

Su SciWorld (73.50%), AlfWorld (71.28%) e StuLife, riduce significativamente l'overhead di retrieval rispetto a retrieval continuo. Confronta in modo favorevole retrieval statico, continuo e LLM-gated.

[[wiki/pages/experience-reuse-continual-learning]] [[wiki/pages/memory-architectures-retrieval]]
