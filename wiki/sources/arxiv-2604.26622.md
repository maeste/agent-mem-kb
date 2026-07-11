---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [visual-memory, optical-retrieval, long-horizon-agents, context-compression, multimodal]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Li, Zhang, Yang, Qu, Xu, Yang, Ding, Ngai** (HKU, UNT, Tsukuba, Yonsei) — arXiv:2604.26622, Apr 2026

## Summary

OCR-Memory è un framework di memoria che usa la **modalità visiva** come rappresentazione ad alta densità dell'esperienza dell'agente, permettendo la retention di storie arbitrarie lunghe con minimo overhead token al momento del retrieval.

## Claim principali

- **Motivazione**: i sistemi di memoria agentici sono fondamentalmente limitati dai budget testuali. Storing/revisiting raw trajectories è proibitivo in token; summarization e text-only retrieval trade token savings per information loss e evidenza frammentata [[raw/papers/arxiv-2604.26622.pdf]].
- **Approccio visivo**: renderizza traiettorie storiche in immagini annotate con identificatori visivi univoci (bounding boxes indicizzati). Il contenuto denso testuale viene codificato in visual tokens che consumano sostanzialmente meno context mantenendo full fidelity [[raw/papers/arxiv-2604.26622.pdf]].
- **Locate-and-transcribe paradigm**: il modulo di retrieval ottico scansiona le rappresentazioni visuali per predire gli indici dei segmenti rilevanti (non genera testo libero), poi recupera il testo verbatim corrispondente dal database. Decouple context understanding da evidence generation [[raw/papers/arxiv-2604.26622.pdf]].
- **Age-aware adaptive-resolution**: memorie vecchie vengono progressivamente store come thumbnail low-resolution (preservano il semantic gist sufficiente per retrieval). Quando identificate come rilevanti, active-recall up-sampling ripristina alta fedeltà [[raw/papers/arxiv-2604.26622.pdf]].
- **Risultati**: consistent gains su long-horizon agent benchmarks sotto strict context limits. L'encoding ottico aumenta effective memory capacity preservando faithful evidence recovery [[raw/papers/arxiv-2604.26622.pdf]].

## Posizione nel dibattito

Approccio originale che esplora una dimensione (multimodalità) poco esplorata nella letteratura su agentic memory. La chiave insight: usare la visione come compressione loss-free per testo. Rilevante per il trade-off capacity vs fidelity.
