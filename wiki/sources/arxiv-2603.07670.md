---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, agents, survey, taxonomy, evaluation]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Frontiers

**Du (2026)** — Hong Kong Research Institute of Technology

## Summary

Survey comprehensivo sulla memoria negli agenti LLM (2022-early 2026). Formalizza la memoria agente come loop **write-manage-read** strettamente accoppiato con percezione e azione. Introduce una tassonomia tridimensionale: temporal scope, representational substrate, control policy.

## Cinque famiglie di meccanismi

1. **Context-resident compression**: compressione dentro il context window
2. **Retrieval-augmented store**: memorie esterne con retrieval
3. **Reflective self-improvement**: auto-miglioramento da feedback
4. **Hierarchical virtual context**: contesto virtuale a più livelli
5. **Policy-learned management**: gestione appresa via RL

## Evaluation e applicazioni

Traccia lo spostamento da benchmark di recall statici a test agentic multi-sessione che interlacciano memoria con decision-making. Analizza 4 benchmark recenti che espongono gap persistenti.

Applicazioni dove la memoria è fattore differenziale: personal assistant, coding agent, open-world games, scientific reasoning, multi-agent teamwork.

## Open challenges identificate

Continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, multimodal embodied memory.

## Claim chiave

- La memoria trasforma un LLM stateless in un agente self-evolving [[wiki/sources/arxiv-2603.07670]]
- Il campo manca ancora di una soluzione al problema della continual consolidation [[wiki/sources/arxiv-2603.07670]]
