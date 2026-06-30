---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [skills, RL, skill-discovery, agents, memory]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**Xia et al. (2026)** — UNC-Chapel Hill / UC San Diego / Berkeley / others

## Summary

SkillRL è un framework che bridge il gap tra **raw experience** e **policy improvement** tramite automatic skill discovery ed evoluzione ricorsiva. Il problema: i metodi memoria-based esistenti salvano traiettorie raw, spesso ridondanti e noise-heavy, impedendo agli agenti di estrarre pattern comportamentali riutilizzabili ad alto livello.

## Componenti

1. **Experience-based distillation**: trasforma esperienze diverse in skills strutturate in una **Skill Bank** gerarchica
2. **Adaptive retrieval strategy**: per euristiche generali e task-specific
3. **Recursive evolution mechanism**: la skill library co-evolve con la policy dell'agente durante RL

Riduce significativamente il token footprint migliorando l'utilità di ragionamento.

## Risultati

- SOTA su ALFWorld, WebShop e 7 task search-augmented
- Outperform strong baselines di **>15.3%**
- Robustezza mantenuta con aumento complessità task

## Claim chiave

- Le traiettorie raw sono un formato subottimale per l'apprendimento agente; le skills estratte sono superiori per generalizzazione [[wiki/sources/arxiv-2602.08234]]
- La co-evoluzione di skill library e agent policy durante RL produce convergence più rapida [[wiki/sources/arxiv-2602.08234]]
