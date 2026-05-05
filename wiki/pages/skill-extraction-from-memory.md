---
type: page
created: 2026-05-04
updated: 2026-05-05
tags: [llm-agents, memory, skills, procedural-memory, skill-discovery, open-questions]
---

# Estrazione di Skill dalla Memoria

Ipotesi di lavoro: comportamenti ricorrenti osservabili nella memoria di un agente possono essere astratti, formalizzati come *skill* riutilizzabili e gestiti tramite un servizio esterno di retrieval e attivazione on-demand. La letteratura ingestata supporta i singoli mattoni di questa pipeline ma non l'esternalizzazione del catalogo.

## Mattone 1 — Skill come categoria nativa di memoria

Diversi sistemi trattano già le skill come oggetti di memoria distinti dagli episodi:

- ProactAgent struttura la propria experience base in tre tipi: *factual, episodic, **behavioral skills*** [[wiki/sources/cai-2026-proactagent]]
- MIRIX include una Procedural Memory di prima classe tra i sei moduli, con Memory Manager dedicato [[wiki/sources/wang-2025-mirix]]
- La survey Du 2026 conferma il substrato procedurale come dimensione tassonomica standard insieme a fattuale ed episodico [[wiki/sources/du-2026-memory-survey]]
- VOYAGER introduce la prima skill library per agenti LLM embodied, memorizzando programmi JavaScript composable con retrieval per embedding similarity — le skill sono temporally extended e mitigano il catastrophic forgetting [[wiki/sources/wang-2023-voyager]]
- La survey Xu & Yan 2026 sistematizza l'intero paradigma: le agent skills sono pacchetti compostabili (SKILL.md + script + risorse) caricati on-demand, con architettura progressive disclosure a tre livelli che elimina la penalità di contesto per skill library grandi [[wiki/sources/xu-2026-agent-skills-survey]]
- SKILL RL estende il paradigma con distillazione experience-based: traiettorie grezze → skill gerarchiche (generali + task-specific) che co-evolvono con la policy durante RL, superando i baseline del 15.3% con meno contesto [[wiki/sources/xia-2026-skill-rl]]

## Mattone 2 — L'astrazione paga (evidenza empirica)

Il passaggio "episodio grezzo → skill formalizzata" non è solo ergonomico, è funzionalmente migliore:

- Su ALFWorld e BabyAI, *memorie procedurali astratte si trasferiscono più affidabilmente delle traiettorie dettagliate* [[wiki/sources/hu-2026-continual-learning-memory]]
- Un'organizzazione più fine della memoria non è universalmente benefica: serve il giusto livello di astrazione, non più granularità [[wiki/sources/hu-2026-continual-learning-memory]]
- Il negative transfer colpisce sproporzionatamente i casi difficili — l'astrazione mal calibrata può peggiorare le prestazioni invece di trasferirle [[wiki/sources/hu-2026-continual-learning-memory]]
- SKILL RL dimostra che la distillazione da traiettoria a skill riduce l'footprint di token e migliora l'utilità di reasoning — la co-evoluzione di skill e policy supera il paradigma di memoria statica [[wiki/sources/xia-2026-skill-rl]]
- SkillFlow dimostra che il retrieval di skill da un corpus di 36K definizioni è formalizzabile come problema IR multi-stage, ma il collo di bottiglia non è il retrieval: è la qualità della skill library [[wiki/sources/li-2026-skillflow]]

## Mattone 3 — Consolidamento offline come pipeline di estrazione

L'estrazione di skill è naturalmente un processo asincrono, separato dall'esecuzione:

- LightMem ha un consolidation step offline che *astrae evidenze di interazione riutilizzabili e le integra incrementalmente nella LTM* [[wiki/sources/zhang-2026-lightmem]]
- ALAS distilla esperienza in dati di training e consolida via SFT + DPO [[wiki/sources/atreja-2025-alas]] — paradigma alternativo: skill nei pesi anziché in un registry esterno
- Evo-Memory fa self-evolving memory durante lo streaming di task, convertendo interazioni in retrievable experience [[wiki/sources/wei-2026-evo-memory]]

## Mattone 4 — Attivazione proattiva on-demand

Un registry di skill ha senso solo se l'agente sa *quando* attivare cosa. ProactAgent modella il retrieval come azione esplicita di policy con paired-branch process rewards, apprendendo quando e cosa recuperare [[wiki/sources/cai-2026-proactagent]]. È il meccanismo che mancherebbe a un servizio passivo di skill lookup.

## Risposta a una critica fondamentale

Xu et al. sostengono che i sistemi attuali fanno *lookup* per somiglianza, non sviluppano competenza compositiva: accumulano note senza diventare bravi [[wiki/sources/xu-2026-contextual-agentic-memory]]. Una skill formalizzata, parametrica e versionata è una possibile risposta operativa a quella critica — la skill è competenza riutilizzabile, non un episodio recuperato per somiglianza. Il gap tra retrieval e reasoning evidenziato da ActMem va nella stessa direzione: recuperare non basta, serve integrare con esecuzione strutturata [[wiki/sources/actmem]].

## Gap aperto — l'externalizzazione (ora parzialmente coperta)

Tutte le 19 fonti originali trattano memoria e skill come **interne all'agente**. Le 5 fonti nuove su agent skills (VOYAGER, SkillFlow, Ling 2026, SKILL RL, Xu & Yan 2026) riducono parzialmente il gap:

- **Registry esterno condiviso**: lo standard SKILL.md + l'ecosistema agentskills.io con 62K+ stelle GitHub in 4 mesi forniscono il formato e la distribuzione. SkillFlow dimostra retrieval scalabile su 36K skill da GitHub [[wiki/sources/li-2026-skillflow]] [[wiki/sources/xu-2026-agent-skills-survey]]
- **Protocollo di discovery**: il progressive disclosure a tre livelli (metadata → instructions → resources) risolve il problema dell'efficienza di contesto per skill library grandi [[wiki/sources/xu-2026-agent-skills-survey]]
- **Rimangono aperti**: il processo di estrazione automatica da memoria → SKILL.md, la governance cross-agente, e la sicurezza — il 26.1% delle skill community contiene vulnerabilità [[wiki/sources/xu-2026-agent-skills-survey]] [[wiki/sources/ling-2026-agent-skills-analysis]]

## Domanda da sedersi sopra

Se le skill sono comportamenti ricorrenti astratti dalla memoria, il loro confine è epistemologico (cosa conta come "stessa skill"?) o pragmatico (cosa è abbastanza riutilizzabile da meritare reificazione)? La differenza determina chi può popolare il registry: solo l'agente stesso, oppure un processo collettivo di consolidamento cross-agente.
