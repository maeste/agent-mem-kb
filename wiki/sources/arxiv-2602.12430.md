---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [agent-skills, survey, skill-acquisition, security, mcp, computer-use-agents]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and the Path Forward

**Xu, Yan** (Zhejiang University) — arXiv:2602.12430, Feb 2026

## Summary

Survey completo sul paradigma degli **agent skills**: pacchetti componibili di istruzioni, codice e risorse che gli agent caricano on-demand per estendere dinamicamente le capability senza retraining.

## Claim principali

- **Definizione di skill**: non un modello o prompt template, ma un pacchetto self-contained (SKILL.md + script opzionali + doc + asset) che l'agente scopre, carica e segue quando task rilevanti emergono [[raw/papers/arxiv-2602.12430.pdf]].
- **Distinzione tools vs skills**: tools eseguono e ritornano risultati; skills preparano l'agente a risolvere un problema iniettando conoscenza procedurale, modificando execution context, abilitando progressive disclosure [[raw/papers/arxiv-2602.12430.pdf]].
- **Quattro assi di analisi**: (1) architectural foundations (SKILL.md spec, progressive context loading, relazione con MCP); (2) skill acquisition (RL con skill libraries, autonomous discovery, compositional synthesis); (3) deployment at scale (CUA stack, GUI grounding, OSWorld/SWE-bench); (4) security (26.1% skill community contengono vulnerabilità) [[raw/papers/arxiv-2602.12430.pdf]].
- **Skill Trust and Lifecycle Governance Framework**: four-tier gate-based permission model che mappa skill provenance a graduated deployment capabilities [[raw/papers/arxiv-2602.12430.pdf]].
- **Ecosistema**: Anthropic ha formalizzato lo standard (Oct 2025, open Dec 2025). Repository anthropics/skills: >62K GitHub stars in 4 mesi. Partner skills da Atlassian, Figma, Canva, Stripe, Notion [[raw/papers/arxiv-2602.12430.pdf]].
- **Sette open challenges**: cross-platform portability, capability-based permission models, e altri [[raw/papers/arxiv-2602.12430.pdf]].
- **Relazione con MCP**: skills = "what to do", MCP = "how to connect" [[raw/papers/arxiv-2602.12430.pdf]].

## Posizione nel dibattito

Survey definitivo sull'emergente abstraction layer delle agent skills. Rilevante per capire dove sta andando il deployment di agent in produzione. La sezione security è particolarmente importante (26.1% vulnerability rate).
