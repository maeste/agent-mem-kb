---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [self-refine, reflexion, test-time-scaling, repeated-sampling, agent-loop, paper]
source_path: raw/papers/arxiv-2607.28576.pdf
ingested: 2026-W31 (Sat-Sat)
---

# More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost

Mirzaei et al. (Stony Brook, Jul 2026). Uno studio controllato che testa se i metodi di self-reflection (Self-Refine, Reflexion, debate, ecc.) battono il repeated sampling quando il costo in token è pareggiato.

## Setup

Sette metodi, modelli open (1.5B, 3B, 7B), due benchmark matematici, 150 domande ciascuno. Ogni token generato contato, inclusi quelli spesi in critique/reflection/debate/checking. Ogni metodo confrontato con repeated sampling al proprio costo misurato, paired per domanda, con bootstrap intervals e correzione per molteplicità.

## Risultati

- **Nessun metodo** è reliablemente migliore del repeated sampling a pari costo in nessun setting (36 confronti)
- **Dieci sono reliably peggiori**, tutti metodi dove il modello ispeziona il proprio output
- Tutti i **18 confronti di self-inspection** sono negativi
- Self-Refine e forced Reflexion perdono 3.6-10.1pt vs baseline a 7B
- Reflexion sul modello 1.5B non ha mai attivato un retry: si giudicava sempre corretto

## Connessioni

Conferma empiricamente che i loop di self-reflection non aggiungono segnale: un modello che rilegge il proprio scratchpad usa gli stessi pesi che hanno prodotto l'errore. Il budget è meglio speso in un ulteriore tentativo o in uno script di riproduzione fallimentare. Connette a [[wiki/pages/agent-failure-analysis]] (errori epistemici non risolti dal ributtare lo stesso modello sul problema) e a [[wiki/pages/harness-design]] (i loop introspectivi sono HOW che non paga).

## Discussione (X thread @omarsar0)

Il thread di [[raw/web/unknown-2084761324786172347/index]] riassume il paper. Osservazioni notevoli dai reply: il risultato si applica ai loop introspectivi, non all'execution loop che incorpora nuova evidence (IronstarAI); il baseline vince per majority vote che richiede una risposta verificabile, quindi potrebbe non trasferirsi a task open-ended (RabnoorSingh10); senza modelli frontier testati resta aperto se la self-reflection emerga a scala maggiore (MKhordoo).
