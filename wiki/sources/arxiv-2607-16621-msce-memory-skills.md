---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [memory, skills, agent, co-evolution, long-horizon, lifelong-learning]
source_path: raw/papers/2607.16621.pdf
ingested: 2026-W30 (Sat-Sat)
---

# From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents

**Authors:** Bo Tang, Yang Zhang, et al. (MemTensor, USTC, HK PolyU) | **arXiv:** 2607.16621 | **Date:** Jul 18, 2026

## Summary

Proposes **MSCE** (Memory-Skill Co-Evolution), a training-free framework that converts agent experience into executable skills rather than treating memory as passive context. Organizes experience into three levels (L1 trace, L2 policy, L3 environmental cognition) and crystallizes evidence-backed L2 policies into callable skills with triggers, boundaries, verification rules, and reliability estimates. Outperforms SOTA on EvoAgentBench and LoCoMo.

## Problem
Existing memory systems retrieve prior traces as **passive context** rather than converting them into operational capabilities. Repeated plugin-installation traces still get re-reasoned from scratch. Terminal feedback is sparse and delayed, making step-level credit assignment uncertain.

## MSCE Architecture

### Three Memory Levels
- **L1 Trace Memory**: grounded step-level evidence
- **L2 Policy Memory**: recurring procedural patterns induced from cross-episode traces
- **L3 Environmental Cognition**: declarative knowledge about environment structure and constraints

### Skill Crystallization
L2 policies become skills when they:
- Retain supporting evidence links
- Exhibit positive estimated gain
- Remain consistent with trigger, procedure, and applicability boundary

Skills include: evidence anchors, applicability boundaries, decision guidance, verification rules, reliability estimates.

### Reflection-Weighted Value Backfilling
Propagates sparse terminal feedback through dense local self-reflections to produce evidence-calibrated trace values. This governs both memory evolution and skill lifecycle.

## Results
- Outperforms SOTA skill-augmented and memory-driven baselines on EvoAgentBench and LoCoMo
- Strong cross-domain transferability
- Lifelong evolution capabilities
- Code: https://github.com/MemTensor/MemOS
