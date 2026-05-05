---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, survey, retrieval, evaluation, long-term-memory]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Author:** Pengfei Du (Hong Kong Research Institute of Technology)

This comprehensive survey (covering 2022–early 2026) formalizes agent memory as a write–manage–read loop coupled with perception and action, organized along three dimensions: temporal scope, representational substrate, and control policy. Du identifies five mechanism families: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, and policy-learned management. On the evaluation side, the survey traces the shift from static recall benchmarks to multi-session agentic tests that interleave memory with decision-making, analyzing four recent benchmarks that expose persistent gaps in current systems. The paper surveys applications where memory is the differentiating factor — personal assistants, coding agents, open-world games, scientific reasoning, and multi-agent teamwork — and addresses practical engineering concerns including write-path filtering, contradiction handling, latency budgets, and privacy governance. Open challenges identified include continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, and multimodal embodied memory.

**Key claims:**

- Memory transforms a stateless LLM into a self-evolving agent that accumulates knowledge, avoids repeating mistakes, and develops behavioral patterns (Du, 2026).
- A write–manage–read loop formalism provides a unifying framework for understanding diverse memory architectures.
- Current evaluation benchmarks remain insufficient; multi-session agentic tests are needed to expose real memory-reasoning gaps.
- Learned forgetting and privacy governance are underexplored but critical for real-world deployment.
