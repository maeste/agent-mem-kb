---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [reinforcement-learning, skill-library, skill-discovery, agents]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**Autori:** Peng Xia, Jianwen Chen, Hanyang Wang et al.
**arXiv:** 2602.08234 | Febbraio 2026

## Riassunto

SkillRL bridgea il gap tra esperienza grezza e miglioramento della policy tramite scoperta automatica di skills ed evoluzione ricorsiva. A differenza dei metodi memory-based che memorizzano traiettorie raw (spesso ridondanti e noise-heavy), SkillRL estrae pattern comportamentali riutilizzabili di alto livello.

Componenti principali:
1. **Experience distillation**: trasforma esperienze diverse in skills strutturate in una libreria gerarchica (SKILL BANK)
2. **Adaptive retrieval**: strategia per euristiche generali e task-specific
3. **Recursive evolution**: la libreria skills co-evolve con la policy dell'agente durante RL

Risultati su ALFWorld, WebShop e 7 task search-augmented: SOTA, +15.3% sui baselines, robustezza mantenuta al crescere della complessità del task. Riduce significativamente il token footprint migliorando l'utilità di reasoning.

## Claim chiave

- La distillazione di esperienza in skills strutturate supera la memorizzazione di traiettorie raw [[wiki/sources/arxiv-2602.08234.md]]
- L'evoluzione ricorsiva della skill library insieme alla policy abilita miglioramento continuo [[wiki/sources/arxiv-2602.08234.md]]
- Le skills gerarchiche riducono token footprint mantenendo reasoning utility [[wiki/sources/arxiv-2602.08234.md]]

## Collegamenti

- Alternativa a [[wiki/sources/wang-2023-voyager.md]] (Voyager) per skill library: SkillRL usa RL, Voyager usa prompting
- Relazionato a [[wiki/pages/skill-management]]
- Complementa [[wiki/sources/xia-2026-skill-rl.md]] (stesso lavoro)
