---
type: page
created: 2026-07-23
updated: 2026-08-20
tags: [harness, agentic, loop, architecture, concept]
---

# Harness Design

Il **harness** è il programma che sta tra l'ambiente esterno e il modello linguistico: decide come codificare lo stato, quali strumenti sono disponibili, cosa sopravvive tra le esecuzioni, e cosa definisce "fatto". Il loop è il comportamento; il harness è l'ambiente in cui quel comportamento gira.

## Cinque visioni + una cornice unificante

**Osmani** ([[wiki/sources/addy-osmani-software-factories]]) definisce il harness come "le pareti attorno al loop": sandbox, tool, memoria, gate di verifica. La qualità del harness determina quanto autonomia puoi delegare. Harness engineering da solo non basta: senza verifica umana (back pressure), si accumula [[wiki/pages/comprehension-debt|comprehension debt]].

**Zhang** ([[wiki/sources/alex-zhang-harness-2026]]) argomenta che il harness dovrebbe portare un **inductive bias di livello superiore**. Un buon harness riduce problemi complessi a osservazioni localmente in-distribution (LID) per ogni singola chiamata LM. L'RLM lo realizza tramite context offloading + sub-agent programmatici, abilitando [[wiki/pages/compositional-generalization|compositional generalization]].

**Wang et al.** ([[wiki/sources/arxiv-2607-12227-harness-evaluation]]) mostrano che l'**harness evolution automatico** non batte semplici baseline di test-time scaling sotto budget comparabili, e generalizza poco a task held-out. Solleva il dubbio che i gain osservati derivino dalla ricerca addizionale, non dal design del harness.

## L'harness come variabile misurata, non solo il modello

**OpenAI** ([[wiki/sources/openai-arc-agi-3-harness]]) dimostra empiricamente che il punteggio di un modello su benchmark è funzione dell'harness tanto quanto del modello. GPT-5.6 Sol su ARC-AGI-3 passa dal 13.3% al 38.3% (3x) abilitando due sole impostazioni: retained reasoning (mantieni i pensieri privati cross-turn invece di scartarli ogni azione) e compaction (summary strutturato invece di rolling truncation FIFO). Output token ridotti 6x. La conclusione: "evals raramente misurano modelli isolati, misurano un pacchetto di scelte meno visibili, API settings, harness design, prompting".

## Behavior localization come bottleneck dell'evoluzione

**Wang et al.** ([[wiki/sources/arxiv-2607.13285-harness-handbook]]) spostano il focus dalla generazione di edit al problema che la precede: trovare tutti i siti di codice che implementano il comportamento target. Nei harness di produzione un comportamento è distribuito su file, funzioni, stage di esecuzione, stati condivisi non-adiacenti. La richiesta di modifica descrive il "cosa", i repo sono organizzati per file/funzione: il mapping cognitivo è il gap reale. La proposta: Harness Handbook (rappresentazione behavior-centric costruita via static analysis + LLM structuring) + Behavior-Guided Progressive Disclosure. L'approccio funziona meglio su cambiamenti sparpagliati, percorsi raramente eseguiti, interazioni cross-modulo. Connette il problema della localizzazione al debito di comprensione ([[wiki/pages/comprehension-debt|comprehension debt]]).

## Harness meno prescrittivi per modelli maturi

**Anthropic** ([[wiki/sources/anthropic-claude-5-context-engineering]]) ha rimosso oltre l'80% del system prompt di Claude Code per Opus 5/Fable 5 senza perdita sulle evals. Lo shift: da rules a judgement, da examples a interface design, da all-upfront a progressive disclosure, da manual memory a auto-memory. I modelli cresciuti rendono la micro-gestione controproducente; il system prompt è parte dell'harness e deve dimagrire con la capability del modello.

## WHAT vs HOW: la chiave di lettura

Miessler ([[wiki/sources/danielmiessler-harness-question]]) fornisce la cornice che risolve la tensione: l'harness è la somma di due metà che invecchiano in direzioni opposte. Il **HOW** (istruzioni operative, step-by-step) marcisce col Bitter Lesson: più smart il modello, più inutili le micro-istruzioni. Il **WHAT** (contesto, intent, identità, criteri di qualità) si apprezza: un modello più smart fa di più con quel contesto. I lab possono post-trainare il HOW nel modello, ma non possono post-trainare IL TUO contesto.

