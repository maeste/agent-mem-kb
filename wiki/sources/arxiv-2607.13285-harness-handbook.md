---
type: source
source_path: raw/papers/arxiv-2607.13285.pdf
ingested: 2026-W30 (Sat-Sat)
created: 2026-08-01
updated: 2026-08-01
tags: [harness-design, behavior-localization, progressive-disclosure, code-agents, harness-evolution]
---

# Harness Handbook: behavior localization per harness evolution

Wang, Shi, Li et al. (Tencent + Indiana/UMD/UGA/NUS; arXiv 2607.13285, 2026-07-14). Definisce la behavior localization come bottleneck dell'harness evolution e introduce una rappresentazione behavior-centric + BGPD per risolverlo.

## Punti chiave

- **Behavior localization come problema distinto**: modificare un harness richiede prima di trovare tutti i siti di codice che implementano il comportamento target. I repo sono organizzati per file/funzione/modulo, le richieste di modifica descrivono comportamenti. Il mapping comportamento → codice è il gap reale, non la generazione di edit.
- **Comportamenti distribuiti**: in harness di produzione un singolo comportamento dipende da siti non-adiacenti attraverso file, funzioni, stage di esecuzione, stati condivisi. Siti raramente eseguiti sfuggono all'esplorazione iterativa dei coding agent.
- **Harness Handbook**: rappresentazione operazionale che organizza la conoscenza di implementazione per comportamento (cosa fa l'harness) e linka ogni comportamento al codice. Costruita automaticamente via static program analysis + LLM-assisted behavioral structuring.
- **Behavior-Guided Progressive Disclosure (BGPD)**: workflow che guida il coding agent da descrizioni comportamentali di alto livello ai dettagli implementativi, in stadi, verificando le candidate locations contro il codice corrente.
- **Risultati**: su due harness open-source, Handbook-Assisted planning migliora behavior localization e qualità del piano di edit usando meno planner token. Guadagni massimi su cambiamenti con siti sparsi, code path rari, interazioni cross-modulo.

## Collocazione nel vault

Nucleo centrale per [[wiki/pages/harness-design]]: formalizza harness come first-class software abstraction e identifica l'evoluzione come challenge ricorrente. Collega a [[wiki/pages/comprehension-debt]] (behavior localization è la versione operativa della comprehension debt: il codice c'è ma il mapping cognitivo comportamento→codice manca). BGPD è istanza concreta di progressive disclosure (cfr [[wiki/sources/anthropic-claude-5-context-engineering]]).

🔗 [raw/papers/arxiv-2607.13285.pdf](../../raw/papers/arxiv-2607.13285.pdf)
