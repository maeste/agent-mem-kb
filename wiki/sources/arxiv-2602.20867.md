---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2602.20867.pdf
---

# SoK: Agentic Skills — Beyond Tool Use in LLM Agents

**Authors:** Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu (UTS / CSIRO Data61), 2026.

This systematization-of-knowledge paper argues that the LLM agent field lacks a unifying abstraction for reusable procedural knowledge and introduces "agentic skills" as that abstraction. A skill is formally defined as a 4-tuple S = (C, π, T, R) comprising applicability conditions, an executable policy, termination criteria, and a reusable callable interface — distinguishing skills from atomic tools, one-time plans, and episodic memory (Jiang et al., 2026). The paper maps the full skill lifecycle across seven stages (discovery, practice, distillation, storage, composition, evaluation, update) and proposes two complementary taxonomies: a system-level set of seven design patterns (e.g., metadata-driven progressive disclosure, executable code skills, self-evolving libraries, marketplace distribution) and an orthogonal representation × scope taxonomy covering skill formats (NL, code, policy, hybrid) and operating environments (web, OS, software engineering, robotics). A key contribution is the security and governance analysis, anchored by the ClawHavoc campaign case study in which nearly 1,200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys and cryptocurrency wallets at scale. On evaluation, the authors report benchmark evidence that curated skill libraries can substantially improve agent success rates while self-generated skills may actually degrade performance, underscoring quality-control challenges. The paper concludes with open challenges around robustness, verifiability, and certification of skills for real-world autonomous agents.
