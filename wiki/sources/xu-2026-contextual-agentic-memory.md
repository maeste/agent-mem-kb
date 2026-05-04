---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, critique, generalization, security, neuroscience]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

**Autori:** Binyan Xu, Xilin Dai, Kehuan Zhang (CUHK, Zhejiang University)
**Data:** 2026-04-30

## Summary

Argomenta che i sistemi di memoria correnti (vector store, RAG, scratchpad, context-window management) implementano *lookup* per similarità, non vera memoria. La confusione produce tre conseguenze: (1) agenti che accumulano note senza sviluppare competenza, (2) un limite di generalizzazione compositiva provabile che nessun aumento di contesto o qualità di retrieval può superare, (3) vulnerabilità strutturale a memory poisoning persistente.

Pesandosi sulla teoria Complementary Learning Systems delle neuroscienze (ippocampo = storage esemplare veloce, neocorteccia = consolidamento pesi lento), mostra che gli agenti AI implementano solo la prima metà. Propone co-esistenza di retrieval e weight consolidation come strada avanti.

[[wiki/pages/llm-agent-memory]] [[wiki/pages/forgetting-memory-governance]]
