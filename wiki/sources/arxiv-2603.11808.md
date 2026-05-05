---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2603.11808.pdf
---

# Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories

**Authors:** Shuzhen Bi, Mengsong Wu, Hao Hao, Keqian Li, Wentao Liu, Siyu Song, Hongbo Zhao, Aimin Zhou (ECNU / Shanghai Innovation Institute / USTC), 2026.

This paper presents a systematic framework for automatically extracting agent skills from open-source GitHub repositories, addressing the scalability bottleneck of manual skill authoring. The framework operates in three stages: (1) repository structural analysis that produces hierarchical maps of execution scripts, configuration files, and domain modules; (2) semantic skill identification via dense retrieval mechanisms that match repository components to skill candidate slots; and (3) translation into the standardized SKILL.md format implementing Anthropic's progressive disclosure architecture with three hierarchical levels — metadata (30–100 tokens, pre-loaded), instructions (200–5,000 tokens, loaded on activation), and resources (unbounded, loaded on demand) (Bi et al., 2026). The authors ground their formalization in the S = (C, π, T, R) skill tuple from prior work and validate extraction on two systems: TheoremExplainAgent (STEM theorem visualization) and Code2Video (educational video generation), both using the Manim engine. Their analysis finds that agent-generated educational content achieves 40% gains in knowledge transfer efficiency while maintaining pedagogical quality comparable to human-crafted tutorials. The paper emphasizes the importance of security governance and multi-dimensional evaluation metrics in the extraction pipeline, arguing that systematic mining of agentic repositories provides a scalable middle path between manual authoring and autonomous open-world discovery.
