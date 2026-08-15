---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [diffusion-model, architecture, google-deepmind, gemma, decoding, paper]
source_path: raw/papers/arxiv-2608.00146.pdf
ingested: 2026-W31 (Sat-Sat)
---

# DiffusionGemma Technical Report

Google DeepMind (Aug 2026). Modello sperimentale open-weight che usa discrete diffusion per generare testo ad alta velocità, raffinando blocchi di 256 token in parallelo invece di decodificare un token alla volta.

## Architettura

Ottenuto fine-tunando il modello mixture-of-experts **Gemma 4** (3.8B activated / 25.2B total). Pipeline two-stage compute-efficient (<10% del budget token del modello AR originale):

1. **SFT** per insegnare bidirectional denoising
2. **RL + sampler distillation** per migliorare jointly qualità generazione e efficienza inference

## Risultati

- ~20 token per forward pass
- ~1.500 output token/secondo su singola NVIDIA H100
- Sostanzialmente più veloce dei modelli AR anche con speculative decoding all'avanguardia
- Nuova Pareto frontier speed vs capability
- Mantiene thinking mode, multimodal inputs, long context
- Rimane capace di AR generation con degrado minore: path verso hybrid diffusion-AR decoding

## Connessioni

Architetturalmente rilevante per [[wiki/pages/moe-sparsity]] (parte dalla base MoE Gemma 4). Il parallel decoding apre una direzione diversa dal puro test-time scaling: invece di più tentativi seriali (vedi [[wiki/sources/arxiv-2607.28576-more-reflect-less|More, Reflect Less]]), parallelizza la generazione stessa.
