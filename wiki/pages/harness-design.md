---
type: page
created: 2026-07-23
updated: 2026-08-01
tags: [harness, agentic, loop, architecture, concept]
---

# Harness Design

Il **harness** è il programma che sta tra l'ambiente esterno e il modello linguistico: decide come codificare lo stato, quali strumenti sono disponibili, cosa sopravvive tra le esecuzioni, e cosa definisce "fatto". Il loop è il comportamento; il harness è l'ambiente in cui quel comportamento gira.

## Tre visioni complementari

**Osmani** ([[wiki/sources/addy-osmani-software-factories]]) definisce il harness come "le pareti attorno al loop": sandbox, tool, memoria, gate di verifica. La qualità del harness determina quanto autonomia puoi delegare. Harness engineering da solo non basta: senza verifica umana (back pressure), si accumula [[wiki/pages/comprehension-debt|comprehension debt]].

**Zhang** ([[wiki/sources/alex-zhang-harness-2026]]) argomenta che il harness dovrebbe portare un **inductive bias di livello superiore**. Un buon harness riduce problemi complessi a osservazioni localmente in-distribution (LID) per ogni singola chiamata LM. L'RLM lo realizza tramite context offloading + sub-agent programmatici, abilitando [[wiki/pages/compositional-generalization|compositional generalization]].

**Wang et al.** ([[wiki/sources/arxiv-2607-12227-harness-evaluation]]) mostrano che l'**harness evolution automatico** non batte semplici baseline di test-time scaling sotto budget comparabili, e generalizza poco a task held-out. Solleva il dubbio che i gain osservati derivino dalla ricerca addizionale, non dal design del harness.

## L'harness come variabile misurata, non solo il modello

**OpenAI** ([[wiki/sources/openai-arc-agi-3-harness]]) dimostra empiricamente che il punteggio di un modello su benchmark è funzione dell'harness tanto quanto del modello. GPT-5.6 Sol su ARC-AGI-3 passa dal 13.3% al 38.3% (3x) abilitando due sole impostazioni: retained reasoning (mantieni i pensieri privati cross-turn invece di scartarli ogni azione) e compaction (summary strutturato invece di rolling truncation FIFO). Output token ridotti 6x. La conclusione: "evals raramente misurano modelli isolati, misurano un pacchetto di scelte meno visibili — API settings, harness design, prompting".

## Behavior localization come bottleneck dell'evoluzione

**Wang et al.** ([[wiki/sources/arxiv-2607.13285-harness-handbook]]) spostano il focus dalla generazione di edit al problema che la precede: trovare tutti i siti di codice che implementano il comportamento target. Nei harness di produzione un comportamento è distribuito su file, funzioni, stage di esecuzione, stati condivisi non-adiacenti. La richiesta di modifica descrive il "cosa", i repo sono organizzati per file/funzione: il mapping cognitivo è il gap reale. La proposta: Harness Handbook (rappresentazione behavior-centric costruita via static analysis + LLM structuring) + Behavior-Guided Progressive Disclosure.

## Harness meno prescrittivi per modelli maturi

**Anthropic** ([[wiki/sources/anthropic-claude-5-context-engineering]]) ha rimosso oltre l'80% del system prompt di Claude Code per Opus 5/Fable 5 senza perdita sulle evals. Lo shift: da rules a judgement, da examples a interface design, da all-upfront a progressive disclosure, da manual memory a auto-memory. I modelli cresciuti rendono la micro-gestione controproducente; il system prompt è parte dell'harness e deve dimagrire con la capability del modello.

## Tensione centrale

Il harness deve essere abbastanza strutturato da rendere il comportamento dell'agente prevedibile e verificabile, ma abbastanza flessibile da non soffocare la generalizzazione. Osmani suggerisce **grafi** (state machine con edge condizionali) come via di mezzo tra loop liberi e workflow deterministici. Le nuove fonti complicano il quadro: l'evidenza ARC-AGI-3 (retained reasoning) suggerisce che più memoria cognitiva = meglio, mentre l'evoluzione di Claude Code (rimozione regole) suggerisce meno prescrizione = meglio. La risoluzione: distinguere tra **contenuto del pensiero** (da preservare) e **vincoli sul comportamento** (da alleggerire).
