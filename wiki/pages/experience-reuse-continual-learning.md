---
type: page
created: 2026-05-04
updated: 2026-05-05
tags: [llm-agents, memory, continual-learning, experience-reuse]
---

# Riutilizzo dell'Esperienza e Continual Learning

Il continual learning negli agenti LLM con memoria esterna riposiziona il problema classico stabilità-plasticità dallo spazio dei pesi allo spazio della memoria: vecchie e nuove esperienze competono durante il retrieval sotto una finestra di contesto limitata [[wiki/sources/hu-2026-continual-learning-memory]].

## Meccanismi di riutilizzo

- **Self-evolving memory**: l'agente aggiorna continuamente la propria memoria durante lo streaming di task, convertendo interazioni storiche in retrievable experience [[wiki/sources/wei-2026-evo-memory]]
- **Self-updating LLMs**: pipeline automatizzate che generano curriculum, recuperano info dal web, distillano dati QA e fine-tunano il modello (SFT + DPO) [[wiki/sources/atreja-2025-alas]]
- **Proactive retrieval**: recuperare esperienza proattivamente quando si rileva un knowledge gap, piuttosto che solo all'inizio di un task [[wiki/sources/cai-2026-proactagent]]
- **Memory consolidation**: processo offline che astrae evidenze di interazione riutilizzabili e le integra incrementalmente nella LTM [[wiki/sources/zhang-2026-lightmem]]
- **Skill library con code-as-action**: VOYAGER memorizza programmi JavaScript di successo e li recupera per embedding similarity, abilitando composizione di skill temporally extended senza fine-tuning [[wiki/sources/wang-2023-voyager]]
- **Skill distillation + evoluzione ricorsiva**: SKILL RL distilla traiettorie grezze in skill gerarchiche (generali + task-specific) e le fa co-evolvere con la policy durante RL, riducendo l'footprint di token e migliorando il reasoning [[wiki/sources/xia-2026-skill-rl]]

## Risultati chiave

- Le memorie procedurali astratte si trasferiscono più affidabilmente delle traiettorie dettagliate [[wiki/sources/hu-2026-continual-learning-memory]]
- Il negative transfer danneggia sproporzionatamente i casi più difficili [[wiki/sources/hu-2026-continual-learning-memory]]
- Un'organizzazione della memoria più fine non è universalmente benefica: può causare grave forgetting anche quando migliora il forward transfer [[wiki/sources/hu-2026-continual-learning-memory]]

## Gap fra retrieval e reasoning

ActMem evidenzia il divario tra recuperare informazioni dal passato e usarle effettivamente: la semplice recall è insufficiente, serve integrare memoria con reasoning strutturato [[wiki/sources/actmem]].
