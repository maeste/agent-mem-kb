---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, semantic-memory, retrieval, information-theory]
source_path: raw/papers/arxiv-2604.22085.pdf
---

# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

Memanto proposes a vector-only agentic memory layer that challenges the assumption that knowledge graph complexity is necessary for high-fidelity agent memory. The system uses a typed semantic memory schema with 13 predefined memory categories (e.g., episodic, semantic, procedural), combined with an automated conflict resolution mechanism and temporal versioning, all powered by an information-theoretic search engine that provides deterministic retrieval in under 90ms with zero ingestion delay.

The paper introduces the concept of the "Memory Tax" — the cumulative computational overhead of ingestion, retrieval, and schema management in hybrid graph+vector architectures. The authors argue this tax yields diminishing returns compared to optimized semantic retrieval, especially under deterministic exact-match search rather than approximate nearest neighbor methods.

Benchmarked on LongMemEval and LoCoMo, Memanto achieves 89.8% and 87.1% accuracy respectively, surpassing all evaluated hybrid and vector-based systems while requiring only a single retrieval query and incurring no ingestion cost. A five-stage progressive ablation study quantifies the contribution of each architectural component. The authors propose six design principles for production-ready agentic memory systems derived from real-world deployment feedback.
