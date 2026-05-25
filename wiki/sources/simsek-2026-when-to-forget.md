---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [memory-worth, memory-governance, staleness-detection, outcome-feedback, retrieval-suppression]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Autore:** Baris Simsek | **arXiv:** 2604.12007 | **Aprile 2026**

## Sintesi

Questo lavoro propone **Memory Worth (MW)**: un segnale per-memoria a due contatori che traccia la co-occorrenza di ogni memoria con esiti di successo vs fallimento, fornendo una base teorica leggera per decisioni di staleness detection, retrieval suppression e deprecazione.

## Proprieta chiave

- MW converge quasi sicuramente alla probabilita condizionale di successo p+(m) = Pr[yt = +1 | m in Mt]
- Quantita associazionale, non causale: misura co-occorrenza di outcome, non contribuzione causale
- Richiede solo **due contatori scalari** per unita di memoria
- Aggiungibile a architetture che gia loggano retrievals e episode outcomes

## Risultati

- Dopo 10.000 episodi: **Spearman rho = 0.89 +/- 0.02** tra MW e utilita reale (vs rho = 0.00 per sistemi statici)
- Micro-esperimento con embedding reali (all-MiniLM-L6-v2): memorie stale attraversano soglia bassa (MW = 0.17), specialist rimangono alte (MW = 0.77)

## Collegamenti nel vault

- [[wiki/pages/forgetting-memory-governance]] — MW come primitiva operazionale per la governance della memoria
