---
type: view
created: 2026-08-09
updated: 2026-08-09
tags: [slides, self-improvement, harness, continuous-learning, memory, agent-architecture]
kind: slides
shareable: false
based_on:
  - [[wiki/pages/harness-design]]
  - [[wiki/pages/memory-skills-co-evolution]]
  - [[wiki/sources/dwarkesh-era-of-continual-learning]]
  - [[wiki/sources/openai-arc-agi-3-harness]]
  - [[wiki/sources/qwen3-8-max]]
  - [[wiki/sources/anthropic-claude-5-context-engineering]]
  - [[wiki/sources/arxiv-2607.20064-pro-long]]
  - [[wiki/sources/arxiv-2607-16621-msce-memory-skills]]
  - [[wiki/sources/addy-osmani-software-factories]]
  - [[wiki/sources/danielmiessler-harness-question]]
  - [[wiki/sources/prime-agent]]
  - [[wiki/sources/meta-muse-code-spark-1-2]]
  - [[wiki/sources/arxiv-2607.28576-more-reflect-less]]
  - [[wiki/sources/zero-mem]]
---

# Self-Improvement Continuo degli Agenti AI

Slide deck per discorso. Punto di vista: l'agente come sistema che migliora sé stesso nel tempo, su due superfici (modello e harness/memoria).

*Slide breaks: `---`*

---

## Slide 1 — Tesi

**L'agente AI non è un artefatto congelato. È un sistema che migliora sé stesso.**

Due superfici di miglioramento, che operano a velocità e con meccanismi diversi:

- **Modello** (lenti: giorni/settimane) — i pesi si aggiornano dall'esperienza
- **Harness + memoria** (lenti: secondi/turni) — ciò che sopravvive tra le esecuzioni

La separazione tra le due è il nuovo problema di design.

Fonti: [[wiki/sources/dwarkesh-era-of-continual-learning]], [[wiki/sources/openai-arc-agi-3-harness]]

---

## Slide 2 — Lo shift: da train-then-deploy a continual

Il paradigma train-then-deploy è obsoleto.

> Se i pesi si aggiornano quotidianamente dalle sessioni di lavoro, le safety eval pre-deployment perdono senso.

**4 conseguenze** (Dwarkesh, 8 predictions):

- **Regolazione**: ispezioni periodiche su base continua, non eval una-tantum
- **Alignment**: tecniche calibrate su pesi congelati non scalano; più vicino all'educazione che al safety engineering
- **Diversità reale**: esperienze diverse producono AI effettivamente diverse (<5 modelli prominenti oggi, tutti simili)
- **Moat come switching cost**: cambiare modello = licenziare un dipendente con mesi di contesto

[[wiki/sources/dwarkesh-era-of-continual-learning]]

---

## Slide 3 — L'harness è la variabile misurata, non solo il modello

OpenAI su ARC-AGI-3: GPT-5.6 Sol passa dal **13.3% al 38.3%** (3x) cambiando due impostazioni dell'harness, non il modello.

Le due impostazioni:

- **Retained reasoning**: mantieni i pensieri privati cross-turn invece di scartarli a ogni azione
- **Compaction**: summary strutturato invece di rolling truncation FIFO
- Output token ridotti 6x

> "Evals raramente misurano modelli isolati. Misurano un pacchetto di scelte meno visibili: API settings, harness design, prompting."

**Conseguenza per il discorso**: parlare di "migliorare il modello" senza parlare di harness è incompleto.

[[wiki/sources/openai-arc-agi-3-harness]]

---

## Slide 4 — Modello: 3 azioni di self-improvement

Cosa significa migliorare il modello nell'era continual:

**A. Weight updates dal deployment** (Dwarkesh)
Il modello migliore attrae più utenti → più feedback → modello ancora migliore. Data flywheel auto-rafforzante. Anthropic ha usato Mythos internamente 4 mesi prima del release: in regime continual, 4 mesi di gap = 4 mesi di deployment learning persi.

**B. Self-evolving via feedback loop** (Qwen3.8-Max)
Il modello non segue un piano fisso, **self-evolves through feedback loops**. Caso oh-my-cli: 16 giorni autonomi, 265 commit, 127 PR. Non usa un harness dato: lo genera come output.

