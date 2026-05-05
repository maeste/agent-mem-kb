---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, contextual-bandits, risk, debugging, code-repair]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval

RSCB-MC reframes memory retrieval for coding agents as a risk-sensitive control problem rather than a pure similarity-maximization task. The motivating observation is that superficially similar debugging contexts (e.g., a SQLite lock vs. a stale migration, both producing similar error messages) can share surface-level features while requiring fundamentally different fixes. Unsafe memory injection in such cases doesn't just waste context budget — it actively anchors the agent on incorrect repair strategies.

The system treats non-injection and abstention as first-class safety actions rather than fallback states. It uses a pattern-variant-episode memory schema that separates reusable root-cause patterns from context-specific fix variants and concrete observed episodes, making the controller's decisions more auditable. A fixed 16-feature contextual state captures relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, and token cost.

The reward function deliberately penalizes false-positive memory injection more strongly than missed reuse opportunities. In offline replay evaluation, RSCB-MC achieves 62.5% success with a 0.0% false-positive rate; in a 200-case bounded hot-path validation, it reaches 60.5% proxy success at 331µs p95 decision latency. The central message: for coding-agent memory, the key question is not which memory is most similar, but whether any retrieved memory is safe enough to influence the debugging trajectory.
