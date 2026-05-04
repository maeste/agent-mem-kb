---
type: page
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, skills, procedural-memory, skill-discovery, open-questions]
---

# Estrazione di Skill dalla Memoria

Ipotesi di lavoro: comportamenti ricorrenti osservabili nella memoria di un agente possono essere astratti, formalizzati come *skill* riutilizzabili e gestiti tramite un servizio esterno di retrieval e attivazione on-demand. La letteratura ingestata supporta i singoli mattoni di questa pipeline ma non l'esternalizzazione del catalogo.

## Mattone 1 — Skill come categoria nativa di memoria

Diversi sistemi trattano già le skill come oggetti di memoria distinti dagli episodi:

- ProactAgent struttura la propria experience base in tre tipi: *factual, episodic, **behavioral skills*** [[wiki/sources/cai-2026-proactagent]]
- MIRIX include una Procedural Memory di prima classe tra i sei moduli, con Memory Manager dedicato [[wiki/sources/wang-2025-mirix]]
- La survey Du 2026 conferma il substrato procedurale come dimensione tassonomica standard insieme a fattuale ed episodico [[wiki/sources/du-2026-memory-survey]]

## Mattone 2 — L'astrazione paga (evidenza empirica)

Il passaggio "episodio grezzo → skill formalizzata" non è solo ergonomico, è funzionalmente migliore:

- Su ALFWorld e BabyAI, *memorie procedurali astratte si trasferiscono più affidabilmente delle traiettorie dettagliate* [[wiki/sources/hu-2026-continual-learning-memory]]
- Un'organizzazione più fine della memoria non è universalmente benefica: serve il giusto livello di astrazione, non più granularità [[wiki/sources/hu-2026-continual-learning-memory]]
- Il negative transfer colpisce sproporzionatamente i casi difficili — l'astrazione mal calibrata può peggiorare le prestazioni invece di trasferirle [[wiki/sources/hu-2026-continual-learning-memory]]

## Mattone 3 — Consolidamento offline come pipeline di estrazione

L'estrazione di skill è naturalmente un processo asincrono, separato dall'esecuzione:

- LightMem ha un consolidation step offline che *astrae evidenze di interazione riutilizzabili e le integra incrementalmente nella LTM* [[wiki/sources/zhang-2026-lightmem]]
- ALAS distilla esperienza in dati di training e consolida via SFT + DPO [[wiki/sources/atreja-2025-alas]] — paradigma alternativo: skill nei pesi anziché in un registry esterno
- Evo-Memory fa self-evolving memory durante lo streaming di task, convertendo interazioni in retrievable experience [[wiki/sources/wei-2026-evo-memory]]

## Mattone 4 — Attivazione proattiva on-demand

Un registry di skill ha senso solo se l'agente sa *quando* attivare cosa. ProactAgent modella il retrieval come azione esplicita di policy con paired-branch process rewards, apprendendo quando e cosa recuperare [[wiki/sources/cai-2026-proactagent]]. È il meccanismo che mancherebbe a un servizio passivo di skill lookup.

## Risposta a una critica fondamentale

Xu et al. sostengono che i sistemi attuali fanno *lookup* per somiglianza, non sviluppano competenza compositiva: accumulano note senza diventare bravi [[wiki/sources/xu-2026-contextual-agentic-memory]]. Una skill formalizzata, parametrica e versionata è una possibile risposta operativa a quella critica — la skill è competenza riutilizzabile, non un episodio recuperato per somiglianza. Il gap tra retrieval e reasoning evidenziato da ActMem va nella stessa direzione: recuperare non basta, serve integrare con esecuzione strutturata [[wiki/sources/actmem]].

## Gap aperto — l'externalizzazione mancante

Tutte e 19 le fonti ingestate trattano memoria e skill come **interne all'agente**. Nessuna propone:

- un **registry esterno condiviso** di skill in stile agentskills.io
- un **protocollo di discovery** che permetta a più agenti di pubblicare/scoprire/versionare skill
- un **modello di attivazione** che sia agnostico rispetto all'agente che ha generato la skill

MCP (Model Context Protocol) è il punto di partenza più vicino sul lato tool/risorsa, ma non è ancora oggetto di paper nella vault e non risolve il problema dell'estrazione automatica da memoria.

## Domanda da sedersi sopra

Se le skill sono comportamenti ricorrenti astratti dalla memoria, il loro confine è epistemologico (cosa conta come "stessa skill"?) o pragmatico (cosa è abbastanza riutilizzabile da meritare reificazione)? La differenza determina chi può popolare il registry: solo l'agente stesso, oppure un processo collettivo di consolidamento cross-agente.
