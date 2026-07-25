---
type: page
created: 2026-07-23
updated: 2026-07-25
tags: [harness, agentic, loop, architecture, concept]
---

# Harness Design

Il **harness** è il programma che sta tra l'ambiente esterno e il modello linguistico: decide come codificare lo stato, quali strumenti sono disponibili, cosa sopravvive tra le esecuzioni, e cosa definisce "fatto". Il loop è il comportamento; il harness è l'ambiente in cui quel comportamento gira.

## Tre visioni complementari

**Osmani** ([[wiki/sources/addy-osmani-software-factories]]) definisce il harness come "le pareti attorno al loop": sandbox, tool, memoria, gate di verifica. La qualità del harness determina quanto autonomia puoi delegare. Harness engineering da solo non basta: senza verifica umana (back pressure), si accumula [[wiki/pages/comprehension-debt|comprehension debt]].

**Zhang** ([[wiki/sources/alex-zhang-harness-2026]]) argomenta che il harness dovrebbe portare un **inductive bias di livello superiore**. Un buon harness riduce problemi complessi a osservazioni localmente in-distribution (LID) per ogni singola chiamata LM. L'RLM lo realizza tramite context offloading + sub-agent programmatici, abilitando [[wiki/pages/compositional-generalization|compositional generalization]].

**Wang et al.** ([[wiki/sources/arxiv-2607-12227-harness-evaluation]]) mostrano che l'**harness evolution automatico** non batte semplici baseline di test-time scaling sotto budget comparabili, e generalizza poco a task held-out. Solleva il dubbio che i gain osservati derivino dalla ricerca addizionale, non dal design del harness.

**Wang et al. (Harness Handbook)** ([[wiki/sources/arxiv-2607-13285-harness-handbook]]) attaccano il passo prerequisito: prima di evolvere un harness, bisogna trovare dove intervenire. Definiscono la **behavior localization** come il collo di bottiglia, e propongono una rappresentazione behavior-centric (organizzata per comportamenti, non per file) costruita via analisi statica + LLM. L'approccio funziona meglio su cambiamenti sparpagliati, percorsi raramente eseguiti, interazioni cross-modulo. Connette il problema della localizzazione al debito di comprensione ([[wiki/pages/comprehension-debt|comprehension debt]]).

## Tensione centrale

Il harness deve essere abbastanza strutturato da rendere il comportamento dell'agente prevedibile e verificabile, ma abbastanza flessibile da non soffocare la generalizzazione. Osmani suggerisce **grafi** (state machine con edge condizionali) come via di mezzo tra loop liberi e workflow deterministici.
