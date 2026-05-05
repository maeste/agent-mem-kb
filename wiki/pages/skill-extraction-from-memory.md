---
type: page
created: 2026-05-04
updated: 2026-05-05
tags: [llm-agents, memory, skills, procedural-memory, skill-discovery, open-questions, agent-skills]
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
- Il SoK di Jiang et al. formalizza la skill come tupla S = (C, π, T, R) — condizioni di applicabilità, policy eseguibile, criteri di terminazione, interfaccia richiamabile riusabile — distinguendola in modo netto da tool atomici, piani one-shot e memoria episodica [[wiki/sources/arxiv-2602.20867]]
- SkillX articola una gerarchia esplicita a tre livelli (piani strategici → skill funzionali → skill atomiche) sostenendo che una rappresentazione strutturata e gerarchica dell'esperienza è essenziale per skill generalizzabili, contro l'appiattimento di traiettorie o "insight" piatti [[wiki/sources/arxiv-2604.04804]]
- La rappresentazione SSL (Scheduling-Structural-Logical) separa tre layer informativi oggi confusi nel testo SKILL.md — interfaccia di scheduling, fasi strutturali (prepare/act/acquire/verify/finish), azioni atomiche con side-effect — migliorando MRR@50 da 0.649 a 0.729 nel discovery e F1 da 0.409 a 0.509 nel risk assessment [[wiki/sources/arxiv-2604.24026]]

## Mattone 2 — L'astrazione paga (evidenza empirica)

Il passaggio "episodio grezzo → skill formalizzata" non è solo ergonomico, è funzionalmente migliore:

- Su ALFWorld e BabyAI, *memorie procedurali astratte si trasferiscono più affidabilmente delle traiettorie dettagliate* [[wiki/sources/hu-2026-continual-learning-memory]]
- Un'organizzazione più fine della memoria non è universalmente benefica: serve il giusto livello di astrazione, non più granularità [[wiki/sources/hu-2026-continual-learning-memory]]
- Il negative transfer colpisce sproporzionatamente i casi difficili — l'astrazione mal calibrata può peggiorare le prestazioni invece di trasferirle [[wiki/sources/hu-2026-continual-learning-memory]]
- SKILL RL dimostra che la distillazione da traiettoria a skill riduce l'footprint di token e migliora l'utilità di reasoning — la co-evoluzione di skill e policy supera il paradigma di memoria statica [[wiki/sources/xia-2026-skill-rl]]
- SkillFlow dimostra che il retrieval di skill da un corpus di 36K definizioni è formalizzabile come problema IR multi-stage, ma il collo di bottiglia non è il retrieval: è la qualità della skill library [[wiki/sources/li-2026-skillflow]]
- EvoSkill fornisce evidenza empirica di trasferibilità a livello di skill: una skill evoluta su SealQA migra zero-shot a BrowseComp (+5.3%) senza modifiche, in contrasto con prompt- o code-level evolution che rimangono vincolati al binomio modello-task [[wiki/sources/arxiv-2603.02766]]
- AgentSkillOS mostra che a parità di set di skill ottimale, l'orchestrazione strutturata via DAG batte significativamente l'invocazione piatta — la composizione, non la mera disponibilità, è il fattore critico [[wiki/sources/arxiv-2603.02176]]
- SoK riporta che skill library curate migliorano sostanzialmente i success rate, ma skill auto-generate possono degradare le performance: la pipeline di estrazione ha bisogno di gate qualitativi non banali [[wiki/sources/arxiv-2602.20867]]

## Mattone 3 — Consolidamento offline come pipeline di estrazione

L'estrazione di skill è naturalmente un processo asincrono, separato dall'esecuzione:

