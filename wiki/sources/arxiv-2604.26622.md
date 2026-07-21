---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [optical-memory, visual-retrieval, long-horizon, ocr]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Agent Memory

**Autori:** Li et al. (HKU, UNT, Tsukuba, Yonsei) | **arXiv:** 2604.26622 | **Apr 2026**

## Summary

OCR-Memory è un framework che usa la modalità visiva come rappresentazione ad alta densità dell'esperienza agente, permettendo di retainere storie arbitrarie lunghe con minimo prompt overhead al momento del retrieval. Renderizza traiettorie storiche in immagini annotate con identificatori visivi univoci.

Il paradigma **locate-and-transcribe** seleziona regioni rilevanti via anchor visuali e recupera il testo verbatim corrispondente, evitando free-form generation e riducendo hallucination.

## Key claims

- L'encoding ottico aumenta la capacità memoria effettiva preservando recupero evidence fedele [[wiki/pages/ocr-memory]]
- Guadagni consistenti su benchmark long-horizon con contesto limitato strettamente
- Il trade-off token-storage vs information-loss viene superato usando il canale visuale