**C. Continuous learning comportamentale** (Qwen3.8-Max, e-commerce 365 giorni)
Negoziazioni con prezzi di acquisto decrescenti round dopo round. La "memoria" a lungo termine diventa capacità appresa, non solo contesto.

[[wiki/sources/dwarkesh-era-of-continual-learning]], [[wiki/sources/qwen3-8-max]]

---

## Slide 5 — Harness: 3 path indipendenti di self-improvement

Tre realizzazioni indipendenti di "l'harness migliora sé stesso":

**1. Prime Intellect — `/refine` (CRUD minimal)**
RLM + Continual Harness. `/refine` legge la traiettoria e applica **la più piccola modifica CRUD che migliora l'harness**. 95.5% RHAE Best@1 su ARC-AGI-3 con Opus 5, supera la baseline umana.

**2. Meta Muse Code — co-training del harness**
Spark 1.1 genera ambienti di training, valuta candidati per Spark 1.2. Il harness è **co-trained con il modello**. Skill bundled, async background agents, local event log.

**3. Qwen3.8-Max — harness auto-prodotto**
Il modello genera issue state machine, dispatcher, monitor, watchdog, E2E, CI gate. Il feedback loop si chiude sull'architettura del loop, non solo sul codice.

**Domanda aperta**: un harness auto-migliorante è verificabile?

[[wiki/sources/prime-agent]], [[wiki/sources/meta-muse-code-spark-1-2]], [[wiki/sources/qwen3-8-max]]

---

## Slide 6 — Lo spettro: dove posizionarsi

Le 3 realizazioni di self-improvement non sono equivalenti. Si dispongono su uno spettro:

```
auto-prodotto ←───────────────→ externalizzato
   (Qwen)        (Prime/Muse)      (LoopX, Kiro)
massima flessione    ← gradi di libertà multipli →    massima governabilità
minima governabilità                              minima flessione
```

- **Dove posizionarsi dipende da**: capability del modello × costo del failure
- **Il filo conduttore**: l'harness non è più un artefatto fisso, è una superficie di design

Nota: Kiro (harness come processo server standalone, Agent Client Protocol) e LoopX (control plane provider-neutral) sono ai due estremi della governabilità.

[[wiki/pages/harness-design]]

---

## Slide 7 — Cosa NON funziona: la self-reflection debunked

More-Reflect-Less (36 confronti controllati, 10 reliably peggiori, 18/18 self-inspection negativi):

- **Self-Refine, Reflexion, debate** perdono contro repeated sampling a pari costo token
- Un modello che rilegge il proprio scratchpad **usa gli stessi pesi che hanno prodotto l'errore**
- Il budget è meglio speso in un ulteriore tentativo

**Perché importa per il discorso**: il self-improvement non è introspezione. È:
- cambio dei pesi (modello), oppure
- cambio dell'ambiente (harness/memoria)

I loop introspectivi sono HOW che non paga.

[[wiki/sources/arxiv-2607.28576-more-reflect-less]]

---

## Slide 8 — Memoria: 4 paradigmi di "cosa sopravvive"

La domanda unificante: **cosa sopravvive tra le esecuzioni, e come si recupera?**

Quattro risposte nella letteratura recente:

| Paradigma | Meccanismo | Rappresentante |
|---|---|---|
| **Cristallizzare** | tracce → skill eseguibili | MSCE (L1/L2/L3 + skill crystallization) |
| **Codificare** | persistenza via codice (grep/regex) | PRO-LONG (+18pt ARC-AGI-3) |
| **Automatizzare** | l'agente decide cosa ricordare | Claude 5 (auto-memory) |
| **Pre-strutturare** | grafo deterministico, zero LLM | Zero-Mem (entity-context + temporal hierarchy) |

**Insight**: ognuno sposta il costo. MSCE paga in reflection, PRO-LONG in search, Claude 5 in trust, Zero-Mem in pre-structure.

[[wiki/pages/memory-skills-co-evolution]], [[wiki/sources/arxiv-2607-16621-msce-memory-skills]], [[wiki/sources/arxiv-2607.20064-pro-long]], [[wiki/sources/zero-mem]]

---

## Slide 9 — La chiave di lettura: WHAT vs HOW

Miessler risolve la tensione ARC-AGI-3 vs Claude 5:

- **HOW** (istruzioni operative, step-by-step) **marcisce col Bitter Lesson**
  - più smart il modello, più inutili le micro-istruzioni
  - i lab possono post-trainare il HOW nel modello
