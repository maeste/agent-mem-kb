---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.03964.pdf
---

# SkillFoundry: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources

**Authors:** Shuaike Shen, Wenduo Cheng, Mingqian Ma, Alistair Turcan, Martin Jinye Zhang, Jian Ma (CMU Computational Biology / Machine Learning), 2026.

SkillFoundry addresses the gap between abundant scientific procedural knowledge (scattered across repos, APIs, notebooks, papers, databases) and usable agent capabilities by converting heterogeneous domain resources into validated agent skills. The framework organizes a target domain as a **domain knowledge tree** where internal nodes represent subdomains and leaves represent actionable skill targets; under-covered branches trigger targeted mining, producing a closed-loop acquisition process rather than open-ended collection (Shen et al., 2026). Mined artifacts are compiled into structured skill cards specifying scope, dependencies, inputs/outputs, provenance, and tests, then validated through execution testing, system testing, and synthetic-data testing. Skills that pass are added as new leaves; redundant or low-value ones are consolidated or pruned, making the library self-evolving. The framework produces a substantially novel library: 71.1% of mined skills differ from existing libraries like SkillHub and SkillSMP. Evaluated on MoSciBench, mined skills improve coding agent performance on five of six datasets. SkillFoundry can also design task-specific skills on demand — demonstrated on two challenging genomics tasks (cell type annotation and scDRS workflow), where newly synthesized skills substantially boost agent performance. The work is skill-centric rather than tool-centric, focusing on packaging procedural knowledge rather than merely exposing executable interfaces.
