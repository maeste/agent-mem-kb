---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, agents, visual-retrieval, OCR, long-horizon]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Li et al. (2026)** — HKU / UNT / Tsukuba / Yonsei

## Summary

OCR-Memory affronta il vincolo fondamentale dei sistemi di memoria agente: il **budget testuale del context window**. Memorizzare o rivisitare traiettorie raw è proibitivo in termini di token; la summarization e il retrieval testuale scambiano risparmio di token con perdita di informazione.

L'idea centrale: usare la **modalità visiva** come rappresentazione ad alta densità dell'esperienza agente. Le traiettorie storiche vengono renderizzate in immagini annotate con identificatori visivi univoci. Il retrieval avviene tramite paradigma **locate-and-transcribe**: seleziona regioni rilevanti tramite anchor visivi e trascrive il testo verbatim corrispondente.

## Vantaggi

- Capacità di memoria effettiva aumentata tramite encoding ottico
- Recupero fedele delle evidenze (evita generazione free-form e riduce allucinazione)
- Costo minimo al momento del retrieval
- Guadagni consistenti su benchmark long-horizon sotto contesti limitati

## Claim chiave

- La rappresentazione visiva può servire come mezzo ad alta densità e loss-free per memoria a lungo termine [[wiki/sources/arxiv-2604.26622]]
- Il paradigma locate-and-transcribe riduce l'allucinazione rispetto alla generazione libera [[wiki/sources/arxiv-2604.26622]]