- **WHAT** (contesto, intent, identità, criteri di qualità) **si apprezza**
  - un modello più smart fa di più con quel contesto
  - i lab non possono post-trainare IL TUO contesto

**Mappa sul self-improvement**:

- Retained reasoning (ARC-AGI-3) preserva il **WHAT**: il contenuto del pensiero
- Rimozione delle regole (Claude 5) alleggerisce il **HOW**: i vincoli operativi
- Self-reflection (debunked) è HOW che non paga

[[wiki/sources/danielmiessler-harness-question]], [[wiki/pages/harness-design]]

---

## Slide 10 — Il vincolo: back pressure

Osmani: **puoi delegare solo l'autonomia che puoi verificare a basso costo e alta frequenza.**

> Volume non è il problema. Il surplus di PR cattivi è il problema. L'autonomia non può espandere oltre la capacità di verifica.

**Loop guadagna automazione piena solo se**:
- il check è cheap
- gira ad alta frequenza
- non è facilmente falsificabile
- loop corti (3-10 step) verificano meglio di quelli sprawl (20+)

**La tensione centrale del self-improvement**: il caso in cui il back pressure è più difficile da esercitare è **esattamente** la self-evolution architetturale (Qwen). L'harness scrive sé stesso, ma chi verifica l'harness?

[[wiki/sources/addy-osmani-software-factories]], [[wiki/pages/harness-design]]

---

## Slide 11 — Sintesi: la mappa del discorso

```
                SELF-IMPROVEMENT CONTINUO
                          │
            ┌─────────────┴─────────────┐
         MODELLO                  HARNESS + MEMORIA
            │                            │
   weight updates             3 path self-improvement
   (continual)               (Prime / Muse / Qwen)
            │                            │
   self-evolving              4 paradigmi memoria
   feedback (Qwen)           (MSCE / PRO-LONG /
            │                 Claude 5 / Zero-Mem)
            │                            │
            └─────────────┬──────────────┘
                          │
                  COSA NON FUNZIA
              self-reflection (debunked)
                          │
                  CHIAVE WHAT vs HOW
                  (apprezza / marcisce)
                          │
                  VINCOLO: back pressure
              (verifica < autonomia)
```

---

## Slide 12 — Domanda finale

**Un sistema che migliora sé stesso è ancora sotto controllo?**

Tre casi, tre risposte diverse:

- **Prime `/refine`**: la più piccola modifica CRUD. Auditable per costruzione.
- **Muse co-training**: black box, ma il delta è misurato.
- **Qwen auto-prodotto**: il feedback loop si chiude sull'architettura. Il back pressure di Osmani è massimo qui.

La traiettoria è chiara: l'agente del 2026 non è un artefatto, è un processo. Il design della sua capacità di migliorare è il nuovo lavoro.

---

## Fonti (tutto citato nel vault)

- [[wiki/sources/dwarkesh-era-of-continual-learning]] — Dwarkesh, 8 predictions for continual learning
- [[wiki/sources/openai-arc-agi-3-harness]] — OpenAI, harness è la variabile misurata
- [[wiki/sources/qwen3-8-max]] — self-evolving harness auto-prodotto
- [[wiki/sources/anthropic-claude-5-context-engineering]] — 80% system prompt rimosso
- [[wiki/sources/arxiv-2607.20064-pro-long]] — programmatic memory, +18pt ARC-AGI-3
- [[wiki/sources/arxiv-2607-16621-msce-memory-skills]] — MSCE, L1/L2/L3 + skill crystallization
- [[wiki/sources/addy-osmani-software-factories]] — back pressure, comprehension debt
- [[wiki/sources/danielmiessler-harness-question]] — WHAT vs HOW
- [[wiki/sources/prime-agent]] — `/refine` self-improvement CRUD
- [[wiki/sources/meta-muse-code-spark-1-2]] — harness co-trained
- [[wiki/sources/arxiv-2607.28576-more-reflect-less]] — self-reflection debunked
- [[wiki/sources/zero-mem]] — memoria senza LLM, grafo deterministico
- [[wiki/pages/harness-design]] — pagina concettuale (7 visioni)
- [[wiki/pages/memory-skills-co-evolution]] — pagina concettuale (4 paradigmi)
