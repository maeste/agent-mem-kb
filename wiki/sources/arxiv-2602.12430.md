---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [agent-skills, survey, architecture, mcp, security]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and Path Forward

**Autori:** Renjun Xu, Yang Yan (Zhejiang University)
**arXiv:** 2602.12430 | Febbraio 2026

## Riassunto

Survey comprehensiva sul landscape delle agent skills, organizzata lungo quattro assi:

1. **Fondamenti architetturali**: specifica SKILL.md, progressive context loading, ruoli complementari di skills e MCP (Model Context Protocol)
2. **Skill acquisition**: RL con skill libraries (SAGE), scoperta autonoma skills (SEAgent), sintesi composizionale
3. **Deployment a scala**: stack computer-use agent (CUA), avanzamenti GUI grounding, benchmark OSWorld e SWE-bench
4. **Sicurezza**: il 26.1% delle skills community-contributed contiene vulnerabilità; proposta di Skill Trust and Lifecycle Governance Framework (quattro livelli, gate-based permission model)

Identifica sette open challenges: portabilità cross-platform, permission models capability-based, e altri.

## Claim chiave

- Le agent skills rappresentano un layer di astrazione emergente distinto dai tool use generici [[wiki/sources/arxiv-2602.12430.md]]
- Il 26.1% delle skills community-contributed contiene vulnerabilità di sicurezza [[wiki/sources/arxiv-2602.12430.md]]
- Un framework di governance basato su provenance è necessario per deployment sicuro [[wiki/sources/arxiv-2602.12430.md]]

## Collegamenti

- Survey di riferimento per [[wiki/pages/skill-management]]
- Complementa [[wiki/sources/ling-2026-agent-skills-analysis.md]] (analisi data-driven empirica)
- Sicurezza relazionata a [[wiki/sources/xu-2026-contextual-agentic-memory.md]] (discussioni vulnerability)
