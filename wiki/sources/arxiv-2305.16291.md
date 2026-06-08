---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [embodied-agent, skill-library, minecraft, lifelong-learning, voyager]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# Voyager: An Open-Ended Embodied Agent with LLMs

**Guanzhi Wang et al.** (NVIDIA, Caltech, UT Austin, Stanford) — arXiv:2305.16291, Oct 2023

## Summary

Voyager è il primo agente LLM-powered con apprendimento lifelong in Minecraft che esplora continuamente il mondo, acquisisce skills diverse e fa scoperte senza intervento umano. L'architettura si articola in tre componenti chiave:

1. **Curriculum automatico**: massimizza l'esplorazione generando task adattivi basati sullo stato corrente dell'agente, sull'inventario e sui progressi.
2. **Skill library in crescita**: memorizza comportamenti complessi come codice eseguibile (programmi Voyager), rendendoli temporaneamente estensibili, interpretabili e compostabili.
3. **Iterative prompting mechanism**: incorpora feedback dall'ambiente, errori di esecuzione e auto-verifica per migliorare i programmi generati.

Voyager interagisce con GPT-4 via blackbox queries, bypassando la necessità di fine-tuning. Risultati empirici: 3.3x più item unici, 2.3x distanze maggiori, milestone tech tree fino a 15.3x più veloci rispetto allo SOTA precedente. Generalizza a nuovi mondi Minecraft partendo da zero.

## Key claims
- Le skills sviluppate da Voyager sono temporaneamente estensibili, interpretabili e composabili ([§Abstract](raw/papers/arxiv-2305.16291.pdf))
- L'uso di codice eseguibile come formato di memoria delle skills allevia il catastrophic forgetting ([§1](raw/papers/arxiv-2305.16291.pdf))
- La skill library può essere riutilizzata in nuovi mondi per risolvere task novel ([§4](raw/papers/arxiv-2305.16291.pdf))

## Connections
- [[wiki/pages/voyager]] — dettagli architetturali e valutazione
- [[wiki/pages/skill-library]] — concetto di skill library come memoria procedurale
