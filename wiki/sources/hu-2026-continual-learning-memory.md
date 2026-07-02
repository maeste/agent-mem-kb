---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [continual-learning, memory-agents, experience-reuse, transfer-learning, alfworld, babyai]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Autori:** Qisheng Hu, Quanyu Long, Wenya Wang (Nanyang Technological University)  
**Data:** Aprile 2026 | arXiv:2604.27003

## Sintesi

Questo paper studia il problema del **continual learning nei memory-augmented LLM agent** attraverso una lente controllata. La tesi centrale: la memoria esterna **non elimina** il dilemma stabilita'-plasticita' del continual learning parametrico, ma lo **sposta** a livello di accesso alla memoria.

### Il framework (k, v)

Gli autori introducono un framework che disaccoppia due assi di design fondamentali:
- **k (knowledge representation):** come l'esperienza e' rappresentata (da raw episodic trajectories ad abstract procedural memories)
- **v (memory organization):** come e' organizzata per retrieval (granularita', frequenza)

### Risultati sperimentali su ALFWorld e BabyAI

1. **Abstract procedural memories transferiscono piu' affidabilmente** di detailed trajectories: le memorie procedurali astratte generalizzano meglio across task
2. **Negative transfer colpisce sproporzionatamente i casi difficili:** quando il transfer fallisce, i task gia' hard peggiorano di piu'
3. **Fine-grained memory organization non e' universalmente benefica:** design che producono forte forward transfer possono simultaneamente indurre severo forgetting. Questo e' un risultato controintuitivo importante

### Meccanismi di failure identificati

- **Retrieval pollution:** memorie irrilevanti richiamate nel contesto
- **Context competition:** esperienze utili spostate da altri item recuperati sotto finestra di contesto finita
- **Memory dilution:** con la crescita dello store, l'esperienza rilevante diventa piu' difficile da identificare

## Claim chiave

- La memoria esterna reshapes il problema del continual learning invece di risolverlo [[wiki/sources/du-2026-memory-survey.md]]
- Il trade-off tra forward transfer e forgetting e' intrinseco all'organizzazione della memoria, non un artefatto sperimentale
- Le memorie procedurali astratte sono superiori alle trajectory raw per il transfer cross-task [[wiki/sources/arxiv-2604.27707.md]]

## Posizione nel vault

Paper empirico fondamentale che collega continual learning e memoria agentica. Da affiancare ai lavori su memory consolidation e ai survey sul tema.
