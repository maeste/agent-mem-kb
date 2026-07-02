---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [agent-skills, empirical-analysis, skill-ecosystem, skill-safety, marketplace-analysis]
source_path: raw/papers/arxiv-2602.08004.pdf
---

# Agent Skills: A Data-Driven Analysis of Claude Skills for Extending LLM Functionality

**Autori:** George Ling (Bosch Research), Shanshan Zhong, Richard Huang (CMU)  
**Data:** Febbraio 2026 | arXiv:2602.08004

## Sintesi

Analisi data-driven su larga scala di **40,285 skills pubblicamente listate** da un major marketplace di agent skills (skills.sh). Primo studio quantitativo sull'ecosistema delle skills come infrastruttura emergente.

### Dati analizzati

- **40,285 skills** da un marketplace principale
- Periodo: crescita rapida da meta gennaio a inizio febbraio 2026
- OpenClaw (open-source skills application): 25,000+ GitHub stars in un giorno solo a fine gennaio; 170k+ totali

### Risultati chiave

1. **Publication patterns:** la pubblicazione avviene a burst che tracciano gli shift di attenzione della community
2. **Concentrazione del contenuto:** i skills sono fortemente concentrati in **software engineering workflows**
3. **Adoption:** information retrieval e content creation contano una share sostanziale dell'adozione
4. **Supply-demand imbalance:** pronunciato squilibrio tra categorie
5. **Length distribution:** la maggior parte dei skills rimane entro tipici prompt budgets nonostante distribuzione heavy-tailed
6. **Ecosystem homogeneity:** diffusa redundanza a livello di intent
7. **Safety risks:** skills che abilitano azioni state-changing o system-level

## Claim chiave

- L'ecosistema delle skills mostra forte omogeneita' con widespread intent-level redundancy [[wiki/sources/xu-2026-agent-skills-survey.md]]
- I safety risks non sono teorici: esistono skills pubblici che abilitano azioni system-level
- La supply-demand imbalance suggerisce opportunita' sia per creatori che per piattaforme

## Posizione nelvault

Analisi empirica complementare al survey Xu & Yan 2026. Fornisce dati quantitativi reali sullo stato dell'ecosistema skills.
