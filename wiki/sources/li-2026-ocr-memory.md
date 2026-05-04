---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, visual, optical, multimodal, long-horizon]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Autori:** Jinze Li et al. (HKU, UNT, U. Tsukuba, Yonsei)
**Data:** 2026-04-29

## Summary

OCR-Memory sfrutta la modalità visiva come rappresentazione ad alta densità dell'esperienza dell'agente. Codifica traiettorie storiche come immagini con anchor visivi unici (bounding box indicizzate), recuperando info tramite paradigma locate-and-transcribe che seleziona regioni rilevanti e trascrive il testo verbatim corrispondente.

Evita il trade-off tra capacità di memoria e completezza informativa: storicizza tracce arbitrarie senza summarization lossy. Riduce l'allucinazione rispetto alla generazione free-form. Guadagni consistenti su benchmark long-horizon con limiti di contesto stretti.

[[wiki/pages/memory-architectures-retrieval]]
