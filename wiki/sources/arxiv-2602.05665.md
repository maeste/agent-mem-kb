---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, graph-memory, survey, taxonomy, knowledge-graph, self-evolving]
source_path: raw/papers/arxiv-2602.05665.pdf
---

# Graph-based Agent Memory: Taxonomy, Techniques, and Applications

**Authors:** Chang Yang, Chuang Zhou, Yilin Xiao et al. (HK PolyU, Xiamen University, SMU, Jilin University)
**Published:** February 2026 | arXiv:2602.05665

## Summary

This comprehensive survey positions graph-based memory as the frontier paradigm for LLM agent memory systems, arguing that graph structures offer intrinsic advantages over linear, unstructured, or simple key-value storage: natural encoding of relational dependencies, hierarchical organization, and flexible traversal-based reasoning ([Yang et al., 2026](raw/papers/arxiv-2602.05665.pdf)).

The taxonomy spans multiple dimensions: short-term vs. long-term memory, knowledge vs. experience memory, and non-structural vs. structural memory. The paper systematically reviews techniques across the full memory lifecycle — extraction (transforming raw data into graph content), storage (organizing data efficiently), retrieval (finding relevant content for reasoning), and evolution (updating memory over time). Graph variants covered include knowledge graphs, temporal graphs, hypergraphs, hierarchical trees/graphs, and hybrid structures.

The survey catalogs open-source libraries, benchmarks, and application scenarios, and identifies four key motivations for agent memory: personalization, reasoning beyond context windows, self-improvement, and hallucination mitigation. A companion resource repository is maintained at GitHub (Awesome-GraphMemory). The work serves as a useful reference for practitioners choosing between memory architectures and for researchers identifying open problems in the rapidly growing field of graph-based agent memory.
