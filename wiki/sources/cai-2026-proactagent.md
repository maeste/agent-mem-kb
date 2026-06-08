---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [proactive-retrieval, lifelong-learning, experience-driven-agents, memory-refinement]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval for Experience-Driven Lifelong Agents

**Yuxuan Cai et al.** (East China Normal Univ, Shanghai AI Lab) — arXiv:2604.20572, Apr 2026

## Summary

ProactAgent è un framework di lifelong learning che affronta due limitazioni fondamentali degli agenti esistenti: (1) il retrieval è passivo, triggerato da posizioni predefinite o regole esterne; (2) le strategie di update trattano memoria testuale e parametriche come processi indipendenti.

Due componenti:
1. **EXPONEVO** (Experience-Enhanced Online Evolution): migliora congiuntamente l'agente tramite memory refinement e policy optimization. L'experience base organizza interazioni storiche in repository tipizzati: factual memory, episodic memory, behavioral skills.
2. **PROACTRL** (Proactive RL-based Retrieval): modella il retrieval come azione di policy esplicita, impara quando e cosa recuperare tramite **paired-branch process rewards**. Confronta continuazioni da identici prefissi di interazione con/ senza retrieval per fornire supervisione step-level.

Risultati su SciWorld (73.50%), AlfWorld (71.28%), StuLife (competitivo con modelli proprietari), con sostanziale riduzione overhead retrieval.

## Key claims
- Il retrieval proattivo è superiore a statico, continuo o LLM-gated ([§Abstract](raw/papers/arxiv-2604.20572.pdf))
- Le paired-branch rewards abilitano learning del retrieval senza modello addizionale ([§4](raw/papers/arxiv-2604.20572.pdf))
- Memoria e policy devono evolvere congiuntamente ([§3](raw/papers/arxiv-2604.20572.pdf))

## Connections
- [[wiki/sources/cai-2026-proactagent]] — fonte primaria
- [[wiki/pages/proactive-retrieval]] — retrieval guidato dall'agente
