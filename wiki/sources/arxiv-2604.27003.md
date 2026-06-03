---
type: source
created: 2026-06-03
updated: 2026-06-03
tags: [memory, continual-learning, experience-reuse, alfworld, babyai]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory

**Hu, Long & Wang** (NTU Singapore), arXiv:2604.27003, Apr 2026.

## Summary

Il paper studia come il problema del continual learning si ripresenti nei memory-augmented LLM agent. Invece di risolverlo, la memoria esterna lo **trasloca**: dallo spazio dei parametri allo spazio del retrieval sotto una finestra di contesto limitata.

### Claim principali

- La memoria esterna non elimina il dilemma stabilità-plasticità del continual learning parametrico; lo **rilocalizza a livello di accesso alla memoria** [[wiki/sources/arxiv-2604.27003]].
- Introdotto un framework **(k, v)** che disaccoppia due assi di design: come l'esperienza è rappresentata (k) e come è organizzata per il retrieval (v) [[wiki/sources/arxiv-2604.27003]].
- Su esperimenti sequenziali in ALFWorld e BabyAI: le memorie procedurali astratte trasferiscono più affidabilmente delle traiettorie dettagliate [[wiki/sources/arxiv-2604.27003]].
- Il **negative transfer** colpisce sproporzionatamente i casi difficili [[wiki/sources/arxiv-2604.27003]].
- Organizzazione più fine-grained della memoria non è universalmente benefica: design con forte forward transfer possono simultaneamente indurre severo forgetting [[wiki/sources/arxiv-2604.27003]].
- Vecchia e nuova esperienza competono durante il retrieval sotto context window limitato — questo è il nuovo bottleneck del continual learning [[wiki/sources/arxiv-2604.27003]].

### Rilevanza per la vault

Risultato chiave per [[wiki/pages/experience-reuse-continual-learning]]. Mostra che la memoria esterna non è un free pass per il continual learning, ma un problema riformulato. Complementa [[wiki/sources/hu-2026-continual-learning-memory]] (stesso primo autore, focus diverso).
