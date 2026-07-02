---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [memory-survey, agent-memory, taxonomy, evaluation-benchmarks, memory-mechanisms]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Autore:** Pengfei Du (Hong Kong Research Institute of Technology)  
**Data:** Marzo 2026 | arXiv:2603.07670

## Sintesi

Survey completo sulla memoria negli agent LLM che copre il periodo 2022-inizio 2026. Formalizza la memoria agentica come ciclo **write-manage-read** strettamente accoppiato con percezione e azione.

### Taxonomy tridimensionale

1. **Temporal scope:** working / short-term / long-term
2. **Representational substrate:** context window / external store / model weights
3. **Control policy:** come decidere cosa scrivere, mantenere, recuperare

### Cinque famiglie di meccanismi

1. **Context-resident compression:** compressione dentro il contesto (sliding window, summarization)
2. **Retrieval-augmented stores:** RAG, vector store, memory stream (Generative Agents)
3. **Reflective self-improvement:** Reflexion-style self-critique storage
4. **Hierarchical virtual context:** organizzazione a livelli della memoria (MemGPT paging)
5. **Policy-learned management:** apprendimento delle decisioni di memoria via RL

### Valutazione

Traccia lo shift da benchmark di recall statici a test agentic multi-sessione che interlacciano memoria con decision-making. Analizza quattro benchmark recenti che espongono gap persistenti.

### Applicazioni dove la memoria e' il differenziatore

- Personal assistants
- Coding agents
- Open-world games
- Scientific reasoning
- Multi-agent teamwork

### Engineering realities

- Write-path filtering
- Contradiction handling
- Latency budgets
- Privacy governance

### Open challenges identificati

1. Continual consolidation
2. Causally grounded retrieval
3. Trustworthy reflection
4. Learned forgetting
5. Multimodal embodied memory

## Claim chiave

- La memoria trasforma un LLM stateless in un agente self-evolving [[wiki/sources/du-2026-memory-survey.md]]
- Il taxonomy tridimensionale fornisce uno spazio di design unificato per confrontare sistemi diversi
- I benchmark attuali espongono gap significativi specialmente su task composizionali e long-horizon

## Posizione nel vault

Survey di riferimento sul tema memoria agentica. Struttura l'intero campo e fornisce il taxonomy usato per organizzare le altre sorgenti.
