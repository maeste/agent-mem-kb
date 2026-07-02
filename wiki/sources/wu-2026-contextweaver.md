---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [context-management, dependency-graph, memory-structure, swe-bench, tool-use-agents]
source_path: raw/papers/arxiv-2604.23069.pdf
---

# ContextWeaver: Dependency-Structured Memory for LLM Agents

**Autori:** Yating Wu (UT Austin), Yuhao Zhang, Sayan Ghosh, Sourya Basu, Anoop Deoras, Jun Huan, Gaurav Gupta (AWS AI Labs)  
**Data:** Aprile 2026 | arXiv:2604.23069

## Sintesi

ContextWeaver affronta il problema della gestione del contesto in agent a lungo termine attraverso una **struttura a grafo di dipendenze** tra i passaggi di ragionamento.

### Il problema

Gli approcci esistenti (sliding window, prompt compression, retrieval-based) selezionano contenuto basandosi su recency, salience o similarita' semantica. Questi segnali **non catturano la struttura di dipendenza** che collega un passo di ragionamento al successivo. Quando queste dipendenze vengono perse:
- L'agente interrompe piani in corso
- Ripete esplorazioni gia' fatte
- Produce passaggi che non matchano piu' il contesto precedente

### Architettura tre componenti

1. **Dependency-based construction:** costruisce un grafo dove ogni nodo e' un passo di ragionamento collegato ai passaggi precedenti da cui dipende (causali da tool output, logici da reasoning steps)
2. **Compact dependency summarization:** condensa i percorsi root-to-step in unita' riutilizzabili
3. **Lightweight validation layer:** incorpora feedback di esecuzione

### Risultati su SWE-Bench

- Miglioramenti su sliding-window baseline in pass@1 sia su Verified che su Lite
- Riduzione dei reasoning steps e del token usage
- La modellazione delle dipendenze logiche fornisce un meccanismo di memoria stabile e scalabile

## Claim chiave

- Nei setting agentici, ogni azione successiva dipende da decisioni precedenti, output di tool, ipotesi intermedie [[wiki/sources/wu-2026-contextweaver.md]]
- Perdere le dipendenze logiche e' piu' dannoso che perdere contenuto generico
- Il grafo di dipendenze serializza pattern dinamici long-range che lo sliding window perde sistematicamente

## Posizione nel vault

Contributo pratico alla memory structure. Si colloca nella famiglia "hierarchical virtual context" del taxonomy Du et al., con innovazione specifica sulle dipendenze causali.
