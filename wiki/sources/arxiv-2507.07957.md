---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, multi-agent, multimodal, episodic-memory, personalization]
source_path: raw/papers/arxiv-2507.07957.pdf
---

# MIRIX: Multi-Agent Memory System for LLM-Based Agents

**Authors:** Yu Wang, Xi Chen (MIRIX AI)
**Published:** July 2025 | arXiv:2507.07957

## Summary

MIRIX is a modular, multi-agent memory architecture that organizes agent memory into six specialized types inspired by human cognition: Core, Episodic, Semantic, Procedural, Resource, and Knowledge Vault. Each type has distinct internal structure (e.g., episodic entries include summaries and details), and a dedicated Memory Manager agent controls it, with a Meta Memory Manager handling task routing. An additional Chat Agent demonstrates end-to-end interaction with the memory system.

The system supports multimodal input including high-resolution screenshots, addressing a major gap in existing text-only memory approaches. MIRIX achieves 35% higher accuracy than RAG baselines on a novel ScreenshotVQA benchmark (5K–20K screenshots per sequence) while cutting storage by 99.9%. On the LOCOMO long-form conversation benchmark, it reaches 85.4% accuracy — 8 percentage points above the prior best ([Wang & Chen, 2025](raw/papers/arxiv-2507.07957.pdf)).

Key design choices include an Active Retrieval mechanism where the agent generates a topic before answering, and multiple retrieval tools for different situations. A packaged application captures screen activity every 1.5 seconds and builds personalized memory in real time with local storage for privacy.
