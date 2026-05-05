---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, multi-agent, adaptive-retrieval, memory-consistency, long-term-memory]
source_path: raw/papers/arxiv-2601.20352.pdf
---

# AMA: Adaptive Memory via Multi-Agent Collaboration

**Authors:** Weiquan Huang, Zixuan Wang et al. (HKUST-Guangzhou, Shandong University, NTU, SUSTech)
**Published:** January 2026 | arXiv:2601.20352

## Summary

AMA addresses two persistent problems in external memory systems: the mismatch between fixed storage granularity and task-specific retrieval needs, and the unchecked accumulation of inconsistencies over time. Rather than relying on a single memory controller, AMA decomposes the memory lifecycle across four coordinated agents with distinct roles ([Huang et al., 2026](raw/papers/arxiv-2601.20352.pdf)).

The Constructor transforms raw dialogue into a hierarchical memory with three granularity levels (Raw Text, Fact Knowledge, Episode Memory). The Retriever dynamically routes queries to the appropriate granularity based on reasoning demands. The Judge acts as a logic auditor, checking relevance and detecting inconsistencies. When conflicts are found, the Refresher performs targeted updates or removes stale entries. This separation of concerns prevents the objective conflicts that plague monolithic memory controllers.

Evaluated on challenging long-context benchmarks, AMA significantly outperforms prior state-of-the-art while reducing token consumption by approximately 80% compared to full-context methods. The Refresher component is particularly impactful, enabling nearly 90% accuracy in knowledge update scenarios. The work demonstrates that multi-agent decomposition of memory management — with explicit consistency verification — outperforms both static retrieval paradigms and single-agent memory controllers.
