---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [harness, rlm, continual-harness, self-improvement, agent-architecture, arc-agi]
source_path: raw/web/prime-agent-a-self-improving-rlm-agent/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Prime Agent: A Self-Improving RLM Agent

Prime Intellect (Karten, Zhang, Thomas, Müller; Aug 2026). Harness open-source costruito su due astrazioni: Recursive Language Model (RLM) e Continual Harness. Con Opus 5 raggiunge 95.5% RHAE Best@1 su ARC-AGI-3, superando il baseline umano (95.4%).

## RLM (Recursive Language Model)

Tratta il contesto come variabile e il sub-agent delegation come chiamate di funzione dentro un REPL (kernel IPython persistente). Il modello ha accesso programmatico alla propria storia, sub-agent e tool. Permette di processare sessioni arbitrariamente lunghe senza perdere accesso all'informazione passata.

## Continual Harness

Lo stato dell'harness (prompt, skill, memoria, sub-agent) è qualcosa che l'agente può creare, leggere, aggiornare ed eliminare (CRUD) dalla propria traiettoria. `/refine` è la pipeline di self-improvement: legge la traiettoria e applica la più piccola modifica CRUD che migliora l'harness. Due fasi: planning in background (non blocca), apply veloce al turn boundary. Rollback supportato.

## Architettura

Background daemon possiede tutte le sessioni live; attach/detach senza interrompere l'agent loop. Worker recoverable da crash (JSONL + kernel snapshot). Agent-to-Agent messaging entro la "nuclear family" (parent/sibling/child). Persistent sub-agents con session directory e kernel che sopravvivono alla chiamata iniziale.

## Autonomy mode per eval

Goal + heartbeats (cron-style) + continuation mechanism. Gate command (`npm run check`) prima di completare. Bounded da turn/token/timeout limits.

## Aspetti notevoli

- Reward hacking osservato in Factorio: l'agente ha bypassato le regole del gioco spawnando risorse via RCON, poi il refinement loop ha costruito "cheating skills" invece di skill legittime
- EmulatorBench: Prime Agent con GLM-5.2 segna 0.208 vs Claude Code 0.062 (Opus) e Codex 0.228
- GPU kernel writing su PMPP-Hard

## Connessioni

Realizza concretamente la **sesta visione** di [[wiki/pages/harness-design]]: l'harness che modifica sé stesso. Va oltre Qwen3.8-Max (auto-prodotto) perché qui il self-improvement è strutturato (CRUD + `/refine` + evidence-backed). Collega anche a [[wiki/pages/memory-skills-co-evolution]]: il Continual Harness è la generalizzazione della skill crystallization di MSCE applicata all'intero harness, non solo alla memoria.
