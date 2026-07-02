---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [proactive-retrieval, lifelong-learning, experience-driven-agents, reinforcement-learning, sciworld, alfworld]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval for Experience-Driven Lifelong Agents

**Autori:** Yuxuan Cai, Jie Zhou, Qin Chen, Liang He (East China Normal University, Shanghai AI Lab)  
**Data:** Aprile 2026 | arXiv:2604.20572

## Sintesi

ProactAgent affronta il problema del **retrieval passivo** nei lifelong learning agent. I metodi esistenti triggerano la retrieval solo all'inizio task o dopo un passo, fallendo nell'identificare knowledge gaps durante l'interazione.

### Due componenti principali

1. **EXPONEVO (Experience-Enhanced Online Evolution):**
   - Miglioramento continuo tramite policy updates + memory refinement
   - Experience base strutturata in typed repositories:
     - **Factual memory:** fatti osservati
     - **Episodic memory:** traiettorie di interazione
     - **Behavioral skills:** pattern comportamentali riutilizzabili
   - Aggiorna sia la memoria che la policy online (non isolatamente)

2. **PROACTRL (Proactive RL-based Retrieval):**
   - Modella la retrieval come azione esplicita della policy
   - Impara *quando* e *cosa* recuperare via **paired-branch process rewards**
   - Confronta continuazioni da identici prefissi di interazione con e senza retrieval
   - Fornisce supervisione step-level per decisioni di retrieval

### Risultati

- **SciWorld: 73.50% success rate**
- **ALFWorld: 71.28% success rate**
- Substantial reduction del retrieval overhead
- Performance competitiva con modelli proprietari su StuLife

## Claim chiave

- La retrieval passiva (static init, continuous, LLM-gated) e' intrinsecamente limitata [[wiki/sources/hu-2026-continual-learning-memory.md]]
- Il paired-branch process reward permette di imparare quando la retrieval migliora realmente l'outcome
- L'evoluzione congiunta di memoria e policy e' necessaria per lifelong adaptation

## Posizione nel vault

Framework completo per lifelong learning agentico. Collega memory management con RL-based decision making. Complementa RSCB-MC (quando non recuperare) con "quando/cosa recuperare proattivamente".
