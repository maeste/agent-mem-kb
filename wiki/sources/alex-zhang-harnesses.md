---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [agents, harnesses, compositional-generalization, rlm, post-training]
source_path: raw/web/alex-l-zhang-language-model-harnesses-are-compositional-generalizers/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Language Model Harnesses Are Compositional Generalizers

Post di Alex L. Zhang (MIT OASIS, 20 lug 2026) sul ruolo degli harness nell'abilitare compositional generalization per agent LLM.

## Tesi centrale

I Transformer sono poveri di **compositional generalization** (risolvere problemi unseen componendo quelli familiari). L'harness non e solo plumbing; e il veicolo per **inductive bias di alto livello** che riduce problemi complessi a composizioni di sottoproblemi in-distribution per il neural network [[raw/web/alex-l-zhang-language-model-harnesses-are-compositional-generalizers/index.md]].

## Cosa fa un buon harness

Un buon harness forma ogni chiamata LLM per osservazioni **localmente in-distribution (LID)**: ogni singola chiamata Transformer handle un prompt che e in-distribution rispetto ai suoi dati di training [[raw/web/alex-l-zhang-language-model-harnesses-are-compositional-generalizers/index.md]].

Gli harness esistenti (Claude Code, Codex) falliscono qui: flooding del context window con task-specific info, tool outputs, reasoning che porta a **context rot** (l'history cresce OOD).

## Recursive Language Model (RLM)

Architettura harness proposta con due componenti chiave:

1. **Context offloading**: input-specific context passato come variabile simbolica; root LM call non lo vede direttamente
2. **Programmatic sub-agent calling**: sub-agent e tools trattati come funzioni in un code REPL; root LM sceglie selettivamente info senza mai vedere sub-call outputs

### Risultati sperimentali

- Training esclusivamente su **task brevi**, generalizza a task **8-32x piu lunghi** con ~10x eval lift rispetto a training diretto del Transformer [[raw/web/alex-l-zhang-language-model-harnesses-are-compositional-generalizers/index.md]]
- Cross-domain transfer: training su un dominio trasferisce meglio ad altri domini rispetto a vanilla Transformer
- Su diversi task, RLM con Qwen3-30B avvicina o supera GPT-5.5 sul long eval
- Costo runtime 1.5-3x rispetto a Transformer baseline, ma scala meglio con complessita task

## Equivalenza di task (isomorfismo)

L'RLM induce relazione di equivalenza ~_H su task states: task strutturalmente simili cadono nella stessa classe di equivalenza. Il root LM vede traiettorie **token-for-token simili** per task diversi ma decomponibilmente equivalenti.

## Mismanaged Geniuses Hypothesis (MGH)

I Transformer sono "geni mal gestiti": potenti ma inaffidabili su compositional generalizzazione. Gli inductive biases attuali (geometrici, basso livello) non bastano; servono inductive bias di **piu alto livello di astrazione**, encodabili nel linguaggio e allenabili end-to-end con RL.
