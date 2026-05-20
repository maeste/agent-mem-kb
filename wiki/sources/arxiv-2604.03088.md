---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, VM, compilation, portability, cross-model]
source_path: raw/papers/arxiv-2604.03088.pdf
---

# SkVM: Language VM for Skills across Heterogeneous LLMs and Harnesses

**Autori:** Le Chen, Erhu Feng, Yubin Xia, Haibo Chen (Shanghai Jiao Tong University)
**arXiv:** 2604.03088 (apr 2026)

## Summary

SkVM tratta **skills come codice e LLM come processor eterogenei**, ispirandosi al compiler design tradizionale. Il problema: skill condivise across piattaforme sono trattate come raw context, causando comportamento inconsistente tra agenti diversi.

## Architettura

Analizza 118.000 skills per decomporre i requisiti in **primitive capabilities**, misura quanto bene ogni pair model-harness le supporta.

- **Compile time**: capability-based compilation, environment binding, concurrency extraction
- **Runtime**: JIT code solidification, adaptive recompilation

## Risultati

- Migliora task completion rates across 8 LLM + 3 harness
- Token consumption ridotto fino al **40%**
- Fino a **3.2× speedup** con enhanced parallelism
- **19–50× latency reduction** via code solidification

## Relazione con altri lavori

- Complementare a [[wiki/sources/arxiv-2604.24026]] (SSL): SkVM gestisce *compilazione/execution* portabile delle skill, SSL gestisce *rappresentazione*
- Si collega a [[wiki/sources/arxiv-2604.16911]] (Skilldex): Skilldex distribuisce, SkVM compila/esegue
- Approccio unico nel vault: compiler theory applicato a agent skills
