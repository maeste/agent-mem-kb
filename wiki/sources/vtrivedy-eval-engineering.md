---
type: source
created: 2026-08-20
updated: 2026-08-20
tags: [agent-evals, eval-driven-development, harbor, langchain, harness, interview]
source_path: raw/web/Vtrivedy10-2079976006644072796/index.md
ingested: 2026-W34 (Sat-Sat)
---

# Viv Trivedy (LangChain): eval-engineering skill, thread X

Thread X (22 lug 2026, @Vtrivedy10, LangChain). Annuncio dell'**eval-engineering skill** per lo sviluppo agenti eval-driven: si costruiscono eval insieme all'utente invece di generarle one-shot. 696 likes, 66 RT al fetch.

## Contenuto

L'idea centrale emersa dal thread e dalle risposte dell'autore:

- **Prompt di partenza** (condiviso da Trivedy su richiesta): "Use the eval-engineering skill to create an eval with me. Inspect the agent first, propose a few abilities worth testing, recommend one and then we can build it together"
- **Formato Harbor**: la skill produce eval in formato Harbor. Trivedy: il formato "forces us humans to explicitly interact with both task and verifier design → verifier design is hard"
- **Utenti simulati**: per skill multi-turno che "intervistano" l'utente, la risposta è "simulated users of pre-spec'd responses" (in arrivo nella skill)
- **Roadmap** dichiarata: simulazione fedele di utenti calibrata sulle tracce, miglior generazione di ambienti sintetici per evitare divergenza eval env vs prod env, estensione verso post-training

## Punti sollevati dal thread

- @EnglessonElias: "Interviewing the user instead of oneshot eval gen feels like the key design choice"
- @FanofAITech: "Evals are training data for agents"
- @rohit9m (domanda senza risposta nel thread): se lo stesso modello+contesto scrive task e verifier, come si garantisce che il verifier sia corretto "at birth" e resti corretto? Serve calibrazione contro tracce known-good/known-bad?
- @htahir111: Harbor sta emergendo come formato standard; auspica convergenza con l'ecosistema Prime Intellect (PI ha già integrazione Harbor, confermata da Trivedy)

## Connessioni

- Il prompt "create an eval **with me**" è back pressure applicata alla costruzione di eval: stessa famiglia del verification gate di Osmani in [[wiki/sources/addy-osmani-software-factories|Osmani]] e di [[wiki/pages/comprehension-debt|comprehension debt]]
- "Verifier design is hard" e la domanda di @rohit9m riecheggiano la scoperta ARC-AGI-3 ([[wiki/sources/openai-arc-agi-3-harness|OpenAI]]): evals misurano pacchetti modello+harness, e il verifier è parte dell'harness
- L'ecosistema Harbor/Prime Intellect collega a [[wiki/sources/prime-agent|Prime Agent]] (Continual Harness, RHAE benchmark)
