---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, representation, structure, agents, skill-discovery]
source_path: raw/papers/arxiv-2604.24026.pdf
---

# From Skill Text to Skill Structure: SSL Representation for Agent Skills

**Autori:** Qiliang Liang, Hansi Wang, Zhong Liang, Yang Liu (Peking University)
**arXiv:** 2604.24026 (apr/mag 2026) | **Code:** github.com/COOLPKU/SSL

## Summary

Introduce **SSL (Scheduling-Structural-Logical)**: la prima rappresentazione strutturata per skill di agenti LLM che disentangle tre livelli di informazione attualmente intrecciati in documenti SKILL.md testuali.

## I 3 layer SSL

1. **Scheduling Layer** (skill-level): segnali di invocazione — goal, intent, signature, tags, inputs/outputs, precondizioni. Risponde a "quando invocare questa skill?"
2. **Structural Layer** (scene-level): grafo delle fasi di esecuzione — prepare → act → acquire → verify → finish/retry. Ogni scena ha tipo (READ/CALL/WRITE/EXPORT/CHECK) e target (local files / external API).
3. **Logical Layer** (action-level): azioni atomiche + evidenza di uso risorse — side effects, credentials, retry logic.

Ispirato a Memory Organization Packets, Script Theory e Conceptual Dependency di Schank & Abelson.

## Normalizzazione

LLM-based normalizer converte SKILL.md testuali in rappresentazione SSL strutturata. La struttura rimane paired con il documento sorgente originale.

## Risultati

- **Skill Discovery**: MRR@50 da 0.649 (text-only) → **0.729 (SSL)** (+12%)
- **Risk Assessment**: macro F1 da 0.409 (text-only) → **0.509 (SSL)** (+24%)

## Relazione con altri lavori

- Complementare diretto di [[wiki/sources/arxiv-2604.24594]] (SRA): mentre SRA definisce il paradigma di retrieval delle skill, SSL definisce come **rappresentare** le skill per renderle recuperabili e ispezionabili
- Rilevante per [[wiki/sources/xu-2026-agent-skills-survey]] e [[wiki/sources/li-2026-skillflow]]
- Si collega al tema experience compression spectrum di [[wiki/sources/zhang-2026-lightmem]]: SSL è un passo verso rappresentazioni più strutturate (higher compression) delle skill
