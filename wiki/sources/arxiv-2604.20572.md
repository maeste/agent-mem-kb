---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [proactive-retrieval, lifelong-learning, reinforcement-learning, experience-base, sciworld, alfworld]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval for Experience-Driven Lifelong Agents

**Cai, Zhou, Chen, He** (East China Normal U, Shanghai AI Lab) — arXiv:2604.20572, Apr 2026

## Summary

ProactAgent è un framework di lifelong learning che tratta il retrieval da memoria passata come **decisione proattiva appresa** (non operazione passive triggerata da regole), usando RL per imparare quando e cosa recuperare.

## Claim principali

- **Problema**: i metodi esistenti trattano il retrieval come operazione passive (trigger a task init o dopo uno step). L'agente fallisce nell'identificare knowledge gaps durante l'interazione e nel recuperare proattivamente l'esperienza più utile [[raw/papers/arxiv-2604.20572.pdf]].
- **Due componenti**: (1) **EXPONEVO** (Experience-Enhanced Online Evolution): miglioramento congiunto via policy updates + memory refinement. Experience base organizzata in typed repositories: factual memory, episodic memory, behavioral skills; (2) **PROACTRL** (Proactive RL-based Retrieval): modella retrieval come azione di policy esplicita, impara quando/cosa recuperare via paired-branch process rewards [[raw/papers/arxiv-2604.20572.pdf]].
- **Paired-branch process rewards**: confronta continuazioni da identici prefissi di interazione con e senza retrieval, fornendo supervisione step-level per decisioni di retrieval [[raw/papers/arxiv-2604.20572.pdf]].
- **Risultati**: 73.50% success rate su SciWorld, 71.28% su ALFWorld, sostanziale riduzione del retrieval overhead, competitivo con modelli proprietari su StuLife [[raw/papers/arxiv-2604.20572.pdf]].
- **Distinzione da approcci esistenti**: static initialization (una volta all'inizio), continuous retrieval (ogni step → context overload), LLM-gated retrieval (latenza extra). Proactive retrieval impara adaptive control senza model call addizionali [[raw/papers/arxiv-2604.20572.pdf]].

## Posizione nel dibattito

Primo lavoro a formulare il retrieval come policy action appresa via RL in agent lifelong. Il paired-branch reward design è un contributo metodologico interessante. Rilevante per chiunque costruisca agent a long-term con memory estesa.
