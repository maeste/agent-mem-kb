---
type: source
created: 2026-07-31
updated: 2026-07-31
tags: [moe, sparsity, model-release, open-weights, reasoning-effort, multimodal, thinking-machines]
source_path: raw/web/introducing-inkling-small/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Introducing Inkling-Small

**Author:** Thinking Machines Lab | **Date:** Jul 30, 2026 | **URL:** https://thinkingmachines.ai/news/inkling-small/

## Summary

Thinking Machines Lab rilascia Inkling-Small, modello open-weights MoE da 276B parametri totali / 12B attivi per token (~4.4% attivi), che raggiunge prestazioni comparabili al modello maggiore Inkling (41B attivi su 975B) a un quarto della dimensione. Nativamente multimodale (testo, audio via dMel spectrograms, immagini via patch 40x40 con hMLP), con reasoning effort controllabile (da minimal a xhigh) e context window fino a 1M token. Addestrato su NVIDIA GB300 NVL72, disponibile su Tinker per fine-tuning.

## Key Claims

### Efficienza: stessa performance, meno compute
- Inkling-Small supera Inkling su reasoning (HLE 31.6% vs 29.7%) e agentic coding (SWEBench Verified >80%), mantenendo vantaggio su ogni thinking budget
- Inkling mantiene vantaggio su knowledge coverage e factuality (SimpleQA 43.9% vs 20.6%)
- Su Terminal-Bench 2.1, HLE e IFBench mostra miglior performance-compute tradeoff

### Architettura MoE
- 276B totali, 12B attivi: ~4.4% attivazione, conferma il trend di sparsity estrema ([[wiki/pages/moe-sparsity]])
- Encoder-free, multimodale nativo: audio e immagini processati nello stesso stack del testo
- Variable thinking effort come grado di libertà: l'utente bilancia costo e qualità spostando l'effort da minimal a xhigh

### Multimodalità
- Audio: dMel spectrograms, top performer su Audio MC (54.9%) e MMAU (77.0%) tra open weights
- Visione: patch 40x40 pixel via hMLP a 4 layer; può usare Python per crop/zoom e ispezione programmatica
- Combina reasoning visivo con operazioni programmatiche su immagini

### Epistemics
- Calibration via RL contro proper scoring rules su corpus di domande di forecasting reali
- ForecastBench (no search) Brier Index 61.3 ± 0.46: batte Inkling, Kimi K2.6, GPT-5.5
- ProPHET Arena Brier Score 0.1238: competitivo con GPT-5.5 (0.1179) e Gemini 3.1 Pro (0.1155)

### Safety
- Stessa recipe di Inkling: StrongREJECT 98.4%, FORTRESS adversarial 71.6%
- Competitivo con gli open weights su rifiuto di richieste dual-use

## Connessioni

- **Conferma il trend MoE sparsity** ([[wiki/pages/moe-sparsity]]): 12B attivi su 276B totali (~4.4%) si colloca nel range 2-5% che caratterizza i modelli aperti post-Kimi K3. Confronto diretto con Bajwa ([[wiki/sources/akash-bajwa-sparse-by-design]]): Inkling-Small è meno estremo di K3 (16B/2.8T, <2%) ma più efficiente di Mixtral (13B/46B, 28%).
- **Reasoning effort controllabile**: degree of freedom architetturale, non solo prompt engineering. Da collegare a discussioni su agent harness e test-time compute.
