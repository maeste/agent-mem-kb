---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2603.02176.pdf
---

# AgentSkillOS: Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale

**Authors:** Hao Li, Chunjiang Mu, Jianhao Chen, Siyue Ren, Yiqun Zhang, Lei Bai, Shuyue Hu, Zhiyao Cui (Shanghai AI Lab), 2026.

AgentSkillOS addresses the management and orchestration problem in large-scale agent skill ecosystems, where over 280,000 skills are publicly available as of early 2026. The framework has two stages: **Manage Skills** constructs a hierarchical capability tree by recursively partitioning skills into category nodes, enabling efficient discovery and surfacing non-obvious but functionally relevant skills beyond what pure semantic retrieval yields. **Solve Tasks** retrieves skills via tree exploration, composes them into DAG-based orchestration plans (with three strategy variants), and executes the resulting pipelines with automatic dependency and data-flow management. A key empirical finding is that DAG-based structured orchestration substantially outperforms flat invocation even when both are given the identical oracle skill set, demonstrating that composition — not mere availability — is the critical factor (Li et al., 2026). The authors construct a benchmark of 30 artifact-rich tasks across five categories (data computation, document creation, motion video, visual design, web interaction) with LLM-based pairwise evaluation aggregated via a Bradley–Terry model. Experiments across three ecosystem scales (200, 1K, 200K skills) show AgentSkillOS consistently outperforms vanilla Claude Code invocation and skill-free baselines, with the capability tree effectively approximating oracle-level skill selection.
