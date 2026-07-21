---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [memory-governance, forgetting, staleness, memory-worth]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Autore:** Baris Simsek | **arXiv:** 2604.12007 | **Apr 2026**

## Summary

Propone **Memory Worth (MW)**: un segnale per-memoria a due counter che traccia quante volte una memoria co-occorre con outcome di successo vs fallimento. Fornisce base teorica per staleness detection, retrieval suppression e deprecation.

Prova che MW converge quasi sicuramente alla probabilità condizionale di successo p+(m) = Pr[yt = +1 | m in Mt] sotto regime stationary con minima exploration condition. MW è associazionale, non causale: misura co-occorrenza outcome, non contributo causale.

## Key claims

- Spearman rank-correlation tra MW e true utilities raggiunge ρ = 0.89 ± 0.02 dopo 10k episodi vs ρ = 0.00 per sistemi statici [[wiki/pages/when-to-forget]]
- Richiede solo due scalar counters per memoria unità, addibile a architetture che già loggano retrievals e outcomes
- Le memorie stale attraversano la soglia low-value (MW ~0.17) mentre specialist rimangono high-value (MW ~0.77)
