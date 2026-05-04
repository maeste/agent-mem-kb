---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, forgetting, staleness, memory-worth, convergence]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Autore:** Baris Simsek
**Data:** 2026-04-15

## Summary

Propone Memory Worth (MW), segnale per-memoria a due contatori che traccia co-occorrenza con outcome positivi/negativi. Dimostra convergenza quasi certa alla probabilità condizionale di successo p+(m) = Pr[yt=+1 | m ∈ Mt] sotto regime stazionario con condizione minima di esplorazione.

MW è una quantità associativa (non causale), ma rimane un segnale operativo utile per staleness detection, retrieval suppression e deprecation. Rappresenta una base teorica leggera per decidere quali memorie fidarsi, sopprimere o deprecare man mano che la distribuzione dei task dell'agente shifta.

[[wiki/pages/forgetting-memory-governance]]
