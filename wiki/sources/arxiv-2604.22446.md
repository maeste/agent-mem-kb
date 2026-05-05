---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.22446.pdf
---

# From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

Yu, Fu, He, Huang, Lee Ka Yiu, Fang, Luo, Wang (Huawei Noah's Ark Lab, UCL, University of Liverpool), April 2026.

OneManCompany (OMC) proposes an organisational layer for multi-agent systems that sits above individual agent skills and below task execution, governing how a workforce of heterogeneous agents is assembled, coordinated, and improved over time. The framework introduces *Talents* — portable agent identities that encapsulate skills, tools, and runtime configurations — orchestrated through typed organisational interfaces that abstract over heterogeneous backends. A community-driven *Talent Market* enables on-demand recruitment to close capability gaps dynamically. Organisational decision-making is operationalised through an *Explore-Execute-Review (E²R) tree search* that unifies planning, execution, and evaluation in a single hierarchical loop: tasks decompose top-down into accountable units, and outcomes aggregate bottom-up to drive systematic review. The authors claim formal guarantees on termination and deadlock freedom. Evaluated on PRDBench, OMC achieves an 84.67% success rate, surpassing the prior state of the art by 15.48 percentage points. The core argument is that the field needs to move from skills ("what can an agent do?") through multi-agent interaction ("how do agents interact?") to an organisation-level abstraction ("how should a workforce of agents be structured and managed?").
