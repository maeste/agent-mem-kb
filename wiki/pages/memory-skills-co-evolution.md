---
type: page
created: 2026-07-23
updated: 2026-07-23
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
