---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [model-capability, math, astra, openai, reasoning, verification, frontier]
source_path: raw/web/openais-unreleased-model-astra-solves-ten-major-open-mathematics-problems/index.md
ingested: 2026-W31 (Sat-Sat)
---

# OpenAI's Unreleased Model Astra Solves Ten Major Open Mathematics Problems

Zvi (Don't Worry About the Vase, Aug 2026). Analisi dell'annuncio OpenAI: Astra (modello non rilasciato) ha risolto 10 problemi matematici aperti per ~$2.000 di token (tariffe Sol API).

## I 10 risultati

Sphere packing (upper bounds al Cohn-Elkies threshold), binary/spherical codes (bounds exponentially improved), non-sofic groups (existence construction), Connes rigidity conjecture (disproof), arithmetic circuit complexity (lower bounds permanent), quantum parallel repetition (exponential theorem), closest vector problem (hardness of approximation), Ehrhart volume conjecture, multicolor Ramsey numbers (superexponential lower bound, Erdős 183), extremal number conjectures (Erdős 146 e 180).

Tutti formalizzati in Lean certificate.

## Tesi di Zvi

- AI è ora superumana in math/cyber/coding nei domini verificabili, distinto da superintelligenza
- "The Juice": Astra può puntare a problemi aperti e crackarne alcuni; Fable/Sol puntati agli stessi problemi li risolvono a volte (proof overhang), ma non vanno a cercarli autonomamente allo stesso livello
- Verifiability è il fattore abilitante: i risultati condividono definizione formale, formalizzazione Lean, teoria circostante disponibile, poco attention umano
- Update: timelines leggermente più veloci, più automazione AI R&D sooner, meno probabilità di wall
- Rischio: mondo di "benchmaxxers" dove ciò che è formalmente misurabile viene massimizzato, ciò che richiede human-in-the-loop resta indietro (Goodhart on steroids)

## Reazioni notevoli

- **Henry Yuen** (ha lavorato su quantum parallel repetition): la prova parte dal suo lavoro ma va oltre; il writeup seppellisce il technical crux senza fanfare; Lean proof non dà understanding
- **Elliot Glazer**: Astra probabilmente non è step change oltre Sol; o3 e Sol sono stati gli step changes reali in math autonomo
- **Levent Alpoge**: Fable risolve 5/10 in 24h con setup autonomico generico, no internet
- **Gary Marcus**: mezzo dei problemi risolvibili da Fable, OpenAI non ha avuto control group
- **Tamay Besiroglu** vince bet con Daniel Litt (Annals-quality math by 2030): risolto nel 2026 a costo molto inferiore
- Daniel Litt concede la bet

## Domanda aperta

Verificazione spesso non più facile della generazione. I risultati hanno caratteristiche comuni (well-defined, formalizzabili, teoria disponibile). Resta da vedere se si estende a domini non verificabili.

## Connessioni

Esempio paradigmatico di capability frontier in domini verificabili. Il thread sulla verification come abilitante connette a [[wiki/pages/harness-design]]: i benchmark ARC-AGI-3 verificabili permettono di misurare harness design, ma i domini non verificabili (taste, judgment) restano il gap. La questione "il modello non sa quali parti della proof sono hard quando spiega" collega a [[wiki/pages/comprehension-debt|comprehension debt]].
