---
type: source
created: 2026-08-01
updated: 2026-08-01
tags: [harness, intent-engineering, bitter-lesson, what-vs-how, concept]
source_path: raw/web/the-answer-to-the-harness-question/index.md
ingested: 2026-W30 (Sat-Sat)
---

# The Answer to the Harness Question

Risposta di Daniel Miessler al dibattito di Martin Casado sull'indipendenza del valore dell'harness dal modello.

## Tesi centrale

L'harness non è una cosa sola. È la somma di due metà che invecchiano in direzioni opposte:

- **HOW** (istruzioni step-by-step): marcisce. È il Bitter Lesson di Sutton che si ripete nei config file. Più smart il modello, più stupide le istruzioni выглядят. Se l'harness è soprattutto HOW, meno harness è meglio.
- **WHAT** (contesto: chi sei, cosa stai facendo, cosa significa "buono"): si apprezza. Un modello più smart fa di più con quel contesto, non meno. Se l'harness è soprattutto WHAT, ha valore indipendente che cresce ad ogni release.

## Risposta ai tre beliefs di Casado

1. "Less harness, better" — giusto per la metà HOW.
2. "Model providers post-train the harness into the model" — giusto per HOW, sbagliato per WHAT. I lab possono migliorare l'agenticità, ma non possono post-trainare IL TUO contesto nel modello.
3. "Harnesses have real independent value" — giusto per la metà WHAT.

## Intent Engineering

Il principio di design: catturare cosa l'umano vuole, trasmetterlo al modello ad ogni task, e per il resto stare fuori dal modo del modello per l'esecuzione.

## Rilevanza per il vault

Questa è la chiave di lettura che collega direttamente [[wiki/pages/harness-design]] e risolve la tensione centrale tra "più memoria cognitiva = meglio" (ARC-AGI-3) e "meno prescrizione = meglio" (Claude 5). La risposta: preserva il WHAT (contenuto del pensiero, intent, memoria), alleggerisci il HOW (regole operative, istruzioni step-by-step). Conferma anche il principio di [[wiki/sources/agent-behavior]]: behavior spec catturano il WHAT, non il HOW.
