---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [agent-skills, survey, skill-acquisition, security, model-context-protocol]
source_path: raw/papers/arxiv-2602.12430.pdf
---

# Agent Skills for LLMs: Architecture, Acquisition, Security, and the Path Forward

**Autori:** Renjun Xu, Yang Yan (Zhejiang University) | **arXiv:** 2602.12430 | **Febbraio 2026**

## Sintesi

Survey completo sullo strato di **agent skills** — pacchetti componibili di istruzioni, codice e risorse che gli agent caricano on-demand. Organizza il campo lungo 4 assi: architettura, acquisizione, deployment scalabile, sicurezza.

## Aspetti chiave

1. **Architettura:** specifica SKILL.md, progressive context loading, ruolo complementare con MCP (Model Context Protocol)
2. **Acquisizione:** RL con skill libraries (SAGE), scoperta autonoma (SEAgent), sintesi composizionale
3. **Deployment:** computer-use agent stack, GUI grounding, benchmark OSWorld/SWE-bench
4. **Sicurezza:** il **26.1%** delle skills della community contiene vulnerabilita; propone Skill Trust and Lifecycle Governance Framework a 4 tier

## Contesto

Standard aperto lanciato da Anthropic (Ott 2025, open Dic 2025). Repository anthropics/skills: >62k stelle in 4 mesi. Partner: Atlassian, Figma, Canva, Stripe, Notion.

## Sfide aperte (7)

Portabilita cross-platform, permission models basati su capability, e altri.

## Collegamenti nel vault

- [[wiki/pages/agent-skills-ecosystem]] — survey di riferimento per l'ecosistema delle agent skills
