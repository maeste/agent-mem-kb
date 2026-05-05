---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, proactive-retrieval, lifelong-learning, reinforcement-learning, experience-base]
source_path: raw/papers/arxiv-2604.20572.pdf
---

# Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents

**Authors:** Yuxuan Cai, Jie Zhou, Qin Chen, Liang He (East China Normal University, Shanghai AI Laboratory)

ProActAgent addresses two limitations of current lifelong learning agents: passive retrieval (triggered at fixed positions or by external rules) and decoupled online updating (treating textual memory and policy optimization as independent). The framework introduces two components. First, Experience-Enhanced Online Evolution (EXPONEVO) jointly updates textual memory and policy parameters during online interaction, organizing historical interactions into typed repositories — factual memory, episodic memory, and behavioral skills. Second, Proactive Reinforcement Learning-based Retrieval (PROACTRL) models retrieval as an explicit policy action, learning when and what to retrieve via paired-branch process rewards that compare task continuations with and without retrieval at each step. This provides step-level supervision, encouraging retrieval only when it improves outcomes or efficiency. Evaluated on SciWorld, AlfWorld, and StuLife, ProActAgent achieves 73.50% success on SciWorld and 71.28% on AlfWorld while substantially reducing retrieval overhead, and is competitive with proprietary models on StuLife.

**Key claims:**

- Passive retrieval strategies (static initialization, continuous retrieval, LLM-gated) either miss knowledge gaps mid-interaction or cause context overload (Cai et al., 2026).
- Treating retrieval as a learnable policy action — with paired-branch rewards comparing with/without-retrieval continuations — enables adaptive, overhead-efficient memory access.
- Joint evolution of textual memory and policy parameters is essential for effective lifelong adaptation; updating only one side is insufficient.
- Structured experience bases with typed repositories (factual, episodic, behavioral) provide both evidence and actionable guidance for downstream decisions.
