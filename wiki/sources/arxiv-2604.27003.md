---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, continual-learning, agents, transfer-learning]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory

**Hu, Long & Wang (2026)** — Nanyang Technological University

## Summary

Questo paper studia come il **continual learning (CL)** si manifesti negli agenti con memoria esterna. L'ipotesi comune è che la memoria esterna risolva il dilemma stabilità-plasticità del CL parametrico; gli autori dimostrano che il problema **non scompare ma si sposta al livello della memoria**.

Sotto una finestra di contesto limitata, esperienze vecchie e nuove competono durante il retrieval: il bottleneck del CL si sposta dagli aggiornamenti dei parametri all'accesso alla memoria.

## Framework (k, v)

Gli autori introducono un framework che disaccoppia due assi di design:
- **k** (representation): come l'esperienza viene rappresentata
- **v** (organization): come è organizzata per il retrieval

## Risultati su ALFWorld e BabyAI

- Le memorie procedurali astratte trasferiscono più affidabilmente delle traiettorie dettagliate
- Il **negative transfer** danneggia sproporzionatamente i casi difficili
- L'organizzazione a grana fine non è universalmente benefica: design che producono forte forward transfer possono simultaneamente indurre severo forgetting

## Claim chiave

- La memoria esterna non risolve il problema del continual learning, lo **rimodella** in un problema di rappresentazione e design del retrieval [[wiki/sources/arxiv-2604.27003]]
