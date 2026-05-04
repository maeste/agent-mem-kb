---
type: page
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, forgetting, memory-governance, security]
---

# Dimenticanza e Governanza della Memoria

La capacità di dimenticare è tanto fondamentale quanto quella di ricordare per gli agenti LLM. Senza meccanismi di obsolescenza, la memoria si degrada in rumore e diventa un vettore di sicurezza.

## Memory Worth

Simsek (2026) propone Memory Worth (MW), un segnale per-memoria a due contatori che traccia quante volte una memoria co-occorre con outcome positivi vs. negativi. Converge quasi certamente alla probabilità condizionale di successo dato il retrieval della memoria, sotto ipotesi di stazionarietà. Abilita staleness detection, retrieval suppression e deprecation [[wiki/sources/simsek-2026-when-to-forget]].

## FSFM — Selective Forgetting

Gu et al. (2026) propongono una tassonomia neuro-ispirata: decadimento passivo (curva di Ebbinghaus), cancellazione attiva, triggerata dalla sicurezza, e adattiva basata su RL. Risultati: +8.49% efficienza di accesso, +29.2% signal-to-noise, 100% eliminazione rischi di sicurezza [[wiki/sources/gu-2026-fsfm]].

## Vulnerabilità della memoria esterna

Xu et al. (2026) evidenziano che la memoria esterno converte temporanee prompt injection in compromissione persistente: contenuto iniettato si propaga attraverso tutte le sessioni future [[wiki/sources/xu-2026-contextual-agentic-memory]].

RSCB-MC dimostra che nel contesto del debugging, il false-positive retrieval può ancorare l'agente su una strategia di repair errata, consumando budget di contesto e amplificando fix allucinati. Il sistema penalizza più fortemente i falsi positivi rispetto ai mancati riutilizzi [[wiki/sources/iscan-2026-rscb-mc]].
