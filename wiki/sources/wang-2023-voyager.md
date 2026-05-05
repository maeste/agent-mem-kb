---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, skills, skill-library, embodied-agent, minecraft, lifelong-learning, code-as-action]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# VOYAGER: An Open-Ended Embodied Agent with Large Language Models

Guanzhi Wang et al. (NVIDIA, Caltech, UT Austin, Stanford, UW Madison), arXiv:2305.16291, 2023.

## Summary

VOYAGER è il primo agente LLM-powered per lifelong learning embodied in Minecraft. L'agente esplora autonomamente il mondo, acquisisce skill diversificate e compie scoperte senza intervento umano. Si compone di tre moduli: (1) un curriculum automatico che genera task progressivamente più difficili in base allo stato dell'agente e dell'ambiente; (2) una skill library in crescita dove i programmi JavaScript di successo vengono memorizzati e recuperati per similarity embedding al momento del bisogno; (3) un meccanismo di prompting iterativo che usa il codice come spazio d'azione e incorpora feedback dall'ambiente ed errori di esecuzione per raffinare i programmi. Le skill sono temporally extended, interpretabili e composable. Risultati: 3.3× più item unici, 2.3× distanze di viaggio più lunghe, milestone della tech tree fino a 15.3× più veloci rispetto allo SOTA precedente. La skill library permette zero-shot generalizzazione a nuovi mondi e task.

## Key claims

- Una skill library di codice riutilizzabile con retrieval per embedding similarity abilita transfer e mitiga catastrophic forgetting senza fine-tuning [[wiki/pages/skill-extraction-from-memory]] [[wiki/pages/experience-reuse-continual-learning]]
- Il curriculum automatico basato su GPT-4 funziona come novelty search in-context, proponendo task calibrati sullo stato corrente dell'agente
- L'accuratezza di retrieval delle skill (top-5: 96.5%) dimostra che il recupero per similarità è affidabile per skill di codice in domini strutturati
