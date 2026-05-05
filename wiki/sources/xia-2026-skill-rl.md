---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, skills, reinforcement-learning, skill-distillation, recursive-evolution, grpo]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SKILL RL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

Peng Xia et al. (UNC Chapel Hill, U Chicago, UCSD, NEC Labs, UC Berkeley, UCSC), arXiv:2602.08234, 2026.

## Summary

SKILL RL è un framework che collega esperienza grezza e miglioramento di policy tramite scoperta automatica di skill ed evoluzione ricorsiva. Tre componenti chiave: (1) meccanismo di distillazione experience-based che trasforma traiettorie in skill — episodi di successo diventano dimostrazioni, fallimenti vengono sintetizzati in lezioni di failure concisi per ridurre il rumore contestuale; (2) SKILL BANK gerarchico che distingue general skills (guida strategica universale) da task-specific skills (euristica per task specifici), con retrieval adattivo; (3) meccanismo di evoluzione ricorsiva dove la skill library e la policy dell'agente co-evolvono durante RL — dopo ogni epoch di validazione, i failure modes vengono analizzati per generare o raffinare skill. Su ALFWorld, WebShop e 7 task search-augmented supera i baseline del 15.3% con significativamente meno contesto rispetto a metodi memory-based.

## Key claims

- La distillazione da traiettoria a skill astratta riduce l'footprint di token e migliora l'utilità di reasoning rispetto alla memorizzazione di traiettorie grezze [[wiki/pages/skill-extraction-from-memory]] [[wiki/pages/experience-reuse-continual-learning]]
- La co-evoluzione di skill library e policy durante RL supera il paradigma di memoria statica — le skill vengono raffinate in base ai failure modes osservati
- Le skill gerarchiche (generali + task-specific) abilitano un retrieval adattivo che bilancia transfer e specificity
