---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, forgetting, neuro-inspired, agents, security]
source_path: raw/papers/arxiv-2604.20300.pdf
---

# FSFM: A Biologically-Inspired Framework for Selective Forgetting

**Gu et al. (2026)** — China Mobile / Jiutai

## Summary

FSFM è un framework **neuro-ispirato per selective forgetting** negli agenti LLM. L'argomento centrale: in ambienti resource-constrained, un meccanismo di forgetting ben progettato è cruciale quanto la retention per performance ottimale su tre dimensioni:

1. **Efficienza computazionale e di storage** tramite memory pruning intelligente
2. **Qualità del contenuto** aggiornando dinamicamente preferenze obsolete e informazioni contestuali
3. **Sicurezza** tramite active forgetting di input malevoli, dati sensibili, contenuto privacy-compromettente

Il framework trae ispirazione dalla teoria dell'indicizzazione/consolidamento ippocampale e dalla curva di dimenticanza di Ebbinghaus.

## Tassonomia dei meccanismi di forgetting

- Passive decay-based
- Active deletion-based
- Safety-triggered
- Adaptive reinforcement-based

## Risultati

- Access efficiency: **+8.49%**
- Content quality: **+29.2%** signal-to-noise ratio
- Security: **100%** eliminazione rischi sicurezza

## Claim chiave

- Il selective forgetting è una capability fondamentale per agenti LLM next-gen in scenari real-world resource-constrained [[wiki/sources/arxiv-2604.20300]]
- I paradigmi attuali trattano la memoria come sempre crescente; questo è subottimale [[wiki/sources/arxiv-2604.20300]]
