---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, causal-reasoning, retrieval, knowledge-graph]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents

**Authors:** Xiaohui Zhang, Zequn Sun, Chengyuan Yang, Yaqin Jin, Yazhong Zhang, Wei Hu (Nanjing University, Alibaba Group)

ActMem addresses a core limitation of existing LLM agent memory systems: they act as passive recorders that retrieve past information without understanding its deeper implications for current decision-making. The framework transforms unstructured dialogue history into a structured causal and semantic graph, enabling agents to perform active causal reasoning over their memories. By leveraging counterfactual reasoning and commonsense completion, ActMem can deduce implicit constraints and resolve conflicts between past states and current intentions — for example, inferring that a user buying a toxic houseplant conflicts with having a teething puppy, even though the two topics have no surface-level semantic overlap. The authors introduce ActMemEval, a benchmark designed to evaluate agent reasoning in logic-driven memory scenarios rather than simple fact retrieval. Experiments show ActMem significantly outperforms baselines on complex, memory-dependent tasks, establishing causal reasoning over memory as a necessary capability beyond standard RAG-based retrieval.

**Key claims:**

- Passive memory retrieval is insufficient for agents that must reason about conflicts between past states and current goals (Zhang et al., 2026).
- Structured causal-semantic graphs with counterfactual reasoning enable agents to detect latent conflicts that standard similarity-based retrieval misses.
- Existing memory benchmarks focus too narrowly on fact recall; ActMemEval evaluates logic-driven reasoning scenarios requiring memory integration.
