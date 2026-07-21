---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [agent, embodied-ai, minecraft, skill-library, lifelong-learning, llm]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# Voyager: Open-Ended Embodied Agent with LLMs

**Autori:** Wang et al. (NVIDIA, Caltech, UT Austin, Stanford) | **arXiv:** 2305.16291 | **Ott 2023**

## Summary

Voyager è il primo agente LLM-powered con apprendimento lifelong in Minecraft, capace di esplorare continuamente il mondo, acquisire skill diverse e fare scoperte senza intervento umano. L'architettura si articola in tre componenti chiave:

1. **Curriculum automatico**: massimizza l'esplorazione generando task adattativi basati sullo stato corrente dell'agente e sulle capacità già acquisite.
2. **Skill library in crescita**: memorizza comportamenti complessi come codice eseguibile (programmi Python/Voyager API), consentendo composizione e riutilizzo.
3. **Meccanismo di prompting iterativo**: incorpora feedback dall'ambiente, errori di esecuzione e auto-verifica per refinare i programmi.

Voyager interagisce con GPT-4 via blackbox queries senza fine-tuning. Risultati: 3.3x item unici in più, 2.3x distanza percorsa, milestone tech tree fino a 15.3x più veloci rispetto a SOTA precedente. Le skill sono temporalmente estese, interpretabili e compostizionali, mitigando catastrophic forgetting.

## Key claims

- Le skill come codice eseguibile permettono composizione e transfer più efficaci rispetto a rappresentazioni implicite [[wiki/pages/voyager]]
- Il curriculum automatico basato su GPT-4 supera approcci RL classici per l'esplorazione open-ended
- La skill library generalizza a nuovi mondi Minecraft, mentre altri approcci faticano
