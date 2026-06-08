---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [agent-skills, survey, skill-acquisition, security, mcp]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and Path Forward

**Renjun Xu, Yang Yan** (Zhejiang University) — arXiv:2602.12430, Feb 2026

## Summary

Survey comprehensivo sul paradigma delle agent skills, primo trattamento focalizzato specificamente sullo strato di astrazione skills (non su agenti LLM in generale, non su tool use). Organizza il campo lungo quattro assi:

1. **Architetturali**: specifica SKILL.md, progressive context loading, relazione con MCP
2. **Acquisizione**: RL con skill libraries (SAGE), autonomous skill discovery (SEAgent), compositional skill synthesis
3. **Deployment a larga scala**: computer-use agent stack, GUI grounding, benchmark OSWorld/SWE-bench
4. **Security**: il 26.1% delle skills community-contributed contiene vulnerabilità; propone **Skill Trust and Lifecycle Governance Framework** — modello a 4 tier con permission map basata sulla provenienza

Identifica **7 open challenges**: portabilità cross-platform, capability-based permission models, e altri. Risorse: https://github.com/scienceaix/agentskills

## Key claims
- Le skills rappresentano un'astrazione superiore rispetto ai tools tradizionali ([§1](raw/papers/arxiv-2602.12430.pdf))
- La sicurezza delle skills è un problema empiricamente dimostrato ([§6](raw/papers/arxiv-2602.12430.pdf))
- MCP e skills sono strati complementari dell'agentic stack ([§3](raw/papers/arxiv-2602.12430.pdf))

## Connections
- [[wiki/sources/xu-2026-agent-skills-survey]] — fonte primaria
- [[wiki/pages/agent-skills]] — architettura e acquisizione skills
