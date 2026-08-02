---
type: source
created: 2026-08-01
updated: 2026-08-01
tags: [agent-behavior, specification, eval, trace-review, format]
source_path: raw/web/agent-behavior/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Agent Behavior

Un formato standard per descrivere il comportamento atteso di un agente AI attraverso interazioni ripetute. Ogni behavior spec è un file Markdown (`BEHAVIOR.md`) in `.agents/behaviors/<name>/`, versionato insieme al codice.

## Tesi centrale

I system prompt dicono al modello come agire a runtime. Le eval testano se il comportamento è avvenuto. Ma manca uno strato intermedio: definire **cosa conta come buon comportamento** prima di misurarlo. Agent Behavior colma questo gap con spec scritte per reviewer, eval author e agent che auditano trace.

## Dimensioni raccomandate

Ogni behavior dovrebbe considerare: **Intent** (perché importa), **Evidence** (cosa ispezionare prima di decidere), **Decision** (cosa inferire), **Execution** (cosa fare), **Recovery** (fallback quando il primo path fallisce), **Failure modes** (cosa prevenire).

## Distinzione chiave: BEHAVIOR.md vs AGENTS.md

`AGENTS.md` è ottimizzato per l'esecuzione runtime (direttive operative, tool-aware). `BEHAVIOR.md` è ottimizzato per la revisione (aspettative durature, failure modes). Il primo cambia quando l'implementazione cambia; il secondo quando lo standard comportamentale cambia.

## Relazione con gli altri artefatti

System prompt (runtime), skills (procedure), tool docs (API), evals (test), trace (record): le behavior spec liinformano tutti ma non li duplicano. Sono lo strato di **intento** che sta sopra l'esecuzione.

## Rilevanza per il vault

Si collega a [[wiki/pages/harness-design]]: il behavior spec è essenzialmente il "cosa" dell'harness separato dal "come". Conferma la tesi di Miessler ([[wiki/sources/danielmiessler-harness-question]]): l'harness ha valore indipendente quando cattura intent (WHAT) non istruzioni (HOW). Si collega anche a [[wiki/pages/agent-failure-analysis]]: i failure modes espliciti nelle spec sono input diretto per eval di failure trajectories.
