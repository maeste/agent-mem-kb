---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [optical-memory, visual-retrieval, long-horizon-agents, context-compression, ocr]
source_path: raw/papers/arxiv-2604.26622.md
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Autori:** Jinze Li, Yang Zhang et al. (HKU, UNT, Tsukuba, Yonsei) | **arXiv:** 2604.26622 | **Aprile 2026**

## Sintesi

OCR-Memory affronta il vincolo del budget testuale nei sistemi di memoria agent usando la modalita visiva come rappresentazione ad alta densita dell'esperienza. Le traiettorie storiche vengono renderizzate in immagini con identificatori visivi univoci; il retrieval avviene tramite paradigma **locate-and-transcribe**: selezione di regioni rilevanti tramite anchor visivi e trascrizione del testo letterale corrispondente.

## Architettura

- **Encoding:** traiettorie di interazione renderizzate in immagini con bounding box indicizzati come anchor
- **Retrieval:** locate-and-transcribe invece di generazione libera (riduce allucinazioni)
- **Vantaggio chiave:** token visivi consumano sostanzialmente meno contesto del testo raw, mantenendo fedelta completa

## Risultati

- Guadagni consistenti su benchmark long-horizon agent con limiti di contesto stretti
- L'encoding ottico aumenta la capacita di memoria effettiva preservando il recupero fedele delle evidenze
- Evita il trade-off tra capacita di memoria e completezza informativa

## Collegamenti nel vault

- [[wiki/pages/memory-architectures-retrieval]] — approccio alternativo alla compressione di contesto basato su modalita visiva
