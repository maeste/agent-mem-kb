---
type: source
created: 2026-05-05
updated: 2026-06-13
tags: [skills, representation, structured, agents, ssl]
source_path: raw/papers/arxiv-2604.24026.pdf
---

# From Skill Text to Skill Structure: The SSL Representation

**Liang, Wang, Liang & Liu** (Peking University) — arXiv:2604.24026, Apr 2026

## Summary

Introduce la prima **rappresentazione strutturata** per skill di agenti che disaccoppia tre livelli di informazione tipicamente intrecciati in documenti SKILL.md testuali: scheduling (quando invocare), structure (struttura di esecuzione), e logic (azioni/risorse).

## Key claims

- **Problema di rappresentazione**: le skill attuali sono artefatti text-heavy dove segnali machine-usable (interfacce di invocazione, struttura di esecuzione, side effects) sono sepolti in descrizioni natural language.
- **SSL (Scheduling-Structural-Logical)**: ispirato a Memory Organization Packets, Script Theory e Conceptual Dependency di Schank & Abelson.
  - **Scheduling**: segnali di quando invocare la skill
  - **Structure**: struttura di esecuzione a livello di scena
  - **Logic**: evidenza su azioni e uso risorse
- **Normalizer basato su LLM** per istanziare SSL da skill testuali.
- **Risultati**: in Skill Discovery, MRR@50 migliora da 0.649 a 0.729; in Risk Assessment, macro F1 da 0.409 a 0.509 (vs baseline text-only).
- **Non è uno standard finale** ma un passo pratico verso rappresentazioni più ispezionabili e riutilizzabili.

## Positioning

Contributo metodologico fondamentale per l'ecosistema skills negli agenti. Rilevante per chi costruisce skill market o system di skill discovery.
