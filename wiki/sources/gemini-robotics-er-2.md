---
type: source
source_path: raw/web/introducing-gemini-robotics-er-2/index.md
ingested: 2026-W30 (Sat-Sat)
created: 2026-08-01
updated: 2026-08-01
tags: [robotics, embodied-reasoning, gemini, multimodal, google-deepmind]
---

# Gemini Robotics ER 2

Google DeepMind (Hansen, Xu; 2026-07-30). Modello di "embodied reasoning" per robotica: funziona come cervello di alto livello che pianifica task multi-step e delega l'esecuzione motoria a VLA (Vision-Language-Action) di basso livello.

## Punti chiave

- **Temporal intelligence**: guarda flussi video continui invece di snapshot statici. Traccia il progresso in 5 livelli (0-100%), raggiunge 57.4% accuracy su progress classification. Precision moment-finding 91.3% con 0.96s mean absolute distance: identifica il frame esatto dove un evento critico avviene.
- **Multi-robot collaboration**: robot diversi (Apollo 2 umanoide, Franka F3 Duo bracci, Spot quadrupede) comunicano via shared semantic understanding per handoff e task completion che un singolo robot non potrebbe fare.
- **Tool orchestration fluida**: integra Gemini Live API (streaming bidirezionale low-latency). Dichiara interfacce VLA, navigation APIs, tools come funzioni. Il modello "pensa" al passo successivo mentre esegue quello corrente, senza pause stop-and-think.
- **Sicurezza embodied**: ferma l'umanoide quando una persona è vicina, riprende solo ad area libera. Introduce benchmark per VLA orchestrator safe (safety constraints enforcement, environment monitoring, physical feasibility assessment).

## Collocazione nel vault

Prima source su embodied/robotics reasoning. Tema del controllore cognitivo (pianificatore) separato dall'esecutore motorio (VLA) è affine all'architettura harness → tool, ma in dominio fisico. Per ora isolata, nessuna pagina concettuale forte nel vault.

🔗 [raw/web/introducing-gemini-robotics-er-2/](../../raw/web/introducing-gemini-robotics-er-2/index.md)
