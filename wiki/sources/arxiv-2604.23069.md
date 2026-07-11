---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [dependency-graph, context-management, memory-structure, swe-bench, tool-use]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Dependency-Structured Memory for LLM Agents

**Wu, Zhang, Ghosh, Basu, Deoras, Huan, Gupta** (UT Austin, AWS AI Labs) — arXiv:2604.23069, Apr 2026

## Summary

ContextWeaver è un framework di memoria selettiva e strutturata per dipendenze che organizza la traccia di interazione dell'agente in un **grafo di reasoning step**, selezionando il contesto rilevante per le azioni future basandosi sulle dipendenze logiche e causali.

## Claim principali

- **Problema**: sliding window e prompt compression possono omettere informazioni strutturate precedenti che step successivi dipendono. I sistemi retrieval-based trascurano la struttura causale/logica necessaria per multi-step reasoning [[raw/papers/arxiv-2604.23069.pdf]].
- **Tre componenti**: (1) **Dependency-based construction**: linka ogni reasoning step agli step precedenti da cui dipende; (2) **Compact dependency summaries**: condensano root-to-step reasoning paths in unità riutilizzabili; (3) **Lightweight validation layer**: incorpora execution feedback per filtrare nodi inaffidabili [[raw/papers/arxiv-2604.23069.pdf]].
- **Grafo vs sliding window**: lo sliding window mantiene solo i messaggi recenti scartando informazioni vecchie ma essenziali. ContextWeaver serializza dynamic patterns dal grafo che preservano long-range dependencies [[raw/papers/arxiv-2604.23069.pdf]].
- **Risultati su SWE-Bench Verified/Lite**: migliora pass@1 rispetto a sliding-window baseline, riducendo contemporaneamente reasoning steps e token usage [[raw/papers/arxiv-2604.23069.pdf]].
- **Insight chiave**: modellare le dipendenze logiche fornisce un meccanismo di memoria stabile e scalabile per agent che usano tools [[raw/papers/arxiv-2604.23069.pdf]].

## Posizione nel dibattito

Approccio complementare ai sistemi di memoria basati su similarità semantica. Invece di "cosa è semanticamente simile", chiede "di cosa dipende logicamente questo step?". Particolarmente rilevante per coding agent dove le dipendenze causali (test results → code edits) sono critiche.
