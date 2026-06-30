---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, reasoning, causal-graph, agents, conflict-detection]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging Memory Retrieval and Reasoning in LLM Agents

**Zhang et al. (2026)** — Nanjing University / Alibaba

## Summary

ActMem affronta il gap fondamentale tra **ricordare il passato** e **usarlo efficacemente**. I framework memoria esistenti trattano gli agenti come "recorder" passivi: recuperano informazioni senza comprenderne le implicazioni profonde. Falliscono in scenari che richiedono conflict detection e decision-making complesso.

ActMem trasforma la storia di dialogo non strutturata in un **grafo causale e semantico**. Usa counterfactual reasoning e commonsense completion per dedurre vincoli impliciti e risolvere conflitti tra stati passati e intenzioni correnti.

## Dataset

Introduce **ActMemEval**, dataset comprehensivo per valutare le capability di ragionamento agente in scenari logic-driven, andando oltre il focus fact-retrieval dei benchmark esistenti.

## Esempio motivante

L'utente chiede dove comprare "Sago Palms" (piante velenose per i cani). La memoria passata menziona un cucciolo che mastica tutto. Un sistema di retrieval puro non vede sovrapposizione semantica; ActMem deve inferire il conflitto latente via commonsense reasoning.

## Claim chiave

- Il retrieval memoria deve essere integrato con causal reasoning per supportare task memory-dependent complessi [[wiki/sources/arxiv-2603.00026]]
- I benchmark esistenti testano fact-retrieval, non reasoning con memoria [[wiki/sources/arxiv-2603.00026]]
