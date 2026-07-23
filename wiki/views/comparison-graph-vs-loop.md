---
type: view
created: 2026-07-23
updated: 2026-07-23
tags: [comparison, harness, loop, graph, agent-architecture]
kind: comparison
shareable: false
based_on:
  - [[wiki/pages/harness-design]]
  - [[wiki/pages/comprehension-debt]]
  - [[wiki/pages/compositional-generalization]]
  - [[wiki/pages/agent-failure-analysis]]
  - [[wiki/sources/addy-osmani-software-factories]]
  - [[wiki/sources/alex-zhang-harness-2026]]
  - [[wiki/sources/arxiv-2607-12227-harness-evaluation]]
  - [[wiki/sources/arxiv-2607-09510-failure-as-process]]
  - [[wiki/sources/arxiv-2607-12747-oat-failure-attribution]]
---

# Tutto grafo vs Tutto loop: confronto sui paradigmi di agent control

Due estremi architetturali per governare il comportamento degli agenti LLM. Nessuno dei due vince da solo: il confronto mappa i trade-off che Osmani identifica come "dove mettere ogni switch".

## Tabella sinottica

| Dimensione | Tutto loop (agente libero) | Tutto grafo (state machine) |
|------------|---------------------------|---------------------------|
| **Routing** | LLM decide passo per passo | Edge condizionali predefiniti |
| **Struttura** | Emergente, non vincolata | Esplicita, disegnata a priori |
| **Verifica** | Difficile: failure point sparsi | Leggibile: ogni nodo è un gate |
| **Generalizzazione** | Massima libertà, ma context rot | Vincolata ai path sanctioned |
| **Costo setup** | Minimo (prompt + tools) | Alto (disegnare grafo, nodi, edge) |
| **Failure mode** | Silenzioso, tardivo | Visibile, localizzabile |
| **Autonomia** | Illimitata (pericolosa) | Confinata dentro ogni nodo |
| **Bitter lesson** | Allineato: niente hand-coding | Rischia di violarlo |

## Tutto loop: l'agente libero

### Tesi
L'agente riceve un goal, un set di tool, e decide tutto al volo: quale problema inseguire, quale codice cambiare, quali test lanciare, quando dichiarare vittoria ([[wiki/sources/addy-osmani-software-factories|Osmani]]).

### Punti di forza
- **Zero design cost**: niente flowchart, niente state machine, solo prompt
- **Massima flessibilità**: l'agente può adattarsi a qualsiasi situazione
- **Generalizzazione non vincolata**: niente path predefiniti da rispettare
- Zhang ([[wiki/sources/alex-zhang-harness-2026]]) nota che l'over-structuring ("programmatic strategies such as MapReduce or dynamic programming") rischia di "run afoul of the bitter lesson"

### Punti deboli
- **Comprehension debt**: senza gate, il codice generato non viene letto, il debito cresce silenziosamente ([[wiki/pages/comprehension-debt]])
- **Failure invisibili**: Zhao ([[wiki/sources/arxiv-2607-09510-failure-as-process]]) mostra che i failure iniziano nei primi step e propagano silenziosamente. Senza nodi espliciti, non sai dove è morto
- **Context rot**: l'agente accumula contesto, oltre i 20 step perde il filo (Osmani cita Dex Horthy / 12-factor-agents)
- **Nessun back pressure**: senza gate di verifica, l'autonomia supera la capacità di verifica ([[wiki/pages/comprehension-debt|comprehension debt]])
- Wang ([[wiki/sources/arxiv-2607-12227-harness-evaluation]]) mostra che loop con più search budget non battono harness strutturati sotto budget comparabile

## Tutto grafo: la state machine

### Tesi
Ogni step è un nodo esplicito, ogni transizione è un edge condizionale. L'agente è intelligente dentro ogni nodo ma non può uscire dai path sanctioned ([[wiki/sources/addy-osmani-software-factories|Osmani]]).

### Punti di forza
- **Failure point leggibili**: quando una run muore, punti al nodo che l'ha uccisa
- **Check obbligatori**: ogni edge condizionale è un gate. Non puoi saltarlo
- **Back pressure strutturato**: l'autonomia è proporzionale alla verificabilità
- **Costi di verifica bassi**: loop corti (3-10 step) tra nodi sono economici da validare
- Pattern già visibile in LangGraph, LlamaIndex Workflows, Jerry Liu's hybrid workflow-graph

### Punti deboli
- **Costo di design alto**: ogni task richiede un grafo disegnato
- **Generalizzazione limitata**: il grafo è specifico al task, non si trasferisce
- Zhang avverte esplicitamente: l'over-structuring soffoca la compositional generalization. Il suo RLM ottiene generalizzazione vincolando l'osservazione (cosa l'agente vede), non il routing (dove l'agente va)
- **Non previene il root cause**: Zhao mostra che i failure sono epistemici (non sapere qualcosa), non strutturali. Il grafo rende il failure visibile ma non lo risolve
- Wang: mancano prove che il grafo (come harness design) produca gain reali vs simple test-time scaling

## Le quattro tensioni irrisolte

### 1. Routing vs Osservazione
Osmani disciplina il **dove** (grafi, edge condizionali). Zhang disciplina il **cosa** (context offloading, LID). Sono ortogonali: potresti avere entrambi, nessuno, o uno solo. Nessun source nella vault testa la combinazione.

### 2. Visibilità vs Prevenzione
Il grafo rende i failure localizzabili (Zhao, OAT). Ma né il grafo né il loop prevengono il root cause epistemico. OAT ([[wiki/sources/arxiv-2607-12747-oat-failure-attribution|Yeh]]) modella il "flow of success" ma non corregge lo step errato, lo identifica dopo.

### 3. Design vs Search
Wang ([[wiki/sources/arxiv-2607-12227-harness-evaluation|Wang et al.]]) è la critica più dura al grafo: se il gain deriva dalla ricerca addizionale (più tentativi), non dal design del grafo, allora disegnare state machine è fatica sprecata. Osmani non ha questo esperimento di controllo.

### 4. Struttura vs Bitter lesson
Zhang: "make no mistake, doing that we will inevitably run afoul of the bitter lesson". Osmani: "the genuinely new move was trying to throw the diagram away". Sono in diretta contraddizione. Zhang vuole che l'inductive bias viva nel harness ma in forma leggera (LID, context offloading); Osmani vuole grafi pesanti con edge espliciti.

## Sintesi: il modello "switchboard"

Osmani stesso offre la via d'uscita: non "tutto grafo" né "tutto loop", ma decidere **caso per caso** dove mettere ogni switch.

**Domanda operativa per ogni loop:** il check è economico, frequente, e non ingannabile?
- **Sì** → dark (loop libero, automatizzato)
- **No** → lit (grafo con gate di verifica umana)

Il modello non è "quale paradigma" ma "quale switch in quale posizione". La skill richiesta non è architetturale: è sapere dove un errore è costoso e dove non lo è.
