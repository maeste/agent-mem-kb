---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, multimodal, visual-retrieval, long-horizon]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

OCR-Memory proposes a novel approach to the agent memory bottleneck: instead of compressing or truncating interaction histories to fit within text-based context budgets, it encodes complete trajectories as images. The key insight is that visual tokens consume substantially fewer context slots than raw text while preserving full fidelity of the original information, enabling retention of arbitrarily long agent histories with minimal prompt overhead.

The framework employs a "locate-and-transcribe" retrieval paradigm. Historical trajectories are rendered into images annotated with unique visual anchors (indexed bounding boxes). When the agent needs context, an optical retriever scans these images to predict relevant segment indexes rather than generating free-form text, then deterministically fetches the corresponding verbatim text from an external store. This decoupling of understanding from evidence generation significantly reduces hallucination risk.

An age-aware adaptive-resolution scheme mimics human memory's vivid-to-fuzzy property: older trajectory images are progressively stored as lower-resolution thumbnails to manage token cost, while an "active-recall" up-sampling mechanism restores full fidelity when faded memories are identified as relevant. Evaluated on Mind2Web and AppWorld benchmarks, OCR-Memory consistently outperforms existing baselines under strict token budgets, establishing a new state-of-the-art for long-horizon agent tasks.
