---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [agent-skills, data-driven-analysis, ecosystem-analysis, skill-marketplace, safety, homogeneity]
source_path: raw/papers/arxiv-2602.08004.pdf
---

# Agent Skills: A Data-Driven Analysis of Claude Skills

**Ling, Zhong, Huang** (Bosch Research, CMU) — arXiv:2602.08004, Feb 2026

## Summary

Analisi data-driven su larga scala di **40,285 skills pubblicamente listate** da un marketplace principale di agent skills, esaminando tipi disponibili, pattern di adozione e rischi.

## Claim principali

- **Dataset**: 40,285 skills da un marketplace principale analizzate con metodi quantitativi [[raw/papers/arxiv-2602.08004.pdf]].
- **Pattern di pubblicazione**: la pubblicazione avviene a short bursts che trackano shift nell'attenzione della community. Crescita rapida: >40,000 skills by early Feb 2026; OpenClaw >170K GitHub stars [[raw/papers/arxiv-2602.08004.pdf]].
- **Concentrazione del contenuto**: skill content è fortemente concentrato in software engineering workflows; information retrieval e content creation contano una share sostanziale di adozione [[raw/papers/arxiv-2602.08004.pdf]].
- **Supply-demand imbalance**: pronunciato squilibrio tra offerta e domanda across categories [[raw/papers/arxiv-2602.08004.pdf]].
- **Dimensione**: la maggior parte delle skills rimane dentro tipici prompt budgets nonostante heavy-tailed length distribution [[raw/papers/arxiv-2602.08004.pdf]].
- **Ecosistema omogeneo**: widespread intent-level redundancy (molte skills fanno la stessa cosa), forte omogeneità dell'ecosistema [[raw/papers/arxiv-2602.08004.pdf]].
- **Safety risks**: skills che abilitano state-changing o system-level actions identificati. Rischi non-triviali per la sicurezza [[raw/papers/arxiv-2602.08004.pdf]].

## Posizione nel dibattito

Analisi empirica complementare al survey teorico di Xu & Yan (arxiv-2602.12430). Mentre Xu&Yan propongono framework e taxonomy, Ling et al. misurano cosa esiste realmente nell'ecosistema. I dati su omogeneità e safety risks sono actionabili per chi progetta skill marketplaces.
