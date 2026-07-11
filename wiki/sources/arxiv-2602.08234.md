---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [skill-discovery, reinforcement-learning, skill-library, experience-distillation, alfworld, webshop]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**Xia, Chen, Wang, Liu, Zeng, Wang, Han, Zhou, Zhao, Chen, Zheng, Xie, Yao** (UNC-Chapel Hill, U Chicago, UCSD, NEC Labs, UC Berkeley, UCSC) — arXiv:2602.08234, Feb 2026

## Summary

SkillRL è un framework che bridge il gap tra raw experience e policy improvement tramite **automatic skill discovery** ed **evoluzione ricorsiva**, trasformando traiettorie ridondanti in una libreria di skill gerarchica riutilizzabile.

## Claim principali

- **Problema**: i metodi memory-based esistenti salvano raw trajectories che sono redundant e noise-heavy. Questo impedisce agli agent di estrarre behavioral patterns high-level, riutilizzabili e essenziali per la generalizzazione [[raw/papers/arxiv-2602.08234.pdf]].
- **Skill Bank**: libreria di skill gerarchica costruita via experience-based distillation mechanism che trasforma esperienze diverse in skill strutturate [[raw/papers/arxiv-2602.08234.pdf]].
- **Adaptive retrieval strategy**: per euristiche generali e task-specific [[raw/papers/arxiv-2602.08234.pdf]].
- **Recursive evolution**: la skill library co-evolve con la policy dell'agente durante reinforcement learning. I due sistemi si rafforzano reciprocamente [[raw/papers/arxiv-2602.08234.pdf]].
- **Risultati**: SOTA su ALFWorld, WebShop e 7 search-augmented tasks, outperforming strong baselines >15.3%. Robustness mantenuta quando task complexity aumenta [[raw/papers/arxiv-2602.08234.pdf]].
- **Riduzione token footprint**: le skill compressono l'esperienza migliorando contemporaneamente reasoning utility [[raw/papers/arxiv-2602.08234.pdf]].

## Posizione nel dibattito

Rileva che memorie grezze (trajectories) sono un formato inefficiente per il learning. La distillazione in skill + evoluzione ricorsiva è un approccio che connette memory research con RL per agent. Complementa ProactAgent (entrambi usano RL ma con focus diversi).
