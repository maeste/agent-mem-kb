---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [memory-governance, forgetting, memory-quality, staleness-detection]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Baris Simsek** — arXiv:2604.12007, Apr 2026

## Summary

Questo paper introduce **Memory Worth (MW)**: un segnale per-memoria a due contatori che traccia quanto spesso una memoria co-occorre con outcome di successo vs fallimento. Fornisce una base metodologica e teorica per **staleness detection**, retrieval suppression e deprecation decisioni.

Risultati chiave:
- MW converge almost surely alla conditional success probability p+(m) = Pr[yt = +1 |m ∈ Mt] sotto assunzioni esplicite
- Dopo 10.000 episodi: Spearman rank-correlation ρ = 0.89 ± 0.02 tra MW e true utilities (vs ρ = 0.00 per sistemi senza update)
- Micro-esperimento con embedding retrieval (all-MiniLM-L6-v2): stale memories attraversano soglia low-value (MW = 0.17), specialist memories rimangono high-value (MW = 0.77)

Il richiede solo due scalar counters per memoria unit + logging di retrievals e episode outcomes. Limitazione chiave: MW misura associazione outcome, non causazione.

## Key claims
- Gli attuali sistemi ignorano gli outcome signals disponibili ad ogni episodio ([§1](raw/papers/arxiv-2604.12007.pdf))
- MW è un primitivo operativo minimale per la governance della memoria ([§Abstract](raw/papers/arxiv-2604.12007.pdf))
- L'associazione (non causazione) è comunque utile come signal operativo ([§2](raw/papers/arxiv-2604.12007.pdf))

## Connections
- [[wiki/sources/simsek-2026-when-to-forget]] — fonte primaria
- [[wiki/pages/memory-governance]] — gestione qualità e deprecazione memoria
