---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [skill-learning, reinforcement-learning, skill-library, experience-distillation]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented RL

**Peng Xia et al.** — arXiv:2602.08234, Feb 2026

## Summary

SkillRL è un framework che colma il gap tra esperienza grezza e miglioramento della policy attraverso **scoperta automatica di skills** ed evoluzione ricorsiva. A differenza dei metodi memoria esistenti che salvano traiettorie grezze (ridondanti e noise-heavy), SkillRL distilla esperienze in **pattern comportamentali riutilizzabili** ad alto livello.

Componenti chiave:
- **Experience-based distillation**: trasforma esperienze diverse in skills strutturate (Skill Bank gerarchico)
- **Adaptive retrieval**: strategia per euristiche generali e task-specific
- **Recursive evolution**: la skill library co-evolve con la policy dell'agente durante RL

Risultati su ALFWorld, WebShop e 7 task search-augmented: SOTA, supera baselines >15.3%, robusto all'aumento della complessità. Riduce significativamente il token footprint migliorando l'utilità di reasoning.

## Key claims
- Le traiettorie grezze sono troppo ridondanti per un efficace reuse ([§1](raw/papers/arxiv-2602.08234.pdf))
- La distillazione in skills strutturate abilita transfer inter-task ([§3](raw/papers/arxiv-2602.08234.pdf))
- L'evoluzione ricorsiva di skills e policy è mutualmente vantaggiosa ([§4](raw/papers/arxiv-2602.08234.pdf))

## Connections
- [[wiki/sources/xia-2026-skill-rl]] — fonte primaria
- [[wiki/pages/skill-learning]] — apprendimento automatico di skills
