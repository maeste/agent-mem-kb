---
type: source
created: 2026-06-28
updated: 2026-06-28
tags: [memory, agentic-memory, cognitive-science, retrieval-vs-learning]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Autori:** Binyan Xu, Xilin Dai, Kehan Zhang (CUHK, Zhejiang University)
**arXiv:** 2604.27707 (Apr 2026)

## Riassunto

Il paper argomenta che i sistemi di memoria agentici attuali (vector store, RAG, scratchpad, context-window management) implementano **lookup**, non **memoria**. Questa confusione di categoria ha conseguenze provabili:

- **Generalizzazione per similarita vs regole:** il recupero generalizza per somiglianza agli esempi memorizzati; la memoria basata sui pesi generalizza applicando regole astratte a input mai visti prima
- **Soffitto di generalizzazione compositiva:** nessun aumento della dimensione del contesto o qualita del recupero puo superare questo limite
- **Vulnerabilita al memory poisoning:** contenuto iniettato si propaga in tutte le sessioni future

Gli autori propongono una tassonomia della memoria con 4 tipi: Working (context window), Episodic (external store), Semantic (model weights), Experiential (model weights via fine-tuning/CL). I sistemi attuali occupano solo la riga "Episodic"; la riga "Experiential" e il gap da colmare.

## Claim chiave

- I sistemi agentici attuali accumulano note senza sviluppare expertise [[wiki/sources/arxiv-2604.27707.md]]
- La teoria dei Complementary Learning Systems dalla neuroscienza suggerisce di affiancare storage ippocampale rapido a consolidamento corticale lento [[wiki/sources/arxiv-2604.27707.md]]
- Il paper risponde a quattro visioni alternative sulla memoria agentica [[wiki/sources/arxiv-2604.27707.md]]

## Collegamenti

- Complementare a [[wiki/sources/xu-2026-contextual-agentic-memory.md]] (stesso primo autore, focus diverso)
- Rilevante per [[wiki/pages/]] (da creare: pagina su memory taxonomy)
