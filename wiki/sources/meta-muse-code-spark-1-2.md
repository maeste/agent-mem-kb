---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [harness, co-training, coding-agent, meta, model-release, muse-spark]
source_path: raw/web/introducing-muse-code-and-muse-spark-1-2/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Introducing Muse Code and Muse Spark 1.2

Meta Superintelligence Labs (Aug 2026). Muse Code è un terminal coding agent powered by Muse Spark 1.2 (modello coding-focused).

## Muse Code (harness)

- **Async background agents**: sub-agent persistenti attivi per l'intera sessione, non spawnati per singolo task. Riducono latenza e steering su task multi-step difficili
- **Local event log**: ogni model call, tool run, approval, edit è appended. Single source of truth, replay-exact, restart-safe
- **Skill bundled**: `/plan` (approval-gated plan), `/grill` (stress-test del piano), `/goal` (lavora verso il completamento)

## Muse Spark 1.2 (modello)

- Coding-focused update di Spark 1.1: scaling compute su coding task, espansione diversity dell'ambiente di training
- **Co-training con Muse Code**: rejection sampled harness trajectories + recipe optimization per goals, compaction, subagents + integrazione del Muse Code toolset
- **Long-horizon**: addestrato su whole-repo generation, progetti end-to-end, auto-research. Usa planning + goal conditioning + context compaction
- **Self-improvement loop**: Spark 1.1 genera ambienti e template, poi valuta i candidati producendo dataset scalabile per Spark 1.2

## Case study: kernel optimization

Iterative GPU kernel optimization su 1000+ tool call (fino a 24h). Benchmark KDA e MLA per Hopper. Spark 1.2 combina chunk-parallel + sequential inter-chunk scan con fusion/tiling e ottimizzazioni KDA-specifiche.

## Annuncio (X thread @finkd)

Zuckerberg annuncia Muse Code in beta [[raw/web/unknown-2085080750034940201/index]]: 14k likes.

## Connessioni

La co-training harness-model è la realizzazione industriale del principio che [[wiki/pages/harness-design|l'harness è la variabile misurata]]: non si valuta il modello isolato, si valuta il pacchetto modello+harness. Il self-improvement loop (modello genera training environment → valuta → addestra successore) è lo stesso pattern di [[wiki/sources/prime-agent|Prime Agent]] ma applicato al training pre-deployment anziché runtime.
