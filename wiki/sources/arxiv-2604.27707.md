---
type: source
created: 2026-05-24
updated: 2026-05-24
tags: [memory, critique, theory, agents]
source_path: raw/papers/arxiv-2604.27707.pdf
---

# Contextual Agentic Memory is a Memo, Not True Memory

Xu, Dai, Zhang (CUHK, Zhejiang University), April 2026.

Questo paper avanza una tesi critica forte: i sistemi di memoria agente attuali (vector store, RAG, scratchpad, context-window management) implementano lookup, non memoria vera. L'autore distingue due percorsi strutturalmente distinti: cambiare θ (pesi del modello via fine-tuning/RL) vs cambiare C (contesto via prompting/RAG/MCP). La compressione θ-based è generativa (il modello ricombina regole per input mai visti); la C-based è retrieval-based (solo ciò che è esplicitamente nel contesto). Citando la teoria dei Complementary Learning Systems dalle neuroscienze, il paper argomenta che l'intelligenza biologica risolve il problema accoppiando storage ippocampale rapido (esemplari) con consolidamento neocorticale lento (pesi), mentre gli agenti AI attuali implementano solo la prima metà. Quattro claim principali: (1) Definizonale: la memoria agente è exemplar-based lookup senza extrapolazione; (2) Strutturale: un "Generalization Gap theorem" dimostra che la memoria retrieval-based ha un soffitto inferiore alla memoria weight-based; (3) Dinamica: agenti solo C-engineering non sviluppano expertise; (4) Sicurezza: la memoria agente converte transient prompt injection in persistent compromise. Il paper propone un'architettura di co-esistenza e una call to action per system builder e benchmark designer.
