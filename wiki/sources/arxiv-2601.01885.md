---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, reinforcement-learning, unified-memory, long-term-memory, short-term-memory, grpo]
source_path: raw/papers/arxiv-2601.01885.pdf
---

# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management

**Authors:** Yi Yu, Liuyi Yao et al. (Wuhan University, Alibaba Group)
**Published:** January 2026 | arXiv:2601.01885

## Summary

Agentic Memory (AgeMem) unifies long-term and short-term memory management into a single learned policy, treating memory operations (store, retrieve, update, summarize, discard) as tool-based actions the LLM agent can invoke autonomously. This directly addresses the fragmented status quo where LTM and STM are designed, optimized, and deployed as separate modules with heuristic-based controllers ([Yu et al., 2026](raw/papers/arxiv-2601.01885.pdf)).

Training the unified policy is challenging because memory operations yield sparse and discontinuous rewards — writing a memory now may only help many steps later. The authors propose a three-stage progressive reinforcement learning strategy with a step-wise variant of GRPO (Group Relative Policy Optimization) to handle this credit assignment problem. Experiments across five long-horizon benchmarks show consistent improvements over strong memory-augmented baselines across multiple LLM backbones.

A notable finding is that end-to-end learned memory management produces both higher task performance and higher-quality long-term memory compared to heuristic approaches, suggesting that the agent's ability to jointly reason about what to remember and what to forget is a learned skill rather than one that can be fully specified through rules. This work provides evidence that treating memory as an integral part of the agent's action space, rather than an external system, is a productive research direction.
