---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [discovery, distributed-systems, multi-agent, p2p, infrastructure]
source_path: raw/papers/arxiv-2604.23080.pdf
---

# Usable Agent Discovery for Decentralized AI Systems

**Autori:** Patrizio Dazzi, Emanuele Carlini, Matteo Mordacchini, Saul Urso (UniPisa, CNR Italy)
**arXiv:** 2604.23080 (apr 2026)

## Summary

Studio su discovery decentralizzato di agenti in infrastrutture distribuite a larga scala. Il problema: discovery deve trovare non solo il nodo giusto ma un **target eseguibile usabile** (agent possono essere warm, cold, o off). Due livelli di churn interagenti:

1. **Node-level churn**: failure, departures, recoveries dei nodi fisici
2. **Agent-level churn**: lifecycle demand-driven (warm ↔ cold transitions)

## Confronto overlay

- **Structured (Kademlia)**: lookup a bassa latenza, stato routing compatto. Più robusto ed efficiente in regimi stabili e node-churn.
- **Gossip-based (Cyclon+Vicinity)**: overhead messaging più alto, degrada più graceful sotto change. Può essere più veloce quando la readiness domina.

## Metriche chiave

Introduce **Useful Availability UΔ(q,a)**: probabilità che una route scoperta produca un servizio entro un deadline significativo. Separa efficienza (latenza), resilienza (success rate), e readiness (stato agent).

## Regime map empirico

4 regimi studiati: stable, node-churn-only, agent-cooling-only, combined. Nessun overlay è universalmente superiore; la scelta dipende dalle condizioni operative.

## Relazione con altri lavori

- Infrastrutturale rispetto ai paper core del vault; rilevante per deployment di sistemi multi-agent a scala
- Si collega al tema skill-based discovery di [[wiki/sources/arxiv-2604.24594]] (SRA) e [[wiki/sources/arxiv-2604.24026]] (SSL) ma a livello infrastrutturale invece che di rappresentazione
