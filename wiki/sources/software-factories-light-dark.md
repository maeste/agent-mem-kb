---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [ai-coding, software-factories, agents, software-engineering]
source_path: raw/web/software-factories-light-and-dark/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Software Factories, Light and Dark

Articolo di Addy Osmani (22 lug 2026) sulla metafora della "fabbrica software" per sistemi agentic di generazione codice.

## Architettura della factory

Tre concetti stratificati [[raw/web/software-factories-light-and-dark/index.md]]:
- **Loop**: unita atomica, un agent che ripete: gather context -> action -> check result -> repeat
- **Harness**: le pareti attorno al loop (sandbox, tools, memory persistente, gate di "done")
- **Factory**: molti harnessed loops in parallelo, alimentati da una queue, drenati through un review gate verso production

La factory non e un agent piu grande; e un **org chart fatto di loop**.

## Dark vs Light Factory

- **Dark factory**: code ships che nessun umano ha letto, verificato solo da macchine. Metafora dalle fabbriche lights-out (FANUC 2001, Xiaomi 2024) [[raw/web/software-factories-light-and-dark/index.md]]
- Facile da avviare, ma accumula **comprehension debt**: il divario tra quanto codice esiste e quanto un umano comprende
- Dopo ~4 mesi di dark factory completa (esperienza riportata da Dex), serve debugging manuale doloroso
- **Light factory**: stessa pipeline ma giudizio umano upstream (design, architettura) + review prima di ship
- La safety net e architettura ordinaria: tipi, test seams, call stack corte, boundary nette, dependency injection

## Back pressure principle

- **Il collo di bottiglia non e mai la generazione, ma la verifica**
- Regola: autonomia del loop non puo espandere oltre cio che si puo verificare cheap e reliable
- Loop corti (3-10 step) sono verificabili; loop lunghi (>20 step) perdono il filo e nascondono errori
- Un loop guadagna status fully automated solo se il check e cheap, high-frequency, e non falsificabile

## Grafi vs loop

- I loop dovrebbero camminare su grafi predefiniti (state machines, conditional edges) invece di scegliere il path tool call by tool call
- Pattern visibile in LangGraph, LlamaIndex Workflows, actor model
- Citazione chiave: "mostly deterministic code, with LLM steps sprinkled in at just the right points"
