---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, knowledge-base, construction, hierarchy, transfer-learning]
source_path: raw/papers/arxiv-2604.04804.pdf
---

# SkillX: Automatically Constructing Skill Knowledge Bases for Agents

**Autori:** Chenxi Wang, Zhuoyun Yu, Xin Xie, Wuguannan Yao, Runnan Fang, Shuofei Qiao, Kexin Cao, Guozhou Zheng, Xiang Qi, Peng Zhang, Shumin Deng (ZJU et al.)
**arXiv:** 2604.04804 (apr 2026) | **Code:** github.com/zjunlp/SkillX

## Summary

SkillX è un framework fully automated per costruire **skill knowledge base** plug-and-play riutilizzabili across agenti e ambienti. Il problema affrontato: agenti attuali imparano in isolamento, riscoprendo ripetutamente comportamenti simili da esperienza limitata.

## Pipeline (3 innovazioni)

1. **Multi-Level Skills Design**: distilla traiettorie raw in gerarchia a 3 livelli — strategic plans → functional skills → atomic skills
2. **Iterative Skills Refinement**: revisione automatica delle skill basata su execution feedback per migliorare continuamente qualità della libreria
3. **Exploratory Skills Expansion**: generazione e validazione proattiva di skill novel per espandere coverage oltre seed data

## Risultati

- SkillKB migliorano task success e execution efficiency quando plugged in agenti base più deboli (transfer learning)
- Valutazione su AppWorld, BFCL-v3, τ²-Bench
- Backbone: GLM4.6

## Relazione con altri lavori

- Complementare a [[wiki/sources/arxiv-2604.24026]] (SSL): SkillX *costruisce* le skill, SSL le *rappresenta* strutturalmente
- Si collega a [[wiki/sources/arxiv-2604.03964]] (SkillFoundry): entrambi costruiscono skill KB automaticamente, ma SkillX è general-purpose mentre SkillFoundry è domain-specific (scientifico)
- Converge con [[wiki/sources/li-2026-skillflow]] sul tema di skill extraction da traiettorie
