---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, benchmark, test-time-learning, experience-reuse, lifelong-learning]
source_path: raw/papers/arxiv-2511.20857.pdf
---

# Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory

**Authors:** Tianxin Wei et al. (UIUC, Google DeepMind)
**Published:** November 2025 | arXiv:2511.20857

## Summary

Evo-Memory introduces a benchmark framework that shifts the evaluation of agent memory from passive conversational recall to active experience reuse. The core insight is that current memory systems "remember what was said but not what was learned" — they retrieve past facts but fail to abstract reusable reasoning strategies for future tasks ([Wei et al., 2025](raw/papers/arxiv-2511.20857.pdf)).

The benchmark structures datasets into sequential task streams spanning both multi-turn goal-oriented tasks (e.g., embodied manipulation) and single-turn reasoning/QA, requiring agents to search, adapt, and evolve their memory after each interaction. Over ten existing memory modules are evaluated under this unified framework, revealing that most systems struggle with genuine experience accumulation.

The paper also contributes two methods: ExpRAG, a baseline for retrieving prior experience, and ReMem, an action–think–memory refine pipeline that tightly couples reasoning, task execution, and memory updates. ReMem demonstrates that explicit memory evolution steps — not just storage and retrieval — are necessary for continual improvement. This benchmark fills a critical gap by providing a standardized way to measure whether agents actually learn from experience over time, as opposed to merely recalling it.
