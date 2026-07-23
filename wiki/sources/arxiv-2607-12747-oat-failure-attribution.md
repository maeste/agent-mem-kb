---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [failure-attribution, agentic-systems, anomaly-detection, debugging, one-class-learning]
source_path: raw/papers/2607.12747.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Tracing Agentic Failure from the Flow of Success

**Authors:** Samuel Yeh, Yiwen Zhu, Shaleen Deep, Sharon Li (UW-Madison, Microsoft Research) | **arXiv:** 2607.12747 | **Date:** Jul 14, 2026

## Summary

Proposes **OAT** (One-class Anomaly Trajectory), a method for **unsupervised failure attribution** in LLM agentic systems. Trains exclusively on successful trajectories using neural controlled differential equations to model the dynamical pattern of success. At inference, each step in a failure trajectory gets an anomaly score based on deviation from learned dynamics. 200-5000x faster than prompting-based baselines with better F1 scores.

## Problem
When an agentic system fails on a long-horizon task, identifying which of dozens/hundreds of steps went wrong is extremely challenging. Root causes are obscured by compensatory downstream steps. Manual tracing can take hours per trajectory. SOTA reasoning models achieve below 15% accuracy on failure attribution.

## OAT Approach

### Training
- Trains on **only successful trajectories** (no failure labels needed)
- Uses neural CDEs to model temporal dynamics of successful execution in latent space
- Requires as few as 100 successful trajectories

### Inference
- Each step in a failure trajectory assigned anomaly score
- Score = deviation from learned successful dynamics
- Error steps identified as anomalous deviations

## Results
- **200-5000x faster** than prompting-based baselines
- **+20% F1** improvement on in-domain tasks
- **+7% F1** on out-of-distribution tasks
- Eliminates need for costly step-level error annotation on failure data

## Comparison to Prior Work
- Prompting-based: expensive, requires multiple LLM calls per trajectory
- RL post-training: needs step-level error annotations on failures (costly, ambiguous)
- OAT: lightweight, no failure labels, trains on success only
