---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, forgetting, governance, staleness, memory-quality]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Autori:** Baris Simsek
**arXiv:** 2604.12007 | Aprile 2026

## Riassunto

Il paper introduce **Memory Worth (MW)**: un segnale a due contatori per-memoria che traccia quanto spesso una memoria co-occorre con esiti di successo vs fallimento. Fornisce una foundation teorica lightweight per staleness detection, retrieval suppression e deprecation decisioni.

Prova che MW converge quasi sicuramente alla probabilità condizionale di successo p+(m) = Pr[yt = +1 | m in Mt] sotto un regime di retrieval stazionario con condizione di esplorazione minima. Importante: p+(m) è una quantità associazionale, non causale: misura outcome co-occurrence, non impatto causale.

I sistemi memory esistenti si basano su euristiche write-time o importance scores assegnati da LLM per valutare qualità della memoria. MW offre invece una metrica operazionale basata su outcome feedback reale.

## Claim chiave

- Memory Worth (MW) fornisce una metrica operazionale con garanzie di convergenza per la governance della memoria [[wiki/sources/arxiv-2604.12007.md]]
- Le importance scores statiche write-time sono inadeguate per gestire quality decay della memoria [[wiki/sources/arxiv-2604.12007.md]]
- L'approccio associazionale (non causale) è sufficiente per decisioni di deprecation pragmatiche [[wiki/sources/arxiv-2604.12007.md]]

## Collegamenti

- Complementa [[wiki/sources/gu-2026-fsfm.md]] (FSFM) sul forgetting selettivo
- Relazionato a [[wiki/sources/simsek-2026-when-to-forget.md]] (stesso lavoro)
- Governance primitive per [[wiki/pages/memory-systems]]
