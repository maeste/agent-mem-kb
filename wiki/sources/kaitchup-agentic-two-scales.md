---
type: source
created: 2026-08-01
updated: 2026-08-01
tags: [agentic-ai, model-architecture, looped-transformer, moe, small-model, coding-agent]
source_path: raw/web/agentic-ai-at-two-different-scales-nanbeige4-2-3b-and-laguna-s2-1/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Agentic AI at Two Different Scales: Nanbeige4.2-3B and Laguna S 2.1

The Weekly Kaitchup #152 (Benjamin Marie, Jul 25 2026). Confronto tra due modelli agentic a scale opposte: un dense 3B con Looped Transformer e un MoE 118B/8B per coding long-horizon.

## Nanbeige4.2-3B: Looped Transformer

Modello dense da ~4B parametri (3B non-embedding). 22 layer fisici eseguiti **due volte** (stessi pesi riutilizzati), per una profondità computazionale di ~44 layer senza存储 44 layer indipendenti.

**Trade-off**: meno memoria pesi, ma stesso costo compute di un 44-layer (ogni token passa due volte). KV-cache alta: 8 KV heads × 128 dim, ~176 KiB/token. A 256K context = ~44 GiB per singola sequenza, quasi il doppio di Qwen3.6 27B. I modelli looped dovrebbero indicare il numero di pass nel nome (es. `3B-2P`), come i MoE indicano i parametri attivi.

**Risultati**: supera Qwen3.5-9B e Gemma 4 12B su agent/coding/reasoning benchmark.

## Laguna S 2.1: MoE 118B/8B per coding

MoE con 118B parametri totali, ~8B attivi/token. 48 layer (12 global attention + 36 sliding-window 512). 256 routed expert, top-10 + 1 shared. Per-head softplus output gating (volume control per attention head). Reasoning interleaved con tool call.

**Target**: long-horizon software engineering (repo-level bug fixing, terminal interaction, multilingual code maintenance). KV-cache 256K ~24 GB.

**Controversia community**: benchmark con risultato eccellente ma feedback mixed. Il reviewer nota che Laguna S 2.1 su DeepSWE non raggiunge una frazione del claim. Il pool harness non è open source e avrebbe un "hidden advisor" feature che chiama un modello più smart, non documentato.

## Rilevanza per il vault

Nanbeige (Looped Transformer) è un'architettura alternativa alla [[wiki/pages/moe-sparsity|MoE sparsity]] per ottenere profondità computazionale senza espandere i parametri: invece di sparsity spaziale (expert routing), usa **sparsity temporale** (stessa compute ripetuta). Entrambi i modelli confermano che l'agentic capability non richiede scale iperbolica: 3B dense o 8B active possono competere, se l'architettura e il training sono giusti. La controversia su Laguna conferma il problema di [[wiki/pages/harness-design]]: quando il harness non è open, i benchmark sono non verificabili (vedi anche [[wiki/sources/arxiv-2607-12227-harness-evaluation]]).
