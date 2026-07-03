---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, survey, evaluation, taxonomy, agents]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Autori:** Pengfei Du (HK Research Institute of Technology)
**arXiv:** 2603.07670 | Marzo 2026

## Riassunto

Survey strutturata su come la memoria è progettata, implementata e valutata in agenti LLM moderni, coprendo lavori dal 2022 all'inizio del 2026. Formalizza la memoria agentica come ciclo write-manage-read strettamente accoppiato con percezione e azione.

Contributi:
1. **Taxonomia tridimensionale**: temporal scope, representational substrate, control policy
2. **Cinque famiglie di meccanismi**: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, policy-learned management
3. **Valutazione**: analisi di quattro benchmark recenti che espongono gap nei sistemi attuali
4. **Applicazioni**: personal assistant, coding agent, open-world games, scientific reasoning, multi-agent teamwork
5. **Engineering realities**: write-path filtering, contradiction handling, latency budgets, privacy governance
6. **Open challenges**: continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, multimodal embodied memory

## Claim chiave

- La memoria agentica va formalizzata come ciclo write-manage-read accoppiato a percezione/azione [[wiki/sources/arxiv-2603.07670.md]]
- Esistono cinque famiglie distinte di meccanismi memory con trade-off diversi [[wiki/sources/arxiv-2603.07670.md]]
- I benchmark attuali espongono gap persistenti in continual consolidation e causal grounding [[wiki/sources/arxiv-2603.07670.md]]

## Collegamenti

- Survey di riferimento per [[wiki/pages/memory-systems]]
- Complementa [[wiki/sources/yang-2026-graph-memory.md]] (focus graph-based) e [[wiki/sources/xu-2026-agent-skills-survey.md]] (focus skills)
- Valutazione relazionata a [[wiki/sources/wei-2026-evo-memory.md]] (Evo-Memory benchmark)
