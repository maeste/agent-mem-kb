---
type: page
created: 2026-07-23
updated: 2026-08-01
tags: [memory, skills, long-horizon, agent-architecture, concept]
---

# Memory & Skills Co-Evolution

I sistemi di memoria per agenti long-horizon recuperano tipicamente tracce passate come contesto passivo. La proposta di MSCE è convertirle in capacità esecuibili: non ricordare cosa è successo, ma estrarre procedure riutilizzabili.

## Il problema

Tang et al. ([[wiki/sources/arxiv-2607-16621-msce-memory-skills]]) identificano due limiti: (1) la memoria viene ri-usata come contesto passivo, costringendo l'agente a ragionare di nuovo su informazioni già viste; (2) terminal feedback è sparse e delayed, rendendo lo step-level credit assignment incerto.

## Gerarchia a 3 livelli MSCE

- **L1 Trace Memory**: step-level evidence, grounded
- **L2 Policy Memory**: pattern procedurali ricorrenti, indotti da cross-episode traces
- **L3 Environmental Cognition**: conoscenza dichiarativa su struttura e vincoli dell'ambiente

Questa separazione distingue evidence, procedura, e conoscenza ambientale, convertendo storici rumorosi in astrazioni governabili.

## Skill Crystallization

Le policy L2 diventano skill quando:
- Mantengono evidence links di supporto
- Mostrano estimated gain positivo
- Rimangono consistenti con trigger, procedura, e boundary di applicabilità

Le skill includono: trigger, procedura, boundary di applicabilità, regole di verifica, stima di affidabilità.

## Reflection-Weighted Value Backfilling

Propaga feedback terminale sparse attraverso self-reflection dense locali, producendo valori calibrati per evidence per ogni trace. Governando così l'evoluzione sia della memoria che delle skill.

## Risultati

Outperforma SOTA skill-augmented e memory-driven baselines su EvoAgentBench e LoCoMo, con forte trasferibilità cross-domain e capacità di evoluzione lifelong.

## Sviluppi: programmatic memory e auto-memory

Due nuove fonti ampliano il quadro della memoria per agenti:

**PRO-LONG** ([[wiki/sources/arxiv-2607.20064-pro-long]]) introduce la **programmatic memory** come quarto paradigma oltre L1/L2/L3. Il tradeoff centrale è fidelity-tractability: più informazione si persiste, più il recupero diventa intrattabile. PRO-LONG spezza il vincolo salvando tutto (append-all log lossless) ma recuperando via codice (grep/regex/search nativo per coding agent). Risultato: +18pt su ARC-AGI-3 vs base coding agent, SOTA con 4.2-5.8x meno token. La distinzione chiave è **accessed context** (window attiva, ~100k-1M token) vs **accessible context** (memoria tool-reachable, 10M+ token). Il design è reso possibile dalla maturazione dei coding agent stessi: la programmatic memory non è un'astrazione aggiunta, sfrutta capability già presenti.

**Claude 5** ([[wiki/sources/anthropic-claude-5-context-engineering]]) sposta la memoria da manuale ad automatica: l'agente salva memorie rilevanti senza intervento dell'utente (#hotkey non più necessario). Conferma la traiettoria: meno fardello cognitivo sull'umano, più carico sull'agente che decide cosa ricordare.

La convergenza: MSCE cristallizza tracce in skill, PRO-LONG le rende trattabili via codice, Claude 5 le automatizza. Tre risposte alla stessa domanda: cosa sopravvive tra le esecuzioni e come si recupera.
