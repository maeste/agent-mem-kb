---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, lifelong-learning, proactive-retrieval, agents]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval for Experience-Driven Lifelong Agents

**Cai et al. (2026)** — East China Normal University / Shanghai AI Lab

## Summary

ProactAgent è un framework di lifelong learning per agenti con **retrieval proattiva** da una base di esperienza strutturata. Il problema identificato: i metodi esistenti trattano il retrieval da esperienza passata come operazione passiva, attivandolo solo all'inizio del task o dopo uno step. L'agente fallisce nell'identificare knowledge gaps durante l'interazione e nel recuperare proattivamente l'esperienza più utile.

## Componenti

1. **ExpoNevo (Experience-Enhanced Online Evolution)**: miglioramento continuo tramite policy updates + memory refinement. La base esperienza organizza le interazioni in repository tipizzati: factual memory, episodic memory, behavioral skills.
2. **ProactRL (Proactive RL-based Retrieval)**: modella il retrieval come azione di policy esplicita; impara *quando* e *cosa* recuperare via paired-branch process rewards. Confronta continuazioni da identici prefissi di interazione con/senza retrieval.

## Risultati

- SciWorld: **73.50%** success rate
- AlfWorld: **71.28%** success rate
- Substantially reduced retrieval overhead
- Performance competitiva con modelli proprietari su StuLife

## Claim chiave

- Il retrieval proattivo basato su outcome migliora significativamente le performance lifelong rispetto al retrieval passivo [[wiki/sources/arxiv-2604.20572]]
- La comparazione paired-branch (con/ senza retrieval) fornisce supervisione step-level per decisioni di retrieval [[wiki/sources/arxiv-2604.20572]]
