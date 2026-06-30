---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [skills, agents, survey, security, MCP, architecture]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and Path Forward

**Xu & Yan (2026)** — Zhejiang University

## Summary

Survey sullo strato di **agent skills** come astrazione emergente per estendere le capability LLM senza retraining. Una skill è un pacchetto auto-contenuto: file di istruzioni strutturato (SKILL.md), script opzionali, documenti di riferimento, asset. L'agente scopre, carica e segue la skill quando task rilevanti emergono.

Organizza il campo su 4 assi:

1. **Architectural foundations**: specifica SKILL.md, progressive context loading, ruolo complementare di skills e MCP (Model Context Protocol)
2. **Skill acquisition**: RL con skill libraries (SAGE), autonomous skill discovery (SEAgent), compositional skill synthesis
3. **Deployment at scale**: computer-use agent stack, GUI grounding, benchmark OSWorld/SWE-bench
4. **Security**: **26.1%** delle skills community-contributed contengono vulnerabilità

## Governance proposta

**Skill Trust and Lifecycle Governance Framework**: modello a 4 tier con permission basate gate che mappano provenienza skill a capability di deployment graduate.

## Claim chiave

- Le skills risolvono la tensione tra modelli general-purpose e expertise procedurale specializzata [[wiki/sources/arxiv-2602.12430]]
- La sicurezza è un problema critico: oltre 1/4 delle skills pubbliche ha vulnerabilità [[wiki/sources/arxiv-2602.12430]]
