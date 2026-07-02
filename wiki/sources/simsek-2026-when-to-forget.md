---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [memory-governance, memory-worth, staleness-detection, deprecation, operational-metric]
source_path: raw/papers/arxiv-2604.12007.pdf
---

# When to Forget: A Memory Governance Primitive

**Autore:** Baris Simsek  
**Data:** Aprile 2026 | arXiv:2604.12007

## Sintesi

Questo paper introduce **Memory Worth (MW)**: una primitiva operazionale lightweight per la governance della memoria agentica che risponde alla domanda: "come dovrebbe un agente decidere quali memorie rimangono affidabili col passare dell'esperienza?"

### Il problema

I sistemi di memoria agentica:
- Usano **write-time heuristics** o **LLM-assigned importance scores** per valutare la qualita' delle memorie
- Questi score sono **statici**: una memoria giudicata importante al momento della scrittura puo' diventare stale o dannosa
- Gli outcome signals disponibili a ogni episodio **vanno persi**: una memoria presente durante dozzine di fallimenti continua ad essere trattata come trustworthy

### Memory Worth: definizione

MW e' uno statistica **a due contatori per memoria** che traccia:
- Quante volte la memoria co-occorre con **outcomes di successo**
- Quante volte co-occorre con **outcomes di fallimento**

Sotto un regime di retrieval stazionario con condizione minima di exploration:

**MW converge almost surely a p+(m) = Pr[yt = +1 | m in Mt]**

la probabilita' condizionale di successo dato che la memoria m e' stata recuperata.

### Proprieta' chiave

- MW e' una quantita' **associazionale**, non causale: misura co-occorrenza di outcome, non contribuzione causale
- Richiede solo due scalar counters per memoria unitaria
- Puo' essere aggiunto a architetture che gia' loggano retrievals e episode outcomes
- Supporta tre azioni: staleness detection, retrieval suppression, deprecation

### Risultati empirici

- Synthetic environment (ground-truth utility nota): dopo 10,000 episodi, **Spearman rho = 0.89 +/- 0.02** tra MW e true utilities (20 seed indipendenti)
- Sistemi che non aggiornano mai le loro stime: **rho = 0.00**
- Microexperimento con embedding retrieval reale (all-MiniLM-L6-v2):
  - Stale memories crossano la soglia low-value (**MW = 0.17**)
  - Specialist memories rimangono high-value (**MW = 0.77**) dopo 3,000 episodi

## Claim chiave

- La memory governance richiede una primitiva operazionale online, non statiche write-time heuristics [[wiki/sources/gu-2026-fsfm.md]]
- L'associazione outcome-memoria, seppur non causale, e' un segnale operativo sufficiente per deprecation/suppression decisions
- Due contatori scalari per memoria sono sufficienti per convergenza con garanzie teoriche

## Posizione nel vault

Paper metodologico fondamentale per memory governance. Fornisce la primitiva base su cui sistemi piu' complessi (come FSFM) possono costruire politiche di forgetting.
