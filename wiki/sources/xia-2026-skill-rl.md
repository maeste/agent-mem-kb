---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [skill-discovery, reinforcement-learning, skill-library, recursive-evolution, alfworld, webshop]
source_path: raw/papers/arxiv-2602.08234.pdf
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**Autori:** Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, Huaxiu Yao  
**Data:** Febbraio 2026 | arXiv:2602.08234

## Sintesi

SkillRL bridge il gap tra raw experience e policy improvement attraverso **skill discovery automatica ed evoluzione ricorsiva**. Il problema di partenza: i metodi memory-based esistenti salvano raw trajectories che sono ridondanti e noise-heavy, impedendo agli agent di estrarre pattern comportamentali riutilizzabili di alto livello.

### Architettura

1. **Experience-based distillation mechanism:** trasforma esperienze diverse in **skill strutturate**
2. **SKILL BANK (hierarchical skill library):** libreria di skills organizzata gerarchicamente
3. **Adaptive retrieval strategy:** per euristiche generali e task-specific
4. **Recursive evolution mechanism:** la skill library co-evolve con la policy dell'agente durante RL

### Risultati

- **ALFWorld:** SOTA, convergenza piu' rapida e success rate superiore vs vanilla GRPO e memory-augmented RL
- **WebShop:** SOTA
- **7 search-augmented tasks:** outperform strong baselines di **>15.3%**
- Robustness mantenuta con l'aumentare della complessita' del task
- Riduzione significativa del token footprint con miglioramento del reasoning utility

## Claim chiave

- Le raw trajectories non sono il formato giusto per l'apprendimento agentico; le skills estratte (alta compressione, behavioral patterns) lo sono [[wiki/sources/arxiv-2604.27707.md]]
- L'evoluzione ricorsiva della skill library insieme alla policy e' chiave per il lifelong improvement
- La distillazione da esperienza (sia successo che fallimento, unlike sistemi che scartano i fallimenti) arricchisce lo spazio delle skills

## Posizione nelvault

Contributo all'intersezione tra memory/experience e RL per agent. Collega il tema "skills come memoria compressa" (Xu et al. 27707 spectrum) con implementazione RL concreta.
