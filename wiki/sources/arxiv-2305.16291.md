---
type: source
created: 2026-06-11
updated: 2026-06-11
tags: [agents, embodied-ai, skill-library, llm, minecraft]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# VOYAGER: An Open-Ended Embodied Agent with Large Language Models

Wang, Xie, Jiang, Mandlekar, Xiao, Zhu, Fan, Anandkumar (NVIDIA, Caltech, UT Austin, Stanford), October 2023.

VOYAGER è il primo agente LLM-based con apprendimento lifelong in Minecraft che esplora continuamente il mondo, acquisisce skill diverse e fa scoperte senza intervento umano. Tre componenti chiave: (1) un curriculum automatico che massimizza l'esplorazione basata sul progresso corrente, (2) una skill library in crescita di codice eseguibile per memorizzare e recuperare comportamenti complessi, (3) un meccanismo di prompting iterativo che incorpora feedback ambientali, errori di esecuzione e auto-verifica. Usa GPT-4 via blackbox queries senza fine-tuning. Risultati: 3.3x più item unici, 2.3x distanze più lunghe, milestone tech tree fino a 15.3x più veloci rispetto allo SOTA precedente. Le skill sono temporally extended, interpretabili e composizionali, mitigando catastrophic forgetting. Generalizza a nuovi mondi Minecraft da zero.
