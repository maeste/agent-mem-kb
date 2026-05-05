---
type: page
created: 2026-05-04
updated: 2026-05-05
tags: [llm-agents, memory, forgetting, memory-governance, security, agent-skills, registry]
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

## Governance dei registry di skill

Quando la memoria procedurale viene esternalizzata come catalogo condiviso di skill, il problema di governance si sposta dalla singola sessione al perimetro del registry.

- Il SoK documenta la campagna ClawHavoc, con quasi 1.200 skill malevoli infiltrati in un grande marketplace agentico per esfiltrare API key e wallet crypto: la sola disponibilità non è una garanzia, serve verifica e attribuzione [[wiki/sources/arxiv-2602.20867]]
- Skilldex propone scoring di conformità in stile compilatore (0–100 con diagnostica linea per linea) sulla spec SKILL.md, una skillset abstraction che bundla skill correlate con asset condivisi, scope gerarchico (global / shared / project) e tier di trust nel registry community, riportando il modello mentale dei package manager (npm, pip) sulle skill [[wiki/sources/arxiv-2604.16911]]
- La rappresentazione SSL migliora il risk assessment automatico delle skill (macro F1 da 0.409 a 0.509) rendendo esplicite le azioni atomiche e gli effetti collaterali (READ, CALL, file, network) — le skill diventano ispezionabili invece che opache prose [[wiki/sources/arxiv-2604.24026]]
- Talents in OneManCompany aggiungono un layer organizzativo sopra le skill, con typed organisational interfaces, recruitment on-demand da un Talent Market, e un E²R tree search che lega esecuzione e review — governance non più solo del singolo skill ma della *forza lavoro* di agenti [[wiki/sources/arxiv-2604.22446]]
- Il discovery decentralizzato richiede un proprio modello di governance: agenti hanno doppio churn (host-level e demand-level con stati warm/cold), e overlay structured (Kademlia DHT) vs gossip (Cyclon+Vicinity) coprono regimi diversi — non c'è una scelta universalmente migliore [[wiki/sources/arxiv-2604.23080]]
