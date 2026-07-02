---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [agent-skills, skill-survey, mcp, progressive-disclosure, skill-security, computer-use-agents]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and the Path Forward

**Autori:** Renjun Xu, Yang Yan (Zhejiang University)  
**Data:** Febbraio 2026 | arXiv:2602.12430

## Sintesi

Primo survey completo sul paradigma **agent skills**: pacchetti componibili di istruzioni, codice e risorse che gli agent caricano on-demand per estendere le loro capabilities senza retraining.

### Evoluzione storica

1. **Prompt engineering (2022-2023):** istruzioni craftate, efimere e non modulari
2. **Tool use / function calling (2023-2024):** API invocabili, ma atomiche; tools eseguono e ritornano non reshape l'understanding dell'agente
3. **Skill engineering (2025-present):** bundle auto-contenuti con SKILL.md, script, documenti di riferimento, metadata

### Quattro assi di analisi

1. **Architectural foundations:** SKILL.md specification, progressive context loading, relazione tra skills e MCP (Model Context Protocol)
2. **Skill acquisition:** RL con skill libraries (SAGE), autonomous discovery (SEAgent), compositional synthesis
3. **Deployment at scale:** Computer-Use Agent stack, GUI grounding, benchmark su OSWorld e SWE-bench
4. **Security:** **26.1% delle community skills contengono vulnerabilita'**. Proposta dello Skill Trust and Lifecycle Governance Framework (4-tier, gate-based permission model)

### Contesto di mercato

- Anthropic ha lanciato Agent Skills (ottobre 2025), open standard (dicembre 2025)
- Repository anthropics/skills: **62,000+ GitHub stars** in 4 mesi
- Partner skills da Atlassian, Figma, Canva, Stripe, Notion
- MCP donato alla Linux Foundation's Agentic AI Foundation (dicembre 2025)

### Sette open challenges

1. Cross-platform skill portability
2. Capability-based permission models
3. Skill composition verification
4. Runtime skill adaptation
5. Skill quality at scale
6. Multi-agent skill coordination
7. Standardized evaluation

## Claim chiave

- Skills = "what to do", MCP = "how to connect": insieme definiscono lo stack agentic emergente [[wiki/pages/agent-skills]]
- La sicurezza delle skills e' un problema reale e quantificabile (26.1% vulnerabili) [[wiki/sources/xu-2026-agent-skills-survey.md]]
- Il paradigm shift da tools a skills e' paragonabile al passaggio da functions a objects nel software

## Posizione nelvault

Survey di riferimento sui agent skills. Fondamentale per comprendere il livello di astrazione "skill" che sta emergendo come standard de facto.
