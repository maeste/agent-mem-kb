---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [memory-survey, agent-memory-taxonomy, evaluation-benchmarks, memory-mechanisms]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Autore:** Pengfei Du (HK Research Institute of Technology) | **arXiv:** 2603.07670 | **Marzo 2026**

## Sintesi

Survey completo sulla memoria negli agent LLM (2022-inizio 2026). Formalizza la memoria agent come ciclo write-manage-read accoppiato con percezione e azione, introducendo una **tassonomia tridimensionale**: scope temporale, substrato rappresentazionale, policy di controllo.

## Taxonomia delle meccanismi (5 famiglie)

1. **Context-resident compression:** compressione dentro il contesto
2. **Retrieval-augmented stores:** memorie con retrieval esterno
3. **Reflective self-improvement:** miglioramento tramite riflessione
4. **Hierarchical virtual context:** contesto virtuale gerarchico
5. **Policy-learned management:** gestione appresa via policy

## Evaluation

Traccia lo spostamento da benchmark di recall statici a test agentic multi-sessione che interlacciano memoria con decision-making. Analizza 4 benchmark recenti che espongono gap persistenti.

## Domini applicativi

Assistenti personali, coding agent, open-world games, ragionamento scientifico, teamwork multi-agent.

## Sfide aperte

Continual consolidation, retrieval causalmente fondato, reflection trustworthy, forgetting appreso, memoria multimodale embodied.

## Collegamenti nel vault

- [[wiki/pages/llm-agent-memory]] — survey di riferimento per la tassonomia della memoria agent
- [[wiki/pages/memory-architectures-retrieval]] — tassonomia delle 5 famiglie di meccanismi
