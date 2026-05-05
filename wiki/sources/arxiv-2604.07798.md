---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, small-language-models, efficiency, retrieval, multi-tier-memory]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# Lightweight LLM Agent Memory with Small Language Models

**Authors:** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, et al. (UESTC, Kyung Hee University, City University of Hong Kong, Oxford)

LightMem proposes decoupling online memory operations from offline consolidation by assigning specialized Small Language Models (SLMs) to each stage, avoiding the latency overhead of repeated large-model calls. The system organizes memory into three tiers: short-term (conversational context), mid-term (reusable interaction summaries), and long-term (consolidated knowledge), with user identifiers enabling multi-user isolation. Online, three SLM modules handle distinct operations — a Controller rewrites queries into intent-conditioned hypothetical queries, a Selector performs metadata-constrained pre-filtering and semantic-consistency re-ranking, and a Writer summarizes interactions into compact mid-term entries. Offline, a large-context model handles long-term abstraction and consolidation. Experiments on LoCoMo show consistent gains across model scales, with an average F1 improvement of ~2.5 over A-MEM, while achieving low median latency (83ms retrieval, 581ms end-to-end).

**Key claims:**

- Existing memory systems face a sharp efficiency–effectiveness trade-off: retrieval-based methods are fast but noisy, LLM-based methods are accurate but slow (Zhang et al., 2026).
- Separating online processing (handled by SLMs) from offline consolidation (handled by larger models) achieves both high accuracy and low latency.
- A two-stage retrieval pipeline — vector-based coarse retrieval followed by semantic consistency re-ranking — substantially reduces retrieval noise.
- Multi-user isolation through identity metadata is essential for practical deployment.
