---
type: source
created: 2026-05-05
updated: 2026-06-13
tags: [multi-agent, organization, talent-market, orchestration]
source_path: raw/papers/arxiv-2604.22446.pdf
---

# From Skills to Talent: OneManCompany (OMC)

**Yu, Fu, He, Huang, Ka Yiu, Fang, Luo & Wang** (Huawei Noah's Ark Lab, UCL, Liverpool) — arXiv:2604.22446, Apr 2026

## Summary

Framework che eleva i sistemi multi-agente al livello **organizzativo**: incapsula skills, tools e runtime configurazioni in identità agent portatili chiamate **Talents**, orchestrate tramite interfacce organizzative tipate. Un **Talent Market** community-driven abilita recruiting on-demand.

## Key claims

- **Gap identificato**: manca un layer organizzativo principiato che governa come una forza lavoro di agenti è assemblata, governata e migliorata nel tempo, **decoupled da ciò che i singoli agenti sanno**.
- **Talent = Container**: profili per-employee con skills, performance, configurazioni runtime.
- **E2R tree search (Explore-Execute-Review)**: unifica pianificazione, esecuzione e valutazione in un loop gerarchico con garanzie formali su terminazione e deadlock-freedom.
- **Typed organisational interfaces**: astraggono su backend eterogenei.
- **Org Knowledge**: workflow SOPs editabili e company culture rules che persistono cross-project.
- **Risultati su PRDBench**: 84.67% success rate (+15.48pp vs SOTA). Case studies cross-domain confermano generalità.

## Positioning

Visione ambiziosa di multi-agent systems come organizzazioni auto-organizzanti. Rilevante per architetture di agent orchestration a larga scala.
