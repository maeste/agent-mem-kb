---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, tool-calling, short-term-memory, context-management, mcp]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling

**Authors:** Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah, Pradeep Honaganahalli Basavaraju, James A. Burke (PwC)
**Published:** July 2025 | arXiv:2507.21428

## Summary

MemTool addresses a specific but critical gap in LLM agent memory: managing dynamically discovered tools and MCP server contexts across multi-turn conversations. As agents discover and add tools to their context window, the working memory fills up, yet most prior work focuses on compressing conversational history rather than evicting no-longer-needed tools.

The framework proposes three architectural modes: (1) Autonomous Agent Mode, where the LLM independently decides which tools to keep or discard; (2) Workflow Mode, which applies deterministic removal rules without LLM autonomy; and (3) Hybrid Mode, combining both approaches. Evaluated across 13+ LLMs on the ScaleMCP benchmark over 100 consecutive user interactions, the results show a stark capability divide — reasoning models (GPT-4 class) achieve 90–94% tool removal efficiency in autonomous mode, while medium-sized models drop to 0–60% ([Lumer et al., 2025](raw/papers/arxiv-2507.21428.pdf)). Workflow and Hybrid modes provide more consistent performance across model sizes, while Autonomous and Hybrid modes deliver better task completion accuracy.

The work provides practical guidance for practitioners: smaller models benefit from deterministic tool eviction, while stronger reasoners can safely self-manage their tool context, and hybrid approaches offer the best balance for production deployments.
