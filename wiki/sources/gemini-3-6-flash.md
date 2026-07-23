---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [google, gemini, llm-models, ai-agents, cybersecurity]
source_path: raw/web/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Gemini 3.6 Flash, 3.5 Flash-Lite, 3.5 Flash Cyber

Annuncio Google (21 lug 2026) di tre nuovi modelli della famiglia Flash, orientati ad agentic workflows.

## Modelli annunciati

### Gemini 3.6 Flash
- Modello "workhorse" successore di 3.5 Flash: migliori performance in coding, knowledge work, multimodalita [[raw/web/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber/index.md]]
- **17% meno output token** rispetto a 3.5 Flash (Artificial Analysis Index); fino al 65% in meno su DeepSWE
- Prezzo: $1.50/M input, $7.50/M output (inferiore a 3.5 Flash)
- Benchmark rilevanti: DeepSWE 49% vs 37%, MLE Bench 63.9% vs 49.7%, OSWorld-Verified 83.0% vs 78.4%, GDPval-AA v2 1421 vs 1349
- Computer use come built-in client-side tool via Gemini API
- Include enhanced Frontier Safety safeguards (CBRN, cyber offense)

### Gemini 3.5 Flash-Lite
- Piu veloce della serie 3.5: **350 output token/s**, prezzo $0.3/M input, $2.5/M output [[raw/web/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber/index.md]]
- Supera 3.1 Flash-Lite di margine ampio; in alcuni benchmark (SWE-Bench Pro, OSWorld-Verified) batte anche 3 Flash
- Ideale per high-throughput: agentic search, document processing
- Supporta thinking levels configurabili (minimal/low per latenza, alti per sub-agent workloads)

### Gemini 3.5 Flash Cyber (CodeMender)
- Modello specializzato per cybersecurity, basato su 3.5 Flash [[raw/web/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber/index.md]]
- Performance competitive su CyberGym in combinazione con CodeMender (multi-agent security pipeline)
- **Disponibilita limitata**: solo governi e partner trusted tramite pilot program
- Dual-use concern: rilascio controllato per mitigare misuse

## Note aggiuntive

- Gemini 3.5 Pro in testing con partner; **Gemini 4** gia in pre-training (ambizioso run)
- Disponibilita immediata per 3.6 Flash e 3.5 Flash-Lite su Gemini API, Android Studio, Antigravity, Gemini Enterprise Agent Platform, Gemini app
