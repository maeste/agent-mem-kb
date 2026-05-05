---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, skills, survey, skill-library, mcp, security, progressive-disclosure, agentskills]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and the Path Forward

Renjun Xu, Yang Yan (Zhejiang University), arXiv:2602.12430, 2026.

## Summary

Prima survey dedicata esclusivamente al paradigma delle agent skills — pacchetti compostabili di istruzioni, codice e risorse che gli agenti caricano on-demand senza retraining. Il lavoro copre quattro assi: (i) fondamenti architetturali — specifica SKILL.md, progressive disclosure a tre livelli (metadata → instructions → resources), rapporto complementare con MCP ("skills = what to do, MCP = how to connect"); (ii) acquisizione di skill — RL con skill library (SAGE), scoperta autonoma (SEAgent), sintesi composizionale; (iii) deployment — stack CUA (Computer Use Agent), benchmark OSWorld e SWE-bench; (iv) sicurezza — il 26.1% delle skill contribuite dalla community contiene vulnerabilità, propone un Skill Trust and Lifecycle Governance Framework a quattro tier con permission model basato su provenienza. Identifica 7 sfide aperte: portabilità cross-platform, modelli di permission basati su capability, ecc. La specifica SKILL.md è diventata standard aperto (dic 2025), con 62K+ stelle GitHub in 4 mesi.

## Key claims

- Le agent skills sono il layer di astrazione emergente che risolve la tensione tra modelli generalisti e procedura specializzata — una skill non è un tool (che esegue e ritorna) ma un pacchetto che modifica il contesto esecutivo dell'agente [[wiki/pages/skill-extraction-from-memory]]
- Il progressive disclosure a tre livelli (metadata ~30 token, instructions 200-2K token, resources on-demand) è l'innovazione architetturale chiave che permette skill library grandi senza penalità di contesto
- La governance della sicurezza richiede mappare provenienza → verifica gates → permessi graduati, dato che una frazione significativa delle skill community è vulnerabile
