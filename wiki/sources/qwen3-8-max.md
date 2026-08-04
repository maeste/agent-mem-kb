---
type: source
created: 2026-08-04
updated: 2026-08-04
tags: [model-release, qwen, moe, long-horizon-agents, self-evolving-harness, multimodal, autonomous-coding]
source_path: raw/web/qwen3-8-max/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Qwen3.8-Max: A New Bar for Coding and Cowork

**Qwen Team**, 3 agosto 2026. ℹ️ Rilascio del nuovo flagship Qwen, primo Max-class della serie ad annunciare open weights (entro la settimana).

## In breve

Qwen3.8-Max scala a **2.4T parametri totali, 95B attivi** (~4% attivi). Costruito sull'architettura di Qwen3.5. Posizionamento su coding agent, long-horizon autonomous tasks, multimodal agents. API via QwenCloud (OpenAI + Anthropic compatible), supporta `reasoning_effort` (xhigh/medium/low) e `preserve_thinking`.

## I tre casi di coding autonomo

Il filo conduttore: il modello **self-evolves through feedback loops**, non segue un piano fisso.

1. **Self-evolving harness (10+ giorni)** — crea `oh-my-cli` da zero, poi un harness che fa evolvere il prodotto: issue state machine + dispatcher + monitor + watchdog in un loop. Requisiti da GitHub Issues → ready/leased/active → E2E + CI → merge. Dopo ~16 giorni autonomi: 265 commit, 127 PR, 151 issue. Repo: qwen-code-dev-bot/oh-my-cli. **Il modello costruisce il proprio harness di sviluppo come artefatto autonomo.**
2. **Riproduci un paper, poi miglioralo (5 giorni)** — partendo solo dal paper "Unified Data Selection for LLM Reasoning" e GPU, ~7.600 righe di codice, 1.100 azioni, 33 round di training. Riproduce i 6 finding principali, poi genera 18 idee proprie in 4 round; la 4a ("nhighgate" — conta i hard decision points) batte il metodo originale di **+2.71 pt su AIME24**.
3. **Batta 526 team umani in 24h** — WWW2025 Multimodal Dialogue Intent Recognition Challenge (Tianchi). Ensemble BERT/MacBERT/RoBERTa + Qwen2.5-VL-7B + Chinese-CLIP, weighted voting. Da 0.60 a 0.853 in 45 submission, batte l'87% dei team umani.

## Hardware design autonomo (EDA → silicio)

Ottimizzazione RTL di un core RSA (modular exponentiation) per **500 turn** senza design di riferimento, loop edit-simulate-synthesize-layout. Gate count **8.298 → 678** in 8 stage. Verifica fisica via OpenROAD: die 106×106 → 46×46 µm² (−81%), timing closure a 500 MHz.

## Continuous learning (E-Commerce Bench, 365 giorni)

Simulazione e-commerce realistica: 12 tipi di store, 60 categorie, ~600 fornitori, 7.000 prodotti, ¥100k capitale iniziale. Qwen3.8-Max arriva a **¥416.252 (4.16x)**, +38% su GLM 5.2, +152% su Qwen3.7-Max. Mostra **continuous learning nelle negoziazioni** (prezzi di acquisto decrescenti round dopo round) e allocazione di capitale forward-looking.

## Multimodal agents

Vision attraverso l'intero lifecycle: non solo input (documenti >200 pag, video >100h → video memory graph), ma **feedback loop durante l'esecuzione** — il modello osserva i propri risultati intermedi, rileva deviazioni (oggetto male orientato, UI disallineata) e corregge autonomamente.

- **RecreationBench**: ricostruire app esistenti osservandole come black box, 5 piattaforme.
- **Qwen-MM-Plugins**: libreria di estensione multimodale per agent harness (memoria multimodale, video editing, Blender, CAD). Conferma il trend harness-as-extensible-substrate.

## Connessioni con il vault

- **[[wiki/pages/harness-design]]** — Il caso oh-my-cli è la prima dimostrazione concreta di un **harness che costruisce sé stesso**: il modello genera lo stato-macchina, il dispatcher, i test, l'E2E, il CI gate. Questo va oltre il framework WHAT vs HOW di Miessler: qui l'harness non è dato, è **output del processo**. Aggiunge una sesta visione: l'harness come entità auto-prodotta.
- **[[wiki/pages/moe-sparsity]]** — 2.4T/95B è il nuovo dato più estremo nella tabella sparsity (~4% attivi), allineato a Kimi K3 (2.8T/16B, <2%) ma con parametri attivi molto più alti (95B vs 16B). Qwen sceglie la stessa direzione di Moonshot: sparsity spaziale massima.
- **Long-horizon agents** — 16 giorni, 5 giorni, 24h, 500 turni, 365 giorni: spettro di autonomia temporale che diventa metrica di capability a sé stante.
