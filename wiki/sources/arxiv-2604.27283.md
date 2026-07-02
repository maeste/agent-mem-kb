---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [coding-agents, memory-retrieval, contextual-bandits, risk-sensitive, abstention, debugging]
source_path: raw/papers/arxiv-2604.27283.pdf
---

# RSCB-MC: Risk-Sensitive Contextual Bandits for Memory Retrieval in Coding Agents

**Autore:** Mehmet Iscan (PythaLab, Yildiz Technical University)  
**Data:** Aprile 2026 | arXiv:2604.27283

## Sintesi

RSCB-MC affronta un problema pratico critico nei coding agent con memoria esterna: **quando la memoria recuperata e' dannosa piu' che utile**. L'autore parte da osservazioni operative concrete in cui un agente di debug riconosce un errore "famigliare", recupera una fix precedente, e la applica con fiducia peggiorando la situazione.

### Il problema dei falsi positivi

Diversi root cause possono produrre stack trace quasi identici:
- Database lock vs migration stale: stesso messaggio, fix diverso
- Wrong venv vs wrong PYTHONPATH: stesso ModuleNotFoundError, rimedio diverso
- Invalid config key vs path resolution failure: stesso KeyError

La retrieval per similarita' di superficie non solo e' inutile; **ancora l'agente su un branch di repair errato** consumando budget di contesto.

### Architettura RSCB-MC

Il sistema tratta l'uso della memoria issue come problema di **controllo risk-sensitive**, non come puro top-k retrieval:

1. **Pattern-Variant-Episode schema:** organizza la conoscenza issue riutilizzabile
2. **16-feature contextual state:** converte evidenza di retrieval in stato fisso che cattura relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, token cost
3. **Reward design:** penalizza i false-positive memory injection piu' fortemente del bonus per injection corretta. Non-injection e abstention sono azioni di safety first-class
4. **Azioni possibili:** no memory, inject top resolution, summarize multiple candidates, high-precision/high-recall retrieval, **abstain**, ask for feedback

### Risultati

- Offline replay success rate: **62.5%** (miglior non-oracle)
- False-positive rate: **0.0%**
- Hot-path validation (200 casi): **60.5%** proxy success, 0.0% false positives
- Decision latency p95: **331.466 µs**

## Claim chiave

- Per la memoria dei coding agent, la domanda principale non e' "quale memoria e' piu' simile" ma "**quale memoria e' abbastanza sicura da influenzare la trajectory di debug**"
- La reward function deve trattare il false-positive injection come evento di safety first-class, non come costo marginale
- Abstention (non usare memoria) dovrebbe essere un'azione citadina, non un fallback [[wiki/sources/simsek-2026-when-to-forget.md]]

## Posizione nel vault

Contributo operativo alla letteratura su memory safety negli agent. Complementa i lavori teorici su memory governance (Simsek 2026) con validazione empirica in setting di coding.
