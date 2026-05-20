---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [multi-agent, organization, talent-market, orchestration]
source_path: raw/papers/arxiv-2604.22446.pdf
---

# From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

**Autori:** Zhengxu Yu, Yu Fu, Zhiyuan He, Yuxuan Huang, Lee Ka Yiu, Meng Fang, Weilin Luo, Jun Wang (Huawei Noah's Ark Lab, UCL, U. Liverpool)
**arXiv:** 2604.22446 (apr 2026) | **Web:** one-man-company.com

## Summary

OneManCompany (OMC) eleva i sistemi multi-agent al livello **organizzativo**: introduce un layer di governance che assembla, governa e migliora una forza lavoro di agenti, decoupled da ciò che i singoli agenti sanno.

## Architettura

- **Talents**: identità agenti portatili che incapsulano skills, tools e runtime configurations
- **Talent Market**: community-driven marketplace per on-demand recruitment, chiude capability gaps dinamicamente
- **E2R Tree Search (Explore-Execute-Review)**: loop gerarchico unificato che combina planning (top-down decomposition), execution, e evaluation (bottom-up aggregation). Garantisce termination e deadlock freedom.
- **Org Knowledge**: knowledge level organizzativo con workflow SOPs editabili e company culture rules che persistono cross-project

## Risultati

- PRDBench: **84.67%** success rate (+15.48pp vs SOTA)
- Cross-domain case studies per generalità

## Relazione con altri lavori

- Complementare a [[wiki/sources/arxiv-2604.24594]] (SRA): OMC gestisce *chi* fa cosa, SRA gestisce *come* recuperare skill
- Si collega a [[wiki/sources/arxiv-2604.16911]] (Skilldex) sul tema di packaging/distribuzione skill
- Organizational layer è unico nel vault; rilevante per deployment multi-agent production
