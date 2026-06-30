---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, context-management, dependency-graph, agents]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Dependency-Structured Memory for LLM Agents

**Wu et al. (2026)** — UT Austin / AWS AI Labs

## Summary

ContextWeaver è un framework di memoria **selettiva e strutturata per dipendenze** per agenti LLM. A differenza di approcci come sliding window o prompt compression che selezionano contenuto basandosi su recentness, salience o similarità semantica, ContextWeaver cattura la **struttura di dipendenza** che collega un ragionamento step al successivo.

## Componenti

1. **Costruzione basata su dipendenze**: ogni reasoning step viene collegato agli step precedenti da cui dipende
2. **Summarizzazione compatta delle dipendenze**: condensa i percorsi di ragionamento root-to-step in unità riutilizzabili
3. **Layer di validazione leggero**: incorpora feedback di esecuzione

Il sistema organizza la traccia di interazione dell'agente in un grafo di reasoning steps e seleziona il contesto rilevante per le azioni future.

## Risultati

Su SWE-Bench Verified e Lite: miglioramenti in pass@1 rispetto a sliding-window baseline, con **riduzione dei reasoning steps e del token usage**.

## Claim chiave

- Modelling logical dependencies fornisce un meccanismo di memoria stabile e scalabile per agenti LLM che usano tool [[wiki/sources/arxiv-2604.23069]]
- I segnali di recency/salience non catturano la struttura causale/logica necessaria per multi-step reasoning [[wiki/sources/arxiv-2604.23069]]
