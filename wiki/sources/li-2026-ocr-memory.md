---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [optical-memory, visual-retrieval, long-horizon-agents, multimodal]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Jinze Li et al.** (HKU et al.), arXiv:2604.26622, Apr 2026.

## Summary

OCR-Memory è un framework di memoria che sfrutta la **modalità visuale** come rappresentazione ad alta densità dell'esperienza agente, abilitando la retention di storie arbitrarie lunghe con minimo overhead prompt al momento del retrieval. Renderizza traiettorie storiche in immagini annotate con identificatori visivi univoci, recuperando esperienza tramite paradigma **locate-and-transcribe**: seleziona regioni rilevanti via anchor visivi e trascrive il testo verbatim corrispondente.

## Key Claims

- L'encoding ottico aumenta la capacità memoria effettiva preservando il recupero fedele delle evidenze [[wiki/sources/li-2026-ocr-memory]](raw/papers/arxiv-2604.26622.pdf).
- Evita free-form generation riducendo l'allucinazione rispetto a retrieval puramente testuale [[wiki/sources/li-2026-ocr-memory]](raw/papers/arxiv-2604.26622.pdf).
- I sistemi esistenti sono fondamentalmente limitati dai budget testuali: memorizzare traiettorie raw è proibitivo, mentre summarization trade token savings per information loss [[wiki/sources/li-2026-ocr-memory]](raw/papers/arxiv-2604.26622.pdf).
