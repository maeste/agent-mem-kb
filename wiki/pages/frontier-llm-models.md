---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [llm-models, gemini, moe, kimi-k3, routing, model-scaling]
---

# Frontier LLM Models

Pagina sui modelli LLM frontier: architettura MoE, trend di sparsificazione, routing multi-modello.

## Gemini family (luglio 2026)

Google ha annunciato tre nuovi modelli Flash [[wiki/sources/gemini-3-6-flash]]:

| Modello | Ruolo | Token/s | Prezzo (input/output per M) |
|---------|-------|---------|------------------------------|
| 3.6 Flash | Workhorse | n/d | $1.50 / $7.50 |
| 3.5 Flash-Lite | High-throughput | 350 out | $0.30 / $2.50 |
| 3.5 Flash Cyber | Cybersecurity | n/d | Limited access |

3.6 Flash: -17% output token vs 3.5 Flash, miglioramenti DeepSWE (+12pp), MLE Bench (+14pp), OSWorld (+5pp). Computer use built-in tool. Enhanced Frontier Safety safeguards [[wiki/sources/gemini-3-6-flash]].

3.5 Flash-Lite: in alcuni benchmark supera anche 3 Flash (SWE-Bench Pro, OSWorld-Verified). Ideale per agentic search e document processing ad alto volume [[wiki/sources/gemini-3-6-flash]].

3.5 Flash Cyber: solo governi/trusted partner via CodeMender pilot. Dual-use concerns mitigati con release controllato [[wiki/sources/gemini-3-6-flash]].

In pipeline: 3.5 Pro (testing partner), **Gemini 4** (pre-training iniziato, "most ambitious run yet").

## Trend MoE: sparse by design

Kimi K3 (Moonshot, uscita 27 lug 2026): **2.8T parametri totali**, 896 experts, attiva solo **16 per token (<2%)** [[wiki/sources/sparse-by-design]].

Trend di lungo periodo:
- Parametri totali: ~20x crescita da Mixtral, ~3x negli ultimi 12 mesi
- Parametri attivi: **stagnanti** nella fascia 17-49B per 27 mesi
- Moonship K2/K2.5/K2.6: stesso skeleton 1T/32B per 9 mesi

Ragione: a fisso compute budget, piu experts = minor loss. Si paga in **storage** (cheap tier), non in compute/memory bandwidth (razionato). "The cheapest way to buy intelligence is to spend capacity" [[wiki/sources/sparse-by-design]].

### KV Cache compression
Trend complementare: attention compression riduce drasticamente la cache. V4-Pro a 1M context = 10% cache del predecessore. Sparsity riduce weight-bytes/token; compression riduce cache-bytes/token; storage memorizzato solo cresce [[wiki/sources/sparse-by-design]].

### Due regimi di serving
- **Low batch (enterprise)**: tiered memory possibile (HBM hot, DRAM cold). Sparsity rende self-hosting di trillion-scale models possibile
- **Hyperscale (high batch)**: ogni token attiva expert diversi, niente cold experts. Sparsity converte bandwidth -> HBM capacity demand

**Routing e il fattore critico**: router attuali spread uniformemente (fallisce tiering). Router con localita deliberata abilierebbero tiering anche ad alto batch [[wiki/sources/sparse-by-design]].

## Routing multi-modello: quando ha senso?

Due proprieta strutturali determinano se routing e meaningful [[wiki/sources/arxiv-2607-09197-routing-diversity]]:
1. **Diversita comportamentale**: attori devono rispondere diversamente (altrimenti routing vacuo)
2. **Robustezza**: varianti semanticamente equivalenti devono andare allo stesso attore

Metriche proposte:
- **HSE** (Hierarchic Social Entropy) adattata per LM societies: misura diversita da output, non parametri
- **Robustness metric** (rho): perturbation-based, 5 livelli di perturbazione

Risultati sorprendenti:
- Specialist societies >> real-world model pools in HSE (diversita reale minore del assunto)
- **Diminishing returns forte**: <10 agenti catturano maggior diversita in EmbedLLM, 4 in RouterBench
- **Accuracy e meaningfulness divergono**: KNN routers = best accuracy ma worst robustness; prompted routing = stabile ovunque
