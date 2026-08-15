---
type: source
created: 2026-08-08
updated: 2026-08-08
tags: [harness, loop-engineering, control-plane, agent-teams, long-running, open-source]
source_path: raw/web/github-huangruiteng-loopx-lightweight-loop-engineering-state-kernel-for-long-run/index.md
ingested: 2026-W31 (Sat-Sat)
---

# LoopX: loop engineering state kernel for long-running agents

Huang Ruiteng (GitHub, repo attivo dal mag 2026). Open source, MIT, Python 3.11+, zero dipendenze runtime fuori stdlib.

## Tesi centrale

Agent runtime e control plane sono cose diverse. Codex, Claude Code, Cursor eseguono turni bounded; **LoopX** possiede lo **stato di controllo durevole** che permette al lavoro di continuare across turni, tool, agenti e sessioni. Non è un agent framework né un orchestration runtime: è lo strato che governa obiettivi, gate, evidence, quota e handoff.

## Modello mentale

Agent-native Kanban: le card trasportano identità, autorità, evidence, continuazione. Le mosse sono operatori validati (claim, gate, monitor, writeback). Il board è una proiezione; lo stato LoopX resta source of truth.

## Cinque domande del control plane

| Domanda | Cosa tiene visibile |
|---------|---------------------|
| Qual è l'obiettivo? | Goal attivo, scope esplicito, autorità corrente |
| Cosa succede dopo? | Todo ordinati (user + agent), ownership, claim, lease |
| Cosa serve giudizio umano? | User gate concreti, non "waiting for owner" vago |
| Quale evidence è cambiata? | Run history compatta, validazione, blocker, writeback |
| Il loop può continuare? | Quota, capability, safe fallback, scheduler hint, stop condition |

## Tick core

```
loopx quota should-run      # l'agente registrato deve agire ora?
loopx todo claim            # chi possiede questo slice?
loopx todo update           # cosa è cambiato?
loopx refresh-state         # cosa deve vedere il prossimo turn?
loopx quota spend-slot      # contabilizza uno slice completato
```

## Architettura

Execution path: `Agent -> Capability -> Provider`. Control path: `Provider readback -> Capability transition -> Kernel`. Il Kernel possiede todo, gate, monitor, writeback, quota, recovery, scheduling. Le Capability normalizzano output del provider e propongono transizioni tipate.

## Evidenza

- OpenViking contribution arc: 200+ ore elapsed, PR delivery + fix knowledge reusable
- Auto ML showcase (redacted): 200+ ore, ipotesi/evidence/promotion gates in un grafo
- KNN demo riproducibile: proposer/executor/evaluator agenti in parallelo
- Utente indipendente: 13h+ C++ accuracy run, 4 giorni unattended, 7 PR merged (1B+ token scale)

Elapsed lifetime = wall-clock project time, non 200 ore di compute continuo.

## Connessioni

LoopX è **implementazione concreta** del principio WHAT vs HOW di [[wiki/sources/danielmiessler-harness-question|Miessler]]: il kernel trattiene il WHAT (obiettivo, scope, gate, evidence, autorità) mentre il runtime esegue il HOW (turni bounded). La separazione control-plane/runtime formalizza architetturalmente ciò che Miessler descrive come tensione risolta.

Collega anche a [[wiki/sources/arxiv-2607-09510-failure-as-process|failure-as-process]]: LoopX esplicita evidence log e verifiable handoff proprio per rendere i failure inspectable across turni, il gap identificato nello studio CLI agent. Il quota system risponde alla domanda di [[wiki/sources/arxiv-2607-12227-harness-evaluation|Wang eval]]: quando un agent non produce transizione utile, il loop smette di spendere (stop condition).

Contrasto con [[wiki/sources/qwen3-8-max|harness auto-prodotto di Qwen]]: LoopX è harness esternalizzato e provider-neutral, Qwen genera l'harness come output del modello. Due risposte opposte alla stessa domanda: come governare loop lunghi.
