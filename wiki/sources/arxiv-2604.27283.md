---
type: source
created: 2026-05-24
updated: 2026-05-24
tags: [memory, retrieval, coding-agents, bandits, safety]
source_path: raw/papers/arxiv-2604.27283.md
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

Iscan (PythaLab, Yildiz Technical University), April 2026.

Questo paper affronta un problema operativo concreto nei coding agent LLM: quando la memoria esterna (fix precedenti, trace di debug) dovrebbe essere usata e quando no. L'autore osserva che similarità superficiale tra errori inganna spesso l'agent: stack trace simili, errori terminali o sintomi di configurazione identici possono avere cause radicalmente diverse. Il paper reframe il problema dell'uso della memoria issue come problema di controllo risk-sensitive (non puro top-k retrieval). RSCB-MC è un memory controller basato su contextual bandit che decide tra: nessuna memoria, inject top resolution, riassumere candidati multipli, high-precision/high-recall retrieval, abstention, o richiesta di feedback. Lo schema di storage è pattern-variant-episode; lo stato contestuale ha 16 feature fisse (rilevanza, incertezza, compatibilità strutturale, history feedback, false-positive risk, latenza, token cost). La reward penalizza false-positive injection più forte del missed reuse. Risultati: 62.5% offline replay success rate con 0.0% false-positive rate; 60.5% proxy success in validazione hot-path 200-casi con 331µs p95 latenza. Il contributo chiave è concettuale: per la memoria dei coding agent, la domanda principale non è "quale memoria è più simile" ma "qualsiasi memoria recuperata è abbastanza sicura da influenzare la traiettoria di debug".
