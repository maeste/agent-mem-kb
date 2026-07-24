---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [failure-analysis, agent-reliability, debugging, epistemic-error, concept]
---

# Agent Failure Analysis

Lo studio di come e perché gli agenti LLM falliscono, analizzando le traiettorie di esecuzione come processi temporali anziché solo outcomes finali. Dalla failure analysis emerge un pattern: i fallimenti sono predominantemente epistemici e iniziano presto.

## Failure as Process

Zhao et al. ([[wiki/sources/arxiv-2607-09510-failure-as-process]]) analizzano 1,794 traiettorie (63,000+ step) da 7 modelli su 3 scaffolds. Trovano:

- I fallimenti sono guidati da **errori epistemici** (non sapere qualcosa), non errori esecutivi
- Iniziano tipicamente nei **primi step** dell'esecuzione
- Rimangono **nascosti** fino a quando il recovery non è più possibile
- Una singola decisione sbagliata propaga silenziosamente attraverso decine di azioni successive

Implicazione: migliorare l'affidabilità richiede **validazione e intervento anticipati**, non solo valutazione dell'outcome finale.

## Failure Attribution

Yeh et al. ([[wiki/sources/arxiv-2607-12747-oat-failure-attribution]]) propongono OAT: identificare quale step ha causato il fallimento, senza etichette su traiettorie fallite. Si allena solo su traiettorie di successo, modellando le dinamiche con neural CDE. Ogni step di una traiettoria fallita riceve un anomaly score basato sulla deviazione dalle dinamiche apprese.

- **200-5000x più veloce** dei baseline prompting-based
- **+20% F1** in-domain, **+7% F1** out-of-distribution
- Richiede solo 100 traiettorie di successo per il training

## Connessione a harness design

La failure analysis informa direttamente il [[wiki/pages/harness-design|harness design]]: se i fallimenti iniziano nei primi step e rimangono nascosti, il harness deve costruire gate di verifica anticipati (back pressure, vedi [[wiki/pages/comprehension-debt|comprehension debt]]) anziché solo valutazione finale.
