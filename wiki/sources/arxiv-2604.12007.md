---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, governance, forgetting, staleness, agents]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Simsek (2026)** — Independent

## Summary

Questo paper introduce **Memory Worth (MW)**, un segnale per-memoria a due contatori che traccia quanto spesso una memoria co-occorre con outcome di successo vs fallimento. Fornisce una base lightweight e teoricamente fondata per decisioni di staleness detection, retrieval suppression, e deprecation.

Il problema: i sistemi memoria agenti accumulano esperienza ma mancano di un metrica operativa principlesca per la *governance* della qualità delle memorie. Gli score di importanza write-time sono statici; i sistemi dinamici usano giudizio LLM o euristiche strutturali piuttosto che feedback di outcome.

## Proprietà matematiche

MW converge almost surely alla probabilità di successo condizionale p+(m) = Pr[yt = +1 | m in Mt] sotto un regime di retrieval stazionario con condizione minima di exploration. Importante: p+(m) è associativo, non causale.

## Risultati

- Dopo 10,000 episodi: Spearman rank-correlation ρ = **0.89 ± 0.02** tra MW e true utilities
- Sistemi senza aggiornamento: ρ = **0.00**
- Micro-esperimento con real text + embedding retrieval: stale memories crossano la soglia low-value (MW=0.17), specialist memories rimangono high-value (MW=0.77)

## Claim chiave

- La memory governance richiede un primitivo operativo per-memoria che accumuli evidenza di retrieval [[wiki/sources/arxiv-2604.12007]]
- Due contatori scalari per memoria sono sufficienti per un segnale utile di qualità [[wiki/sources/arxiv-2604.12007]]
