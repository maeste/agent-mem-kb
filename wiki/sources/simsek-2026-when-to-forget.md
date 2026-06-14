---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [memory-governance, forgetting, staleness-detection, memory-quality]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Baris Simsek**, arXiv:2604.12007, Apr 2026.

## Summary

Propone **Memory Worth (MW)**: un segnale per-memoria a due contatori che traccia quanto spesso una memoria co-occorre con outcome di successo vs fallimento. Fornisce una base teorica leggera per staleness detection, retrieval suppression e decisioni deprecazione. Prova che MW converge quasi sicuramente alla probabilità di successo condizionato p+(m).

## Key Claims

- Dopo 10.000 episodi, la **Spearman rank-correlation** tra Memory Worth e utilità reale raggiunge **ρ = 0.89 ± 0.02** su 20 seed indipendenti [[wiki/sources/simsek-2026-when-to-forget]](raw/papers/arxiv-2604.12007.pdf).
- I sistemi che non aggiornano le loro valutazioni raggiungono **ρ = 0.00** (nessuna correlazione) [[wiki/sources/simsek-2026-when-to-forget]](raw/papers/arxiv-2604.12007.pdf).
- L'estimatore richiede solo **due contatori scalari per unità memoria** e può essere aggiunto a architetture che già loggano retrievals e episode outcomes [[wiki/sources/simsek-2026-when-to-forget]](raw/papers/arxiv-2604.12007.pdf).
