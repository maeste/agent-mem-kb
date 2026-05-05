---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, continual-learning, retrieval, transfer-learning]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents

This paper investigates whether external memory truly resolves the continual learning challenge for LLM agents, or merely relocates it. The authors argue that while memory-augmented agents appear to sidestep the stability-plasticity dilemma by avoiding parameter updates, old and new experiences still compete during retrieval under limited context windows — shifting the bottleneck from weight interference to memory access.

Using a (k, v) framework that disentangles experience *representation* (the "value") from experience *organization* (the "key"), the authors conduct controlled sequential-task experiments in ALFWorld and BabyAI. Their central findings reveal that abstraction is critical: raw episodic trajectories tend to hinder adaptation to new tasks, while abstract procedural memories transfer more reliably and can reduce forgetting. Negative transfer concentrates disproportionately on cases the agent cannot yet solve independently, while cases it already handles are comparatively robust.

Perhaps most surprisingly, finer-grained memory organization is not universally beneficial — designs that yield strong forward transfer can simultaneously induce severe forgetting, revealing that the stability-plasticity trade-off can re-emerge through retrieval dynamics. The overall conclusion is that external memory does not resolve the continual-learning problem; it reshapes it into a problem of memory representation and retrieval design.
