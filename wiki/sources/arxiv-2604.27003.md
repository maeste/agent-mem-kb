---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [continual-learning, memory-representation, transfer-learning, negative-transfer, alfworld, babyai]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Hu, Long, Wang** (NTU Singapore) — arXiv:2604.27003, Apr 2026

## Summary

Questo paper studia il comportamento della memoria esterna in agent LLM sotto la lente del **continual learning**, mostrando che la memoria non risolve il problema stability-plasticity ma lo **sposta** dallo spazio dei parametri allo spazio di accesso alla memoria.

## Claim principali

- **Relocation thesis**: in CL parametrico, il problema è interferenza nei pesi. In agent con memoria esterna, l'esperienza passata può essere preservata senza sovrascrivere parametri, ma è utile solo se efficacemente recuperata e inserita nella context window limitata. Il bottleneck CL si sposta da *come aggiornare i pesi* a *come experience viene recuperata, riutilizzata e prioritizzata* [[raw/papers/arxiv-2604.27003.pdf]].
- **Framework (k, v)**: disentangle due assi di design fondamentali: **k** = come l'esperienza è rappresentata (da raw episodic trajectories a abstract procedural insights); **v** = come è organizzata per retrieval (granularità e frequenza) [[raw/papers/arxiv-2604.27003.pdf]].
- **Risultati su ALFWorld e BabyAI**: memorie procedurali astratte transferiscono più affidabilmente di detailed trajectories; negative transfer colpisce sproporzionatamente i casi difficili [[raw/papers/arxiv-2604.27003.pdf]].
- **Organizzazione fine-grained non è universalmente benefica**: design che producono strong forward transfer possono simultaneamente indurre severe forgetting. Non esiste free lunch nella organizzazione della memoria [[raw/papers/arxiv-2604.27003.pdf]].
- **Tre meccanismi di fallimento**: (1) retrieval pollution (memorie irrilevanti richiamate), (2) context competition (esperienze utili displace da altri item sotto finestra finita), (3) memory dilution (con la crescita del store, esperienza rilevante diventa harder da identificare) [[raw/papers/arxiv-2604.27003.pdf]].

## Posizione nel dibattito

Primo studio sistematico del continual learning in agent con memoria esterna. Ricollega la letteratura sulla memoria agentic ai classici problemi del CL. Le implicazioni sono importanti per chi progetta sistemi a long-term: la scelta di rappresentazione e organizzazione della memoria ha trade-off strutturali non banali.
