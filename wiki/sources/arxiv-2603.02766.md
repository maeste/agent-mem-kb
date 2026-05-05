---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2603.02766.pdf
---

# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

**Authors:** Noah Provenzano, Salaheddin Alzubi, Jaydon Bingham, Weiyuan Chen, Tu Vu (Sentient / Virginia Tech), 2026.

EvoSkill is a self-evolving framework that automatically discovers and refines reusable agent skills through iterative failure analysis, operating at the skill abstraction level rather than on low-level artifacts like prompts or codebases. The system employs three collaborating agents: an **Executor** that runs tasks under a current skill configuration, a **Proposer** that diagnoses execution failures and suggests new or refined skills, and a **Skill-Builder** that materializes proposals into structured skill folders (trigger metadata, SKILL.md instructions, helper scripts). A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying LLM remains frozen (Provenzano et al., 2026). On OfficeQA (grounded reasoning over U.S. Treasury data), EvoSkill improves Claude Code with Opus 4.5 from 60.6% to 67.9% exact-match accuracy (+7.3%). On SealQA (search-augmented QA with noisy retrieval), it yields a 12.1% gain (26.6% → 38.7%). Crucially, a skill evolved on SealQA transfers zero-shot to BrowseComp with a 5.3% accuracy improvement and no modifications, providing direct evidence that skill-level optimization produces transferable capabilities beyond the training task — unlike prompt- or code-level evolutionary approaches that remain tightly coupled to specific model-task configurations.
