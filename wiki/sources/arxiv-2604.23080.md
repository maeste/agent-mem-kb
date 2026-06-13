---
type: source
created: 2026-05-05
updated: 2026-06-13
tags: [multi-agent, discovery, distributed, p2p, churn]
source_path: raw/papers/arxiv-2604.23080.pdf
---

# Usable Agent Discovery for Decentralized AI Systems

**Dazzi, Carlini, Mordacchini & Urso** (UniPisa, CNR) — arXiv:2604.23080, Apr 2026

## Summary

Studia la **scoperta decentralizzata di agenti** in infrastrutture distribuite con due livelli di churn: node-level (fallimenti, partenze) e agent-level (lifecycles demand-driven con stati warm/cold). Compara overlay strutturati (Kademlia) vs gossip-based (Cyclon+Vicinity) sotto quattro regimi.

## Key claims

- **Due fonti di instabilità distinte**: node-level churn (infrastrutturale) e agent-level churn (demand-driven cooling/riattivazione) stressano la scoperta in modi diversi.
- **Agenti definiti da skills** (come in AGNTCY): la query di discovery targetta le capabilities, non i nodi.
- **Il target non è un nodo raggiungibile ma un *usable execution target***: un host può essere up ma l'agente richiesto cold/suspended.
- **Risultati sperimentali**:
  - Overlay strutturati (Kademlia): più robusti ed efficienti in regimi stabili e node-churn.
  - Gossip-based (Cyclon+Vicinity): competitivi e più veloci quando la *readiness* domina.
  - Nessun vincitore universale: il design ottimale dipende dalle condizioni operative.

## Positioning

Lavoro di sistemi distribuiti rilevante per architetture multi-agenti su larga scala. Non riguarda direttamente la memoria ma l'organizzazione e discovery di agenti con skills.
