---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [proactive-retrieval, lifelong-learning, experience-reuse, reinforcement-learning, agent-memory]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# ProactAgent: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents

**Autori:** Yuxuan Cai, Jie Zhou et al. (ECNU, Shanghai AI Lab) | **arXiv:** 2604.20572 | **Aprile 2026**

## Sintesi

ProactAgent affronta il problema del retrieval passivo negli agent lifelong learning. Invece di recuperare memoria solo all'inizio task o dopo un passo, impara **quando e cosa** recuperare tramite segnali di reward a due rami, modellando il retrieval come azione di policy esplicita.

## Componenti principali

1. **EXPONEVO (Experience-Enhanced Online Evolution):** miglioramento continuo tramite aggiornamento policy + raffinamento memoria
2. **Experience base strutturata:** repository tipizzati — factual memory, episodic memory, behavioral skills
3. **PROACT-RL (Proactive Reinforcement Learning-based Retrieval):** apprende decisioni di retrieval a livello di passo confrontando continuazioni con/senza retrieval

## Risultati

- **73.50%** success rate su SciWorld, **71.28%** su AlfWorld
- Riduzione sostanziale del retrieval overhead
- Performance competitiva con modelli proprietari su StuLife

## Collegamenti nel vault

- [[wiki/pages/experience-reuse-continual-learning]] — contributo sul retrieval proattivo vs passivo
- [[wiki/pages/memory-architectures-retrieval]] — approccio RL-based al controllo del retrieval
