---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [selective-forgetting, neuro-inspired-memory, memory-pruning, security]
source_path: raw/papers/arxiv-2604.20300.pdf
---

# FSFM: A Biologically-Inspired Framework for Selective Forgetting

**Yingjie Gu et al.** (China Mobile) — arXiv:2604.20300, Apr 2026

## Summary

FSFM è un framework neuro-ispirato per il **selective forgetting** negli agenti LLM, disegnando paralleli diretti con processi cognitivi umani: teoria dell'indicizzazione/consolidazione ippocampale e curva di dimenticanza di Ebbinghaus. Argomenta che in ambienti resource-constrained, un meccanismo di forgetting ben progettato è cruciale quanto la retention per:

1. **Efficienza computazionale e storage**: pruning intelligente della memoria
2. **Qualità del contenuto**: aggiornamento dinamico di preferenze obsolete
3. **Sicurezza**: active forgetting di input malevoli, dati sensibili, content privacy-compromising

Taxonomia dei meccanismi di forgetting: passive decay-based, active deletion-based, safety-triggered, adaptive reinforcement-based. Risultati: +8.49% efficienza accesso, +29.2% signal-to-noise ratio, 100% eliminazione rischi sicurezza.

## Key claims
- Il forgetting selettivo è fondamentale quanto la retention per agenti production-grade ([§Abstract](raw/papers/arxiv-2604.20300.pdf))
- L'ispirazione biologica (ippocampo, Ebbinghaus) offre principi applicabili ([§1](raw/papers/arxiv-2604.20300.pdf))
- Quattro categorie di forgetting coprono casi d'uso distinti ([§3](raw/papers/arxiv-2604.20300.pdf))

## Connections
- [[wiki/sources/gu-2026-fsfm]] — fonte primaria
- [[wiki/pages/selective-forgetting]] — meccanismi di dimenticanza selettiva
