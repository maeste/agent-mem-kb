---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [moe, kimi-k3, model-architecture, scaling, open-weights]
source_path: raw/web/sparse-by-design/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Sparse By Design — Kimi K3 And Open Model Scaling

Analisi di Akash Bajwa (20 lug 2026) sulle tendenze architetturali dei modelli open weights, focalizzata su Kimi K3 di Moonshot.

## Kimi K3: numeri chiave

- **2.8T parametri totali**, attiva solo **16 su 896 experts** per token (<2% di pesi attivi per forward pass) [[raw/web/sparse-by-design/index.md]]
- Context window: 1M token, multimodalita nativa
- Benchmark: supera Opus 4.8, circa una generazione indietro a Fable 5 e GPT-5.6
- Uscita prevista: 27 luglio 2026

## Trend di sparsificazione

- Parametri totali cresciuti ~20x da Mixtral, ~3x negli ultimi 12 mesi
- **Parametri attivi pressoché stagni**: fascia 17-49B per 27 mesi
- Moonshot ha ship K2, K2.5, K2.6 in 9 mesi con identico skeleton (1T total, 32B active): zero crescita active parameters
- A budget di training compute fisso, piu experts = minor loss; si paga in **storage** (cheap), non in compute/memory bandwidth (scarce e razionate)
- "The cheapest way to buy intelligence is to spend capacity"

## KV Cache Compression

- Trend complementare: attention compression (CSA/HCA hybrid, Multi-head Latent Attention, nuova architettura K3) comprime la cache
- V4-Pro KV cache a 1M context e il **10%** del predecessore
- Sparser experts riducono weight-bytes/token; compressed attention riduce cache-bytes/token; storage memorizzato solo cresce

## Due regimi di serving

- **Low batch (enterprise self-host)**: tiered memory (HBM per expert frequenti, DRAM per quelli rari). Sparsity rende possibile self-hosting di modelli trillion-scale
- **Hyperscale (high batch)**: ogni token attiva expert diversi, niente cold experts. Sparsity converte bandwidth demand in **HBM capacity demand**: piu stack, streamed meno hard

## Routing come fattore critico

- Router attuali spread tokens uniformemente: fallisce tiering ad alto batch
- Se router allenati con **localita deliberata** (expert popolari, path prevedibili), tiering diventa viable anche ad alto batch