Questo risolve direttamente la tensione ARC-AGI-3 vs Claude 5: retained reasoning preserva il **contenuto del pensiero** (WHAT), la rimozione delle regole alleggerisce i **vincoli operativi** (HOW). Entrambe le direzioni sono corrette perché operano su metà diverse.

Agent Behavior ([[wiki/sources/agent-behavior]]) formalizza questo principio: `BEHAVIOR.md` cattura il WHAT (aspettative durature, failure modes per reviewer), mentre `AGENTS.md` gestisce il HOW (direttive runtime). Lo strato di intento sta sopra l'esecuzione.

## Harness che produce eval

**Trivedy** ([[wiki/sources/vtrivedy-eval-engineering]], thread X lug 2026, ingestato W34) mostra il gradino successivo: l'harness include le skill per costruire le proprie eval. Il prompt di partenza, "create an eval with me", codifica interview-driven come alternativa a oneshot generation: ispeziona l'agente, propone abilità da testare, ne raccomanda una, la costruisce insieme. Formato Harbor per task+verifier. "Verifier design is hard" è il punto di attrito riconosciuto; la domanda aperta del thread (chi verifica il verifier quando modello e contesto generano entrambi?) non ha risposta nel thread.

Interseca tre direttrici: il verification gate di Osmani (back pressure), la lezione ARC-AGI-3 (evals misurano pacchetti modello+harness), e il filone self-improving (Prime `/refine`, Muse co-training). Le eval non sono più solo misurazione esterna: diventano parte del loop che l'harness può estendere.

## Tensione centrale

Il harness deve essere abbastanza strutturato da rendere il comportamento dell'agente prevedibile e verificabile, ma abbastanza flessibile da non soffocare la generalizzazione. Osmani suggerisce **grafi** (state machine con edge condizionali) come via di mezzo tra loop liberi e workflow deterministici. La chiave WHAT/HOW di Miessler risolve la tensione ARC-AGI-3 vs Claude 5: preserva il contenuto del pensiero (WHAT), alleggerisci i vincoli operativi (HOW).

## La sesta visione: l'harness che costruisce sé stesso

**Qwen3.8-Max** ([[wiki/sources/qwen3-8-max]]) introduce un caso qualitativamente nuovo. Nel progetto oh-my-cli, il modello non usa un harness dato: lo **genera come output**. Issue state machine, dispatcher, monitor, watchdog, E2E test trigger, CI gate, session replay: tutto prodotto dall'agente stesso in 16 giorni di esecuzione autonoma (265 commit, 127 PR). Il feedback loop si chiude sull'architettura del loop, non solo sul codice.

Questo va oltre il framework WHAT vs HOW: qui l'harness non è né dato né alleggerito, è **auto-prodotto**. Suggerisce che per modelli sufficientemente capaci il confine tra "programma che gira nel harness" e "programma che scrive il harness" si dissolve. La domanda aperta: un harness auto-prodotto è verificabile? La self-evolution architetturale è esattamente il caso in cui il back pressure di Osmani è più difficile da esercitare.

## LoopX: il control plane externalizzato

**LoopX** ([[wiki/sources/loopx]], Huang Ruiteng 2026) prende la direzione opposta a Qwen: invece di far generare l'harness al modello, lo **externalizza** in un kernel di stato provider-neutral. Il runtime (Codex, Claude Code, Cursor) esegue turni bounded; LoopX possiede obiettivo, gate, evidence, quota, handoff. È implementazione concreta del principio WHAT vs HOW di Miessler: il WHAT (obiettivo, scope, autorità, evidence) vive nel kernel; il HOW (esecuzione del turno) vive nel runtime. Il tick core è minimale: `quota should-run` decide se agire, `todo claim` assegna ownership, `todo update` registra evidence, `quota spend-slot` contabilizza. Il quota system risponde alla domanda di Wang (harness evolution eval): il loop smette di spendere quando non produce transizione utile.

Il contrasto Qwen vs LoopX definisce uno spettro: l'harness può essere generato dal modello (auto-produzione, massima flessibilità, minima governabilità), externalizzato in un control plane (massima governabilità, minima flessibilità), o da qualche parte in mezzo. Dove posizionarsi dipende dalla capability del modello e dal costo del failure.
