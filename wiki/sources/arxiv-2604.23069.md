---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [dependency-memory, context-management, reasoning-graph, swe-bench]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Dependency-Structured Memory for LLM Agents

**Autori:** Wu et al. (UT Austin, AWS AI Labs) | **arXiv:** 2604.23069 | **Apr 2026**

## Summary

ContextWeaver è un framework di memoria selettiva e dependency-structured che organizza il trace di interazione di un agente in un grafo di reasoning step e seleziona il contesto rilevante per azioni future. A differenza di approcci esistenti (sliding window, compression, retrieval semantico), supporta:

1. **Costruzione e traversal basati su dipendenze**: ogni step linkato agli step precedenti da cui dipende
2. **Summarization dipendenza compatta**: condensa path root-to-step in unità riutilizzabili
3. **Layer di validazione lightweight**: incorpora feedback di esecuzione

Valutato su SWE-Bench Verified e Lite.

## Key claims

- Miglioramento pass@1 vs sliding-window baseline su SWE-Bench, con riduzione reasoning steps e token usage [[wiki/pages/contextweaver]]
- Le dipendenze logiche sono segnale più stabile di recency/salience/semantic similarity per agenti tool-using
