---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [harness, evaluation, agent, harness-evolution, test-time-scaling, generalization]
source_path: raw/papers/2607.12227.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Rethinking the Evaluation of Harness Evolution for Agents

**Authors:** Yike Wang, Huaisheng Zhu, et al. (AI2, UW) | **arXiv:** 2607.12227 | **Date:** Jul 14, 2026

## Summary

Critiques the evaluation methodology of automatic harness evolution for LLM agents. Identifies two fundamental flaws: (1) harness evolution is an iterative search, so it should be compared with simple task-level search baselines under matched budgets, not just final performance; (2) search and evaluation share the same benchmark, risking **overfitting**. Experiments on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6 show automatic harness evolution **does not consistently outperform** simple test-time scaling and exhibits **limited generalization**.

## Key Arguments

### Flaw 1: Missing Baseline
Harness evolution repeatedly evaluates and revises candidate harnesses using task feedback. This is essentially test-time scaling. Without comparing against simple baselines (parallel sampling, sequential refinement, task-level revision) under comparable feedback and inference budgets, gains may come from search alone, not better harness design.

### Flaw 2: Benchmark Overfitting
Search uses verifier feedback from benchmark tasks, final harness evaluated on the same benchmark. Observed gains may be overfit to the specific task set.

### Results
- GPT-5.4 and Claude Opus 4.6 on Terminal-Bench 2.1
- Harness evolution does not consistently beat test-time scaling
- Evolved harnesses show limited generalization to held-out tasks
- Raises important questions about effectiveness of automatic harness design methods

## Code
Available at https://github.com/rethinking-harness-evolution
