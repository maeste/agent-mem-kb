---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [proactive-retrieval, lifelong-learning, experience-reuse, rl]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval for Lifelong Agents

**Autori:** Cai et al. (East China Normal Univ, Shanghai AI Lab) | **arXiv:** 2604.20572 | **Apr 2026**

## Summary

ProactAgent è un framework lifelong learning con **retrieval proattiva** da una base esperienza strutturata. A differenza di approcci passivi che recuperano solo all'inizio task o dopo uno step, ProactAgent identifica knowledge gaps durante l'interazione e recupera proattivamente l'esperienza più utile.

Due componenti:
1. **EXPONEVO** (Experience-Enhanced Online Evolution): miglioramento continuo via policy updates + memory refinement. L'experience base organizza interazioni in repository tipizzati (factual memory, episodic memory, behavioral skills).
2. **PROACT RL**: modella retrieval come azione policy esplicita, impara quando e cosa recuperare via paired-branch process rewards confrontando continuazioni con/senza retrieval.

## Key claims

- Success rate 73.50% su SciWorld, 71.28% su AlfWorld con overhead retrieval sostanzialmente ridotto [[wiki/pages/proactagent]]
- Performance competitive con modelli proprietari su StuLife
- Il retrieval proattivo supera quello passivo quando il gap conoscenza emerge mid-interaction
