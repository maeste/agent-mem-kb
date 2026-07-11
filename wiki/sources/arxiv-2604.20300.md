---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [forgetting, memory-management, neuro-inspired, hippocampal-theory, ebbinghaus, security, privacy]
source_path: raw/papers/arxiv-2604.20300.pdf
---

# FSFM: Biologically-Inspired Selective Forgetting for Agent Memory

**Gu, Xiong, Wang, Ren, Li, Zhang, Guo, Sun, Ma, Shi** (China Mobile) — arXiv:2604.20300, Apr 2026

## Summary

FSFM è un framework neuro-ispirato per **selective forgetting** in agent LLM, argumento che in ambienti resource-constrained un meccanismo di oblio ben progettato è cruciale quanto la retention per efficienza, qualità e sicurezza.

## Claim principali

- **Tesi centrale**: forgetting non è un bug ma una feature, sia in cognizione umana che in sistemi AI [[raw/papers/arxiv-2604.20300.pdf]].
- **Cinque problemi della retention illimitata**: (1) resource constraints (storage e computational overhead crescenti); (2) decline di qualità (rumore da contenuti ridondanti); (3) information obsolescence (preferenze e fatti diventano outdated); (4) security vulnerabilities (superficie d'attacco da memorie sensitive); (5) privacy concerns (conflitto con GDPR "right to be forgotten") [[raw/papers/arxiv-2604.20300.pdf]].
- **Taxonomy di meccanismi di forgetting**: (1) passive decay-based; (2) active deletion-based; (3) safety-triggered; (4) adaptive reinforcement-based [[raw/papers/arxiv-2604.20300.pdf]].
- **Grounding biologico**: hippocampal memory indexing/consolidation theory + curva di dimenticanza di Ebbinghaus [[raw/papers/arxiv-2604.20300.pdf]].
- **Risultati**: miglioramenti significativi in access efficiency (+8.49%), content quality (+29.2% signal-to-noise ratio), security performance (100% eliminazione rischi sicurezza) [[raw/papers/arxiv-2604.20300.pdf]].
- **Tre dimensioni del valore**: (1) computational/storage efficiency via intelligent pruning; (2) enhanced quality via dynamic update di informazioni outdated; (3) robust security via active forgetting di malicious inputs, dati sensitive, content privacy-compromising [[raw/papers/arxiv-2604.20300.pdf]].

## Posizione nel dibattito

Uno dei pochi lavori a trattare il forgetting come prima classe citizenship nella ricerca su agentic memory. Complementa i lavori su memory governance (Simsek) e memory worth. Le implicazioni per privacy e security sono particolarmente rilevanti per deployment production.
