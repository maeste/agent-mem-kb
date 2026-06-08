---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-survey, agent-memory, memory-evaluation, memory-taxonomy]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Pengfei Du** (HK RIT) — arXiv:2603.07670, Mar 2026

## Summary

Survey strutturato sul design, implementazione e valutazione della memoria in agenti LLM moderni, coprendo work dal 2022 all'inizio 2026. Formalizza la memoria agente come **write-manage-read loop** strettamente accoppiato con percezione e azione.

Taxonomia tridimensionale:
1. **Scope temporale**: short-term vs long-term
2. **Substrato rappresentazionale**: knowledge vs experience
3. **Policy di controllo**: non-structural vs structural

Cinque famiglie di meccanismi analizzate in profondità:
1. Context-resident compression
2. Retrieval-augmented stores
3. Reflective self-improvement
4. Hierarchical virtual context
5. Policy-learned management

Traccia lo spostamento da benchmark recall statici a test agentic multi-sessione che interlacciano memoria con decision-making. Applicazioni: personal assistant, coding agent, open-world game, scientific reasoning, multi-agent teamwork.

## Key claims
- La memoria trasforma un LLM stateless in un agente self-evolving ([§1.1](raw/papers/arxiv-2603.07670.pdf))
- Il write-path filtering e la contradiction handling sono realtà ingegneristiche critiche ([§6](raw/papers/arxiv-2603.07670.pdf))
- I frontieri aperti includono continual consolidation, causally grounded retrieval, learned forgetting ([§7](raw/papers/arxiv-2603.07670.pdf))

## Connections
- [[wiki/sources/du-2026-memory-survey]] — fonte primaria
- [[wiki/pages/memory-taxonomy]] — taxonomia dei sistemi memoria
