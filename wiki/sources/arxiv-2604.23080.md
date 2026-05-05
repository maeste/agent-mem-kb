---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.23080.pdf
---

# Usable Agent Discovery for Decentralized AI Systems

Dazzi, Carlini, Mordacchini, Urso (University of Pisa, CNR Italy), April 2026.

This paper studies decentralized agent discovery in large-scale distributed agentic systems where multiple agents share physical hosts and are discovered via peer-to-peer overlays. The key insight is that discovery must handle two distinct churn dimensions simultaneously: *node-level churn* (host failures and departures affecting all agents on a node) and *agent-level churn* (demand-driven activation, deactivation, and warm/cold state transitions of individual agents). The authors compare structured overlays (Kademlia DHT) against gossip-based overlays (Cyclon+Vicinity) across four regimes: stable, node-churn-only, agent-cooling-only, and combined. Their empirical regime map shows that structured overlays are more robust and efficient in stable and node-churn regimes, while gossip-based overlays remain competitive and can be faster when agent readiness dominates the workload. The contribution is primarily analytical rather than constructing a new system — it provides a system model with warm/cold agent states, observables separating efficiency, resilience, and service readiness, and practical guidance on overlay choice based on operating conditions. The work is positioned within the AGNTCY framework for skill-based agent discovery.
