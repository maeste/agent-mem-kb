---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [visual-memory, optical-retrieval, long-horizon-memory, multimodal]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Jinze Li et al.** (HKU, UNT, Tsukuba, Yonsei) — arXiv:2604.26622, Apr 2026

## Summary

OCR-Memory è un framework di memoria che sfrutta la **modalità visiva** come rappresentazione high-density dell'esperienza agente, abilitando la retention di storie arbitrarie lunghe con minimo prompt overhead al momento del retrieval. Il problema: i sistemi memoria esistenti sono vincolati dai budget testuali; memorizzare traiettorie grezze è proibitivo in token, mentre summarization e retrieval text-only scambiano risparmio token con perdita informativa.

Approccio:
- **Rendering**: traiettorie storiche renderizzate in immagini annotate con identificatori visivi unici
- **Locate-and-transcribe paradigm**: seleziona regioni rilevanti tramite anchor visuali e trascrive il testo verbatim corrispondente, evitando free-form generation e riducendo hallucination

La codifica ottica aumenta la capacità memoria effettiva preservando il recupero evidence fedele. Risultati consistenti su benchmark long-horizon agent con contesto limits stretti.

## Key claims
- La modalità visiva è superiore al testo per densità informativa nella memoria ([§Abstract](raw/papers/arxiv-2604.26622.pdf))
- Il locate-and-transcribe riduce hallucination vs generazione libera ([§3](raw/papers/arxiv-2604.26622.pdf))
- L'encoding ottico elimina il trade-off capacità/completezza dei metodi testuali ([§1](raw/papers/arxiv-2604.26622.pdf))

## Connections
- [[wiki/sources/li-2026-ocr-memory]] — fonte primaria
- [[wiki/pages/multimodal-memory]] — memoria non-testuale per agenti
