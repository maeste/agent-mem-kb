---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.24026.pdf
---

# From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills

Liang, Wang, Liang, Liu (Peking University), May 2026.

This paper introduces the Scheduling-Structural-Logical (SSL) representation, the first structured representation for agent skill artifacts that disentangles three layers of information currently entangled in text-heavy SKILL.md documents. Drawing on Schank and Abelson's cognitive linguistics work (Memory Organization Packets, Script Theory, Conceptual Dependency), SSL separates: a *Scheduling Layer* (skill-level interface — when to invoke, input/output signatures, tags); a *Structural Layer* (scene-level execution phases — prepare, act, acquire, verify, finish/retry); and a *Logical Layer* (atomic actions and resource-use evidence — READ, CALL, file and network side effects). An LLM-based normalizer instantiates the representation from raw SKILL.md artifacts. Evaluated on two tasks — Skill Discovery and Risk Assessment — SSL-derived representations significantly outperform text-only baselines: MRR@50 improves from 0.649 to 0.729 in discovery, and macro F1 improves from 0.409 to 0.509 in risk assessment. The key claim is that making the implicit structural signals in skill documents explicit and machine-readable enables better search, inspection, and governance of skill collections, positioning SSL as a practical step toward more operationally actionable skill representations.
