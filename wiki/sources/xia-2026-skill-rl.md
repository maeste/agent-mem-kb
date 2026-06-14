---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [agent-skills, skill-learning, reinforcement-learning, skill-library]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented RL

**Peng Xia et al.**, arXiv:2602.08234, Feb 2026.

## Summary

SkillRL è un framework che collega raw experience e miglioramento della policy attraverso **scoperta automatica di skills** ed evoluzione ricorsiva. Introduce un meccanismo di distillazione experience-based per costruire una **skill library gerarchica (SKILL BANK)**, una strategia di retrieval adattiva per euristiche generali e task-specific, e un meccanismo di evoluzione ricorsiva che fa co-evolvere la libreria skills con la policy dell'agente durante RL.

## Key Claims

- SkillRL raggiunge **SOTA su ALFWorld, WebShop e 7 task search-augmented**, superando i strong baselines di oltre il **15.3%** [[wiki/sources/xia-2026-skill-rl]](raw/papers/arxiv-2602.08234.pdf).
- Le traiettorie raw sono spesso ridondanti e noise-heavy; le skills strutturate riducono il token footprint migliorando l'utilità di ragionamento [[wiki/sources/xia-2026-skill-rl]](raw/papers/arxiv-2602.08234.pdf).
- La robustezza si mantiene quando la complessità del task aumenta [[wiki/sources/xia-2026-skill-rl]](raw/papers/arxiv-2602.08234.pdf).
