---
type: source
source_path: raw/papers/arxiv-2607.20064.pdf
ingested: 2026-W30 (Sat-Sat)
created: 2026-08-01
updated: 2026-08-01
tags: [memory, long-horizon-reasoning, context-management, arc-agi-3, programmatic-memory, coding-agents]
---

# PRO-LONG: programmatic memory per long-horizon reasoning

Fox, Wang, Rosu, Dhingra (Duke University; arXiv 2607.20064v2, 2026-07-23). Framework minimal di context management basato su programmatic memory: append-all log come write, code-based search come read. SOTA su ARC-AGI-3.

## Punti chiave

- **Fidelity-tractability tradeoff**: ogni sistema di memoria agent deve bilanciare quanta informazione persistere vs quanto è difficile recuperarla. Più si salva, più il recupero diventa intrattabile. PRO-LONG spezza il tradeoff salvando tutto (fidelity massima) ma recuperando via codice (tractability via grep/regex).
- **Programmatic memory**: write = append di ogni osservazione/azione/outcome al log, nessuna decisione su cosa tenere. Read = search programmatico sul log, nativo per coding agent. Log ground-truth, lossless, 100k+ linee gestibili.
- **Risultati ARC-AGI-3**: +18.0 punti percentuali medi vs base coding agent. Con Fable 5 raggiunge 97.4% best@2 a $1,750. Con Opus 4.6 42.4% pass@1 (miglior risultato pubblico per quel modello). 4.2-5.8x meno token degli harness specializzati concorrenti.
- **Abilitato dai coding agent**: il design è reso possibile dalle capability dei coding agent (Codex, Claude Code). Persistent workspaces e tool per note aggiungono poco; il full log access è il driver.
- **Context rot**: contesti grandi (anche entro window da ~1M token) degradano quando le traiettorie crescono. La distinzione chiave è accessed context (window attiva) vs accessible context (memoria tool-reachable, può essere 10M+ token).

## Collocazione nel vault

Direttamente rilevante per [[wiki/pages/memory-skills-co-evolution]]: programmatic memory è una nuova forma oltre L1/L2/L3, resa possibile dalla maturazione dei coding agent. Conferma la centralità dell'harness (cfr [[wiki/sources/openai-arc-agi-3-harness]]): stessi modelli, stesso benchmark, PRO-LONG +18pt solo cambiando context management. Collega a [[wiki/pages/compositional-generalization]]: long-horizon reasoning richiede generalizzazione attraverso livelli crescenti di difficoltà.

🔗 [raw/papers/arxiv-2607.20064.pdf](../../raw/papers/arxiv-2607.20064.pdf)
