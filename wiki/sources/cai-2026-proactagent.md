---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [proactive-retrieval, lifelong-learning, experience-driven-agents, reinforcement-learning]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval from Memory and Skills for Lifelong Agents

**Yuxuan Cai et al.** (East China Normal University, Shanghai AI Lab), arXiv:2604.20572, Apr 2026.

## Summary

ProactAgent è un framework **experience-driven lifelong learning** per proactive retrieval su una base esperienza strutturata. Introduce **ExpoNEvo** (Experience-Enhanced Online Evolution) per miglioramento continuo tramite policy updates e memory refinement, e **ProactRL** (Proactive RL-based Retrieval) che modella retrieval come azione di policy esplicita, imparando quando e cosa recuperare via paired-branch process rewards.

## Key Claims

- ProactAgent raggiunge **73.50% success rate su SciWorld** e **71.28% su ALFWorld** riducendo sostanzialmente l'overhead di retrieval [[wiki/sources/cai-2026-proactagent]](raw/papers/arxiv-2604.20572.pdf).
- Il confronto tra continuazioni con e senza retrieval fornisce supervisione step-level per decisioni di retrieval [[wiki/sources/cai-2026-proactagent]](raw/papers/arxiv-2604.20572.pdf).
- Performance competitive con modelli proprietari su StuLife [[wiki/sources/cai-2026-proactagent]](raw/papers/arxiv-2604.20572.pdf).
