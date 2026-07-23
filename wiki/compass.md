---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [reflection]
---

# Compass

Riflessione sulla vault. Aggiornato a ogni sessione reflect.

## Dove sta andando il pensiero

Il batch iniziale di 11 source rivela un focus chiaro su due assi: **(1) come costruire agent LLM affidabili** (harnesses, memory/skills, failure analysis, software factories) e **(2) come stanno evolvendo i modelli frontier** (MoE sparsificazione, Gemini family expansion, routing multi-modello). C'e un filo conduttore che attraversa entrambi: la tensione tra capacita di generazione (sempre maggiori) e capacita di verifica/controllabilita (il collo di bottiglia reale). Sia Osmani (back pressure principle) che Zhang (harnesses per LID) che il paper harness evolution evaluation puntano tutti nella stessa direzione: il problema non e generare meglio, e progettare sistemi dove la generazione sia verificabile.

## Cosa non sto guardando

- **AI safety/alignment oltre l'incidente OpenAI/HF**: un solo source tocca sicurezza; manca letteratura su red-teaming, interpretability, governance
- **Applicazioni verticali**: healthcare, finance, scientific discovery — nessun source applicativo
- **Open source ecosystem beyond models**: tooling, frameworks, eval benchmarks dettagliati
- **Hardware/infrastruttura**: come impattano i trend MoE (storage demand) sulle scelte infrastrutturali reali
- **Economico/business model**: pricing trends, cost dynamics di serving MoE a scale

## Una domanda worth sitting with

Se i Transformer sono intrinsecamente poveri di compositional generalizzazione (MGH hypothesis), e l'harness e il vero veicolo per inductive bias di alto livello, allora cosa significa per il ruolo dell'architettura neurale stessa vs l'architettura del sistema che la avvolge? Stiamo spostando l'innovazione dal modello al harness, o stiamo solo scoprendo che il harness era sempre dove abitava l'intelligenza?
