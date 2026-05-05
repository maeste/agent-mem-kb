---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.03088.pdf
---

# SkVM: Revisiting Language VM for Skills across Heterogeneous LLMs and Harnesses

**Authors:** Le Chen, Erhu Feng, Yubin Xia, Haibo Chen (Shanghai Jiao Tong University), 2026.

SkVM tackles the portability and efficiency problem in the agent skill ecosystem by applying classical compiler design principles: skills are treated as code, LLMs as heterogeneous processors. Based on analysis of 118,000 skills from clawhub.ai and skills.sh, the authors find that enabling skills degrades performance on 15% of tasks overall (7% for Opus 4.6, 25% for Qwen3-30B) and yields no improvement on up to 87% of tasks for at least one model, revealing a fundamental mismatch between static skill specifications and variable model capabilities (Chen et al., 2026). SkVM addresses this with a compilation and runtime system: at **compile time**, capability-based compilation extracts 26 primitive capability dimensions, measures model-harness proficiency against them, and adapts skill specifications; environment binding generates setup scripts from implicit dependencies; and concurrency extraction exposes data-, instruction-, and thread-level parallelism to the agent harness. At **runtime**, JIT code solidification materializes high-frequency parameterized script templates into executable code (bypassing LLM parsing), and adaptive recompilation recompiles skills when capability gaps emerge mid-execution. Across eight LLMs and three harnesses, SkVM improves task completion rates by an average of 15.3%, reduces token consumption up to 40%, and achieves 3.2×–50× wall-clock speedups through parallelization and solidification.
