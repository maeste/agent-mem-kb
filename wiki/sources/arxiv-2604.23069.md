---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, context-management, dependency-graph, tool-use]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Selective and Dependency-Structured Memory Construction for LLM Agents

ContextWeaver addresses a gap in how LLM agents manage growing interaction histories: existing context management methods like sliding windows and prompt compression select content based on recency or semantic similarity, but fail to preserve the causal and logical dependencies between reasoning steps. When these dependencies are lost, agents break ongoing plans, repeat exploration, or produce inconsistent steps.

The framework organizes an agent's interaction trace into a dependency graph where each reasoning step is linked to the earlier steps it relies on (tool outputs, decisions, intermediate hypotheses). Three core components enable this: (1) a dependency-based construction module that identifies parent relationships between steps, (2) compact dependency summarization that condenses root-to-current-step reasoning paths into reusable units, and (3) a lightweight validation layer that incorporates execution feedback to filter out unreliable nodes.

Evaluated on SWE-Bench Verified and Lite, ContextWeaver improves pass@1 over sliding-window baselines while reducing both reasoning steps and token usage. The key insight is that modeling logical dependencies — not just recency or similarity — provides a stable and scalable memory mechanism for tool-using LLM agents, complementing static code analysis by capturing the dynamic reasoning progression that static approaches miss.
