---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [memory, agents, llm, forgetting, neuro-inspired, privacy, security, hippocampal-theory]
source_path: raw/papers/arxiv-2604.20300.pdf
---

# FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

**Authors:** Yingjie Gu, Wenjian Xiong, Liqiang Wang, Pengcheng Ren, et al. (China Mobile)

FSFM draws on cognitive neuroscience — specifically hippocampal memory indexing/consolidation theory and the Ebbinghaus forgetting curve — to argue that selective forgetting is as crucial as memory retention for LLM agents operating in resource-constrained environments. The framework establishes a taxonomy of four forgetting mechanism categories: passive decay-based, active deletion-based, safety-triggered, and adaptive reinforcement-based approaches. The paper argues forgetting serves three key dimensions: computational and storage efficiency through intelligent memory pruning, enhanced content quality by dynamically updating outdated preferences and context, and robust security through active removal of malicious inputs, sensitive data, and privacy-compromising content. Controlled experiments demonstrate significant improvements in access efficiency (+8.49%), content quality (+29.2% signal-to-noise ratio), and security (100% elimination of security risks). The work bridges cognitive neuroscience concepts and AI systems, addressing ethical considerations and regulatory compliance including GDPR's "right to be forgotten."

**Key claims:**

- Treating memory as an ever-expanding repository leads to storage bloat, declining quality from redundant information, security vulnerabilities, and privacy conflicts (Gu et al., 2026).
- Biologically-inspired forgetting mechanisms (hippocampal indexing, Ebbinghaus decay curves) provide principled foundations for agent memory pruning.
- Four categories of forgetting — passive decay, active deletion, safety-triggered, and adaptive reinforcement — cover the full spectrum of practical needs.
- Selective forgetting improves efficiency, memory quality, and security simultaneously, with empirical gains of +8.49% access efficiency and +29.2% signal-to-noise ratio.
