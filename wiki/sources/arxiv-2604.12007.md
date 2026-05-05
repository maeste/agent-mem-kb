---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, forgetting, memory-governance, staleness, outcome-feedback]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Author:** Baris Simsek

This paper introduces Memory Worth (MW), a lightweight per-memory signal for memory quality governance in LLM agents. MW uses two scalar counters per memory unit to track how often a memory co-occurs with successful versus failed task outcomes. The author proves that MW converges almost surely to the conditional success probability p+(m) — the probability of task success given that memory m is retrieved — under a stationary retrieval regime with a minimum exploration condition. Crucially, p+(m) is an associational (not causal) measure; it tracks outcome co-occurrence rather than causal contribution, which the author argues is still a useful operational signal. In a controlled synthetic environment with known ground-truth utility, MW achieves a Spearman rank-correlation of ρ = 0.89 ± 0.02 with true memory utilities after 10,000 episodes, compared to ρ = 0.00 for static systems. A retrieval-realistic micro-experiment with standard embedding retrieval (all-MiniLM-L6-v2) confirms stale memories cross the low-value threshold while specialist memories remain high-value.

**Key claims:**

- Write-time importance scores are static and inadequate for tracking how memory quality evolves as task distributions shift (Simsek, 2026).
- A simple two-counter statistic per memory, updated from episode outcomes, suffices for staleness detection, retrieval suppression, and deprecation.
- MW converges almost surely to the post-retrieval conditional success probability under mild assumptions.
- The primitive requires no architectural changes beyond logging retrievals and episode outcomes, making it easily composable with existing memory architectures.
