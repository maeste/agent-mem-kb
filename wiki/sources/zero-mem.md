---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [memory, zero-token, agent-architecture, retrieval, paper]
source_path: raw/papers/arxiv-2607.29377.pdf
ingested: 2026-W31 (Sat-Sat)
---

# Zero-Mem: Zero-Token Memory Operations for LLM Agents

Xiao et al. (HK PolyU + SWUFE + Jilin, Jul 2026). Propone operazioni di memoria a costo zero per agenti LLM: nessun step al di fuori del final QA invoca un LLM o consuma token.

## Idee chiave

- Preserva le interazioni originali come source of record (no LLM call per generare record intermedi)
- Due viste complementari: **entity-context graph** (connessioni cross-interazione) + **temporal hierarchy** (località conversazionale e session state)
- Per ogni query pesa le due viste, recupera da entrambe, segue la struttura per ricostruire relazioni di supporto
- **Deterministic calibration**: prima scarta evidence conflittuale, poi tiene la risposta del reader ancorata alle tracce
- Solo il final-QA reader invoca un LLM; l'encoder è computato separatamente

## Risultati

Competitivo su benchmark long-memory e long-context QA eliminando le chiamate LLM e il consumo di token dalle operazioni di memoria. Riduce i tempi operativi.

## Connessioni

Risponde alla stessa domanda di [[wiki/pages/memory-skills-co-evolution]] ma con strategia opposta a PRO-LONG: invece di persistere tutto e recuperare via codice, elimina del tutto le chiamate LLM dalla memoria spostando il costo su strutture deterministiche (grafo + gerarchia temporale). Mentre MSCE cristallizza e PRO-LONG codifica, Zero-Mem struttura senza generazione.
