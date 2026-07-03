---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [agents, embodied-ai, minecraft, skill-library, lifelong-learning, llm]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# Voyager: An Open-Ended Embodied Agent with LLMs

**Autori:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang et al. (NVIDIA, Caltech, UT Austin, Stanford)
**arXiv:** 2305.16291 | Ottobre 2023

## Riassunto

Voyager è il primo agente embodied basato su LLM progettato per apprendimento lifelong in Minecraft, senza intervento umano. L'architettura si articola in tre componenti principali:

1. **Curriculum automatico**: massimizza l'esplorazione generando autonomamente nuovi obiettivi adattivi
2. **Skill library in crescita**: memorizza comportamenti complessi come codice eseguibile, indicizzabile e riutilizzabile
3. **Meccanismo di prompting iterativo**: incorpora feedback dall'ambiente, errori di esecuzione e auto-verifica per migliorare i programmi

Voyager interagisce con GPT-4 tramite query blackbox, senza fine-tuning. Le skills sviluppate sono temporalmente estese, interpretabili e composizionali. Risultati: 3.3x più item unici, 2.3x distanze più lunghe, milestone tech tree fino a 15.3x più veloci rispetto allo SOTA precedente. Generalizza a nuovi mondi Minecraft da zero.

## Claim chiave

- Gli agenti embodied possono acquisire skills composizionali tramite una libreria di codice eseguibile [[wiki/sources/arxiv-2305.16291.md]]
- Il prompting iterativo con feedback ambientale supera il fine-tuning per l'apprendimento lifelong [[wiki/sources/arxiv-2305.16291.md]]
- Le skills come codice (non solo testo) abilitano riutilizzo e composizione tra task diversi [[wiki/sources/arxiv-2305.16291.md]]

## Collegamenti

- Relazionato a [[wiki/pages/skill-management]] per il concetto di skill library
- Confronta con [[wiki/sources/wang-2025-mirix.md]] (MIRIX) su architetture memory multi-modulo
- Basamento per lavori successivi su skill-based agents come [[wiki/sources/li-2026-skillflow.md]]
