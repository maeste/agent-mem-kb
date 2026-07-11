---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [memory-governance, memory-worth, staleness-detection, deprecation, operational-metric]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Simsek** — arXiv:2604.12007, Apr 2026

## Summary

Questo paper propone **Memory Worth (MW)**: un segnale per-memoria a due contatori che traccia la co-occorrenza di ogni memoria con outcome di successo vs fallimento, fornendo una base operazionale lightweight per decisioni di governance della memoria.

## Claim principali

- **Problema**: i sistemi di memoria agentica accumulano esperienza ma mancano di una metrica operazionale principled per decidere quali memorie trust, suppress o deprecare. Write-time importance scores sono statici; dynamic management usa LLM judgment o euristiche strutturali senza outcome feedback [[raw/papers/arxiv-2604.12007.pdf]].
- **Memory Worth (MW)**: due contatori scalari per memoria che tracciano quante volte co-occorre con successo (+1) vs fallimento (-1). Supporta staleness detection, retrieval suppression, uncertainty-aware review, deprecation [[raw/papers/arxiv-2604.12007.pdf]].
- **Convergenza teorica**: MW converge almost surely alla conditional success probability p+(m) = Pr[yt = +1 | m ∈ Mt] sotto stationary retrieval regime con minimum exploration condition (provato via martingale argument) [[raw/papers/arxiv-2604.12007.pdf]].
- **MW è associzionale, non causale**: misura co-occorrenza di outcome, non contribuzione causale. L'autore argomenta che è comunque utile come signal operativo minimale [[raw/papers/arxiv-2604.12007.pdf]].
- **Risultati empirici**: dopo 10,000 episodi, Spearman rank-correlation ρ = 0.89 ± 0.02 tra MW e true utilities (vs ρ = 0.00 per sistemi statici). In microexperimento con real text + embedding retrieval: stale memories crossano la soglia low-value (MW = 0.17), specialist memories rimangono high-value (MW = 0.77) [[raw/papers/arxiv-2604.12007.pdf]].
- **Requisiti minimi**: solo due scalar counters per memoria unit + logging di retrievals e episode outcomes. Nessuna modifica architetturale [[raw/papers/arxiv-2604.12007.pdf]].

## Posizione nel dibattito

Contributo metodologico pulito e minimale. MW è un "primitive" su cui sistemi più complessi possono essere composti. Complementa A-MAC (admission control pre-storage): A-MAC controlla cosa entra; MW traccia quanto bene ciò che è dentro performa.
