---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [skill-rl, skill-discovery, reinforcement-learning, experience-distillation, skill-library]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# Skill RL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**Autori:** Peng Xia et al. | **arXiv:** 2602.08234 | **Febbraio 2026**

## Sintesi

Skill RL bridge l'esperienza grezza e il miglioramento di policy tramite scoperta automatica di skills ed evoluzione ricorsiva. Costruisce una libreria gerarchica (**SKILL BANK**) da traiettorie, con retrieval adattivo e meccanismo di evoluzione ricorsiva che fa co-evolvere la libreria con la policy dell'agent durante RL.

## Componenti

- **Experience-based distillation:** estrae pattern comportamentali riutilizzabili da traiettorie in SKILL BANK
- **Adaptive retrieval:** strategia per euristiche generali e task-specific
- **Recursive evolution:** skill library co-evolve con la policy

## Risultati

- **+15.3%** vs strong baselines su ALFWorld, WebShop, 7 task search-augmented
- Robustezza mantenuta all'aumentare della complessita del task
- Riduzione significativa del token footprint con aumento dell'utilita di ragionamento

## Collegamenti nel vault

- [[wiki/pages/agent-skills-ecosystem]] — contributo su skill discovery automatica da esperienza
- [[wiki/pages/skill-extraction-from-memory]] — distillazione di skills da traiettorie grezze
