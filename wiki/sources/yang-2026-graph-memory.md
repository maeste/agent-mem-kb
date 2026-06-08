---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [graph-memory, survey, memory-taxonomy, agent-memory]
source_path: raw/papers/arxiv-2602.05665.pdf
---

# Graph-based Agent Memory: Taxonomy, Techniques, and Applications

**Chang Yang et al.** (HK PolyU, XMU, SMU, JLU, HKUST) — arXiv:2602.05665, Feb 2026

## Summary

Survey comprehensivo sulla memoria per agenti LLM dalla prospettiva dei grafi. Il grafo emerge come struttura potente per la memoria agente grazie alla capacità intrinseca di modellare dipendenze relazionali, organizzare informazioni gerarchiche e supportare retrieval efficiente.

Contributi principali:
1. **Taxonomia della memoria agente**: short-term vs long-term, knowledge vs experience, non-structural vs structural
2. **Tecniche del ciclo di vita**: extraction (dati → contenuti), storage (organizzazione efficiente), retrieval (recupero per reasoning), evolution (aggiornamento contenuti)
3. **Librerie open-source e benchmark** per sviluppo e valutazione
4. **Scenari applicativi** e direzioni di ricerca future

Risorse raccolte in https://github.com/DEEP-PolyU/Awesome-GraphMemory. La survey copre work dal 2022 all'inizio 2026.

## Key claims
- I grafi sono particolarmente adatti per modellare dipendenze relazionali nella memoria ([§Abstract](raw/papers/arxiv-2602.05665.pdf))
- Il ciclo di vita della memoria comprende 4 fasi distinte ([§3](raw/papers/arxiv-2602.05665.pdf))
- Esistono gap significativi nella valutazione della memoria self-evolving ([§7](raw/papers/arxiv-2602.05665.pdf))

## Connections
- [[wiki/sources/yang-2026-graph-memory]] — fonte primaria
- [[wiki/pages/graph-memory]] — uso di grafi per memoria agente
