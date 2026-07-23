---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [routing, multi-model, diversity, robustness, lm-societies]
source_path: raw/papers/arxiv-2607.09197.pdf
ingested: 2026-W30 (Sat-Sat)
---

# When is Routing Meaningful? Diversity and Robustness in LM Societies

**Fantine Huot, Michael Kaisers, Mirella Lapata** (Google DeepMind) — arXiv:2607.09197, 10 lug 2026 [[raw/papers/arxiv-2607.09197.pdf]]

Studio su quando le politiche di routing tra modelli LM sono "meaningful", introducendo metriche per diversita comportamentale e robustezza del routing.

## Tesi

Il routing viene valutato quasi esclusivamente su accuracy e costo, ma due proprieta strutturali determinano se e meaningful:
1. La societa di attori deve essere **comportamentalmente differenziata** (altrimenti routing e vacuo)
2. La policy di routing deve essere **robusta**: varianti semanticamente equivalenti devono andare allo stesso attore [[raw/papers/arxiv-2607.09197.pdf]]

High task accuracy e compatibile con violare entrambe: un router puo operare su societa redundanti o assegnare query inconsistentemente.

## Metriche proposte

### Hierarchic Social Entropy (HSE) adattata per LM societies
- Misura diversita comportamentale da output dei modelli (non dai parametri), usando cosine similarity su behavioural vectors
- Sostituisce Euclidean inter-agent distance dell'HSE originale (robotics)
- Prima applicazione di metriche di diversita comportamentale all'analisi di routing LM

### Perturbation-based robustness metric (rho)
- Misura se query semanticamente equivalenti (con perturbazioni superficiali) sono assegnate allo stesso attore
- Five-level perturbation taxonomy: character-level noise, lexical substitution, syntactic transformation, paraphrase, semantic shift

## Risultati chiave

- **Specialist societies** (synthetic purpose-designed experts) raggiungono HSE sostanzialmente piu alto di pool di modelli real-world di dimensione equivalente: la diversita comportamentale nei pool reali e **minore di quanto si assuma**
- **Strong diminishing returns**: <10 agenti catturano maggior parte della diversita disponibile in EmbedLLM; 4 in RouterBench — euristica pratica per society design
- **HSE non implica robustness**: KNN routers raggiungono best accuracy su specialist societies ma worst robustness; prompted routing rimane stabile across tutti i livelli HSE e tipi di perturbazione
- Accuracy e meaningfulness possono **divergere sharpamente**
