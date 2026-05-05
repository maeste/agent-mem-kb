---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.04804.pdf
---

# SkillX: Automatically Constructing Skill Knowledge Bases for Agents

Wang, Yu, Xie, Yao, Fang, Qiao, Cao, Zheng, Qi, Zhang, Deng (Zhejiang University, Ant Group), April 2026.

SkillX is a fully automated framework for building plug-and-play skill knowledge bases that can be transferred across different LLM agents and environments. The paper identifies three core problems with current self-evolving agent paradigms: isolated learning (agents redundantly re-discover similar behaviors), weak generalization of mined experience, and a model capability bottleneck that caps what can be extracted through an agent's own exploration alone. To address these issues, SkillX introduces three synergistic innovations: (1) *Multi-Level Skills Design*, which distills raw trajectories into a three-tiered hierarchy of strategic plans, functional skills, and atomic skills; (2) *Iterative Skills Refinement*, which revises skills based on execution feedback; and (3) *Exploratory Skills Expansion*, which proactively generates and validates novel skills beyond seed data. Using GLM4.6 as a backbone, the authors automatically construct a reusable skill library and demonstrate consistent improvements in task success and execution efficiency when the library is plugged into weaker base agents on benchmarks including AppWorld, BFCL-v3, and τ²-Bench. The key claim is that structured, hierarchical experience representations are essential for generalizable agent learning, in contrast to flat trajectory or insight formats.
