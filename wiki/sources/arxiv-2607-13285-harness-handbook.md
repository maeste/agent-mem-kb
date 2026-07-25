---
type: source
created: 2026-07-25
updated: 2026-07-25
tags: [harness, behavior-localization, agent-evolution, coding-agent, repository-understanding, progressive-disclosure]
source_path: raw/papers/arxiv-2607.13285.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable

**Authors:** Ruhan Wang, Yucheng Shi, Zongxia Li, et al. (Tencent, Indiana U, UMD, UGA, NUS) | **arXiv:** 2607.13285 | **Date:** Jul 14, 2026

## Summary

Defines **behavior localization**, the problem of identifying every code site that implements a target behavior before editing it, as the central bottleneck in harness evolution. Proposes the **Harness Handbook**, a behavior-centric representation synthesized from a harness codebase via static program analysis plus LLM-assisted behavioral structuring. Complements it with **Behavior-Guided Progressive Disclosure (BGPD)**, a workflow that leads coding agents from high-level behavior descriptions to relevant implementation details and verifies candidate locations against current source. On two open-source harnesses (Codex, Terminus-2), handbook-assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens. Biggest gains appear on changes involving scattered implementation sites, rarely executed code paths, and cross-module interactions.

## Problem

Production harnesses are large, tightly coupled, and behaviorally distributed across files, functions, execution stages, and state transitions. A modification request describes what the system should do, but repositories are organized by files and modules. Existing code search, repository indexing, and long-context tools leave developers and coding agents to recover the behavior-to-code mapping themselves. Behavior localization is the missing prerequisite step.

## Harness Handbook: three parts

1. **Representation**: organizes implementation knowledge around runtime behavior rather than files. Each behavior links directly to its source code. Three disclosure levels: L1 system overview (architecture, execution model, stages), L2 component overview (roles, inputs/outputs, interactions), L3 unit deep dive (internal logic, state transitions, edge cases, implementation).
2. **Construction pipeline**: static program analysis extracts call graphs and state dependencies; LLM-assisted behavioral structuring groups implementations into behavior declarations with action types (modify, add, remove) and supporting evidence.
3. **Modification workflow (BGPD)**: guides agents from behavior description to relevant implementation in stages, then verifies candidate locations against the current source. Auto-resynchronizes after every non-empty repository diff.

## Results

- Handbook-Assisted planning improves plan-quality win rates across all three judges; gap of 10.0 percentage points on Codex, 13.3 to 26.7 points on Terminus-2.
- Lower planner token cost per request than baseline exploration.
- Largest gains on scattered implementation sites, rarely executed paths, cross-module interactions.
- Project: https://ruhan-wang.github.io/Harness-Handbook/

## Connection to the vault

Extends [[wiki/pages/harness-design]] with a fourth perspective: rather than evaluating whether harness evolution works ([[wiki/sources/arxiv-2607-12227-harness-evaluation]]) or proposing a compositional harness ([[wiki/sources/alex-zhang-harness-2026]]), it attacks the prerequisite problem of finding where to edit. Behavior-centric organization mirrors the comprehension-debt problem ([[wiki/pages/comprehension-debt]]): without it, agents and developers accumulate misunderstanding about where behaviors live.
