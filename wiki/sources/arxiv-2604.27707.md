---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, cognitive-science, generalization, security]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

This position paper argues that current agentic memory systems — vector stores, RAG, scratchpads, and context-window management — implement lookup, not memory. The authors frame treating retrieval as memory as a category error with provable consequences for agent capability, long-term learning, and security.

The core distinction is between exemplar-based cognition (generalizing by similarity to stored cases) and rule-based cognition (applying abstract principles to novel inputs). Drawing on Complementary Learning Systems theory from neuroscience, the authors note that biological intelligence pairs fast hippocampal exemplar storage with slow neocortical weight consolidation, but current AI agents implement only the first half. The model weights remain identical before and after an agent's "experience."

Four formal claims are advanced: (1) agentic memory cannot extrapolate to compositionally novel situations, (2) a Generalization Gap theorem proves retrieval-based memory has a provably lower ceiling than weight-based memory regardless of context size, (3) agents cannot develop expertise through C-engineering alone, and (4) agentic memory structurally converts transient prompt injections into persistent compromise. The paper closes with a co-existence architecture proposal arguing that episodic traces belong in external stores (fast, temporary), skills can bridge context and weights, and abstract rules must be encoded in weights (slow, generalizable).
