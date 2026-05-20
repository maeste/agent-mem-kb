---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, scientific-agents, knowledge-mining, self-evolving]
source_path: raw/papers/arxiv-2604.03964.pdf
---

# SkillFoundry: Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources

**Autori:** Shuaike Shen, Wenduo Cheng, Mingqian Ma, Alistair Turcan, Martin Jinye Zhang, Jian Ma (CMU)
**arXiv:** 2604.03964 (apr 2026) | **Code:** github.com/ma-compbio-lab/SkillFoundry

## Summary

SkillFoundry è un framework self-evolving che converte risorse scientifiche eterogenee (repo, API, script, notebook, docs, database, paper) in **validated agent skills**. Il gap: ecosistemi scientifici sono ricchi di conoscenza procedurale ma frammentata in artifact che gli agenti non possono operazionalizzare.

## Pipeline

1. Organizza il target domain come **domain knowledge tree**
2. Mine resources da high-value branches
3. Estrae **operational contracts** (task scope, I/O, execution steps, env assumptions, provenance, tests)
4. Compila in **executable skill packages**
5. Closed-loop validation: expand / repair / merge / prune iterativamente

## Risultati

- **71.1%** delle skill mined differiscono da skill libraries esistenti (SkillHub, SkillSMP) → sostanzialmente novel
- Migliora coding agent performance su **5/6** dataset MoSciBench
- Task-specific skills per genomics: cell type annotation + scDRR workflow — miglioramenti sostanziali

## Relazione con altri lavori

- Complementare a [[wiki/sources/arxiv-2604.04804]] (SkillX): SkillFoundry è domain-specific (scientifico), SkillX è general-purpose
- Si collega a [[wiki/sources/arxiv-2604.24594]] (SRA): SkillFoundry produce le skill che SRA deve recuperare
- Rilevante per [[wiki/sources/xu-2026-agent-skills-survey]] come caso d'uso domain-specific
