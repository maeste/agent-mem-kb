---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [coding-agent, failure-analysis, cli-agent, empirical-study, reliability]
source_path: raw/papers/2607.09510.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Failure as a Process: An Anatomy of CLI Coding Agent Trajectories

**Authors:** Xiangxin Zhao, Han Li, et al. (UCL, Nanjing University) | **arXiv:** 2607.09510 | **Date:** Jul 10, 2026

## Summary

First large-scale empirical study of CLI coding-agent **failure trajectories** as temporal processes rather than final outcomes. Analyzes 1,794 valid trajectories (63,000+ execution steps) from 7 frontier models across 3 scaffolds (OpenHands, MiniSWE, Terminus2) on Terminal-Bench. Derives 14 findings across failure occurrence, root causes, recovery, and cross-system consistency.

## Key Findings

### Failure is Epistemic
Failures are predominantly driven by **epistemic errors** (not knowing something), not execution errors.

### Early Onset, Late Discovery
- Failures typically begin within the **first few execution steps**
- Often remain **hidden until recovery is no longer possible**
- Silent propagation: a single incorrect decision cascades through many subsequent actions

### Implications
Improving coding-agent reliability requires **earlier validation and intervention**, not just final-outcome evaluation. The process-oriented framework (onset, evolution, recovery) reveals failure modes invisible to outcome-only analysis.

## Methodology
- 3,843 total trajectories collected, 1,794 filtered as complete/valid
- 7 frontier models tested
- 3 scaffolds: OpenHands, MiniSWE, Terminus2
- Manual annotation across 63,000+ steps