- LightMem ha un consolidation step offline che *astrae evidenze di interazione riutilizzabili e le integra incrementalmente nella LTM* [[wiki/sources/zhang-2026-lightmem]]
- ALAS distilla esperienza in dati di training e consolida via SFT + DPO [[wiki/sources/atreja-2025-alas]] — paradigma alternativo: skill nei pesi anziché in un registry esterno
- Evo-Memory fa self-evolving memory durante lo streaming di task, convertendo interazioni in retrievable experience [[wiki/sources/wei-2026-evo-memory]]
- EvoSkill istanzia il consolidamento offline come tre agenti collaboranti — Executor / Proposer / Skill-Builder — che diagnosticano fallimenti, propongono nuove skill e le materializzano in cartelle strutturate; un Pareto frontier filtra solo le skill che migliorano la validation con LLM congelato [[wiki/sources/arxiv-2603.02766]]
- SkillFoundry alterna mining e validazione su un domain knowledge tree, dove rami sotto-coperti triggerano mining mirato; ogni skill passa execution / system / synthetic-data testing prima di entrare nella library, con il 71.1% di skill prodotte distinte da SkillHub e SkillSMP [[wiki/sources/arxiv-2604.03964]]
- Bi et al. propongono il mining sistematico di repository GitHub agentici come pipeline a tre stadi (analisi strutturale → identificazione semantica via dense retrieval → traduzione in SKILL.md), via di mezzo scalabile tra authoring manuale e scoperta autonoma open-world [[wiki/sources/arxiv-2603.11808]]
- SkillX combina Multi-Level Skills Design + Iterative Skills Refinement (revisione su feedback di esecuzione) + Exploratory Skills Expansion (generazione proattiva oltre i seed), affrontando il triplo problema di apprendimento isolato, debole generalizzazione e cap di capacità del modello esploratore [[wiki/sources/arxiv-2604.04804]]

## Mattone 4 — Attivazione proattiva on-demand

Un registry di skill ha senso solo se l'agente sa *quando* attivare cosa. ProactAgent modella il retrieval come azione esplicita di policy con paired-branch process rewards, apprendendo quando e cosa recuperare [[wiki/sources/cai-2026-proactagent]]. È il meccanismo che mancherebbe a un servizio passivo di skill lookup.

## Risposta a una critica fondamentale

Xu et al. sostengono che i sistemi attuali fanno *lookup* per somiglianza, non sviluppano competenza compositiva: accumulano note senza diventare bravi [[wiki/sources/xu-2026-contextual-agentic-memory]]. Una skill formalizzata, parametrica e versionata è una possibile risposta operativa a quella critica — la skill è competenza riutilizzabile, non un episodio recuperato per somiglianza. Il gap tra retrieval e reasoning evidenziato da ActMem va nella stessa direzione: recuperare non basta, serve integrare con esecuzione strutturata [[wiki/sources/actmem]].

## Gap aperto — l'externalizzazione (ora parzialmente coperta)

Tutte le 19 fonti originali trattano memoria e skill come **interne all'agente**. Le 5 fonti nuove su agent skills (VOYAGER, SkillFlow, Ling 2026, SKILL RL, Xu & Yan 2026) riducono parzialmente il gap:

- **Registry esterno condiviso**: lo standard SKILL.md + l'ecosistema agentskills.io con 62K+ stelle GitHub in 4 mesi forniscono il formato e la distribuzione. SkillFlow dimostra retrieval scalabile su 36K skill da GitHub [[wiki/sources/li-2026-skillflow]] [[wiki/sources/xu-2026-agent-skills-survey]]
- **Protocollo di discovery**: il progressive disclosure a tre livelli (metadata → instructions → resources) risolve il problema dell'efficienza di contesto per skill library grandi [[wiki/sources/xu-2026-agent-skills-survey]]
- **Rimangono aperti**: il processo di estrazione automatica da memoria → SKILL.md, la governance cross-agente, e la sicurezza — il 26.1% delle skill community contiene vulnerabilità [[wiki/sources/xu-2026-agent-skills-survey]] [[wiki/sources/ling-2026-agent-skills-analysis]]
- **Mining strutturale come ponte**: l'estrazione automatica da repo open-source [[wiki/sources/arxiv-2603.11808]] e l'auto-costruzione di skill knowledge base [[wiki/sources/arxiv-2604.04804]] [[wiki/sources/arxiv-2604.03964]] iniziano a coprire la pipeline memoria → skill, mentre il SoK sistematizza i sette stadi del lifecycle (discovery, practice, distillation, storage, composition, evaluation, update) come framework cross-cutting [[wiki/sources/arxiv-2602.20867]]

## Domanda da sedersi sopra

Se le skill sono comportamenti ricorrenti astratti dalla memoria, il loro confine è epistemologico (cosa conta come "stessa skill"?) o pragmatico (cosa è abbastanza riutilizzabile da meritare reificazione)? La differenza determina chi può popolare il registry: solo l'agente stesso, oppure un processo collettivo di consolidamento cross-agente.
