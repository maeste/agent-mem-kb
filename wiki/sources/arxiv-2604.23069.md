---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [dependency-graph, context-management, memory-structure, swe-bench, agent-reasoning]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Selective and Dependency-Structured Memory Construction

**Autori:** Yating Wu (UT Austin), Yuhao Zhang et al. (AWS AI Labs) | **arXiv:** 2604.23069 | **Aprile 2026**

## Sintesi

ContextWeaver e un framework di memoria strutturata per agent LLM che organizza la traccia di interazione in un **grafo di passaggi di ragionamento** con dipendenze causali/logiche, selezionando il contesto rilevante per le azioni future. Risolve il problema degli approcci sliding window e prompt compression che perdono informazioni strutturali su cui dipendono passaggi successivi.

## Componenti

1. **Dependency-based construction:** collega ogni passaggio di ragionamento ai precedenti da cui dipende
2. **Compact dependency summaries:** condensa i percorsi root-to-step in unita riutilizzabili
3. **Lightweight validation layer:** incorpora feedback di esecuzione

## Risultati

- Miglioramenti su **SWE-Bench Verified** e **Lite** in pass@1 vs sliding window baseline
- Riduzione dei passaggi di ragionamento e del token usage
- La modellazione delle dipendenze logiche fornisce un meccanismo di memoria stabile e scalabile per agent tool-using

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — approccio dependency-graph vs retrieval semantico
