---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [compositional-generalization, harness, rlm, inductive-bias, concept]
---

# Compositional Generalization

La capacità di risolvere problemi nuovi componendo concetti familiari. I Transformer sono inaffidabili nel composizionamento: post-training moderno maschera il problema brute-force con più ambienti e orizzonti più lunghi, ma i gain per dati scala hanno ritorni decrescenti senza questa capacità.

## La tesi di Zhang

Zhang ([[wiki/sources/alex-zhang-harness-2026]]) argomenta che la generalizzazione compositiva deve vivere nel [[wiki/pages/harness-design|harness]], non nella rete neurale. Il harness riduce problemi complessi a osservazioni **localmente in-distribution (LID)**: ogni chiamata LM vede un prompt che rientra nella distribuzione di training.

Il RLM (Recursive Language Model) realizza questo tramite:
- **Context offloading**: il contesto specifico del task viene passato come variabile simbolica, il root LM non lo vede
- **Sub-agent programmatici**: i sub-agent sono funzioni in un REPL, gli output restano in variabili, il root LM non vede informazioni task-specifiche

## Risultati sperimentali

Addestrando un RLM su task corti:
- **Length generalization**: generalizza a task 8-32x più lunghi, con eval lift che matcha o supera il train lift
- **Strategy generalization**: generalizza a domini completamente diversi che condividono struttura latente
- Qwen3-30B-A3B con RLM si avvicina o supera GPT-5.5 con RLM harness

## Equivalence Classes

Il RLM induce una relazione di equivalenza ∼_H sugli stati dei task. Task strutturalmente simili cadono nella stessa classe e producono traiettorie quasi identiche token-per-token per il root LM. Questo abilita generalizzazione transitiva: se il sistema risolve X, può risolvere Y.

## Costo

Training RLM è 1.5-3x più lento del Transformer base per i multipli step e sub-call. Ma scala meglio con la complessità del task.
