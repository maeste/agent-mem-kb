---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.24594.pdf
---

# Skill Retrieval Augmentation for Agentic AI (SRA)

Su, Long, Ai, Tang, Wang, Tu, Liu (Tsinghua University), April 2026.

This paper formulates Skill Retrieval Augmentation (SRA) as a new paradigm for scaling agent capabilities beyond the context-window limits of explicit in-context skill injection. Rather than enumerating all available skills in the prompt, SRA treats skills as entries in a large external corpus and requires agents to dynamically retrieve, incorporate, and apply relevant skills on demand. The authors construct SRA-Bench, the first benchmark for decomposed evaluation of the full SRA pipeline across three stages: skill retrieval, skill incorporation (whether the agent correctly identifies useful skills among retrieved candidates), and end-task execution. SRA-Bench contains 5,400 capability-intensive test instances with 636 manually constructed gold skills mixed into a corpus of 26,262 skills. Key findings include: even a simple single-skill retrieval pipeline improves strong LLM agents over skill-free baselines; however, a fundamental bottleneck exists in skill incorporation — current agents load skills at similar rates regardless of whether a gold skill was retrieved or whether the task actually requires external capabilities. The authors argue SRA is distinct from classical RAG because retrieved items are executable capabilities (augmenting functional competence) rather than declarative knowledge (grounding generation). The paper positions skill incorporation — not retrieval — as the critical unsolved problem for scalable skill augmentation.
