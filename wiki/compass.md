---
type: page
created: 2026-07-13
updated: 2026-07-13
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-07-13*

## Dove sta andando il mio pensiero

La vault è ferma dal 5 maggio. In quei due giorni intensi sono passati da zero a 36 sorgenti, 7 pagine concettuali e un'architettura che copre memoria per agenti LLM ed ecosistema agent skills con buona profondità. Il nodo centrale resta [[wiki/pages/skill-extraction-from-memory]]: la domanda su come la memoria si cristallizza in artefatti riutilizzabili è ben supportata da quasi tutte le sorgenti, e la pagina ha assorbito evidenze da VOYAGER fino a SkillFoundry. La pagina [[wiki/pages/agent-skills-ecosystem]] complementa bene il livello di sistema (registry, distribuzione, governance). Le altre cinque pagine — llm-agent-memory, memory-architectures-retrieval, forgetting-memory-governance, experience-reuse-continual-learning, skill-extraction-from-memory — formano un nucleo solido ma non hanno avuto aggiornamenti dal batch iniziale.

## Cosa non sto guardando

- **La critica Xu et al.** ([[wiki/sources/xu-2026-contextual-agentic-memory]]) è citata in tre pagine ma non ne ha una dedicata. È l'unico paper nella vault che fa teoria fondamentale sul confine tra lookup e memoria, e merita uno spazio proprio dove le sue argomentazioni (generalizzazione compositiva, vulnerabilità strutturali, CLS theory) possano essere sviluppate senza essere diluite.
- **Le view proposte in hot.md** (confronto architetture skill library, timeline 2023-2026) non sono state costruite. La cartella `wiki/views/` è vuota. C'è materiale sufficiente per almeno un confronto strutturato.
- **Le pagine memory-architectures-retrieval e experience-reuse-continual-learning** sono rimaste al 4 maggio e non hanno integrato le sorgenti del batch skills (SKILL RL, SkillFlow, EvoSkill, AgentSkillOS) che le riguardano direttamente.
- **Il cluster sicurezza/governance** delle skill (26.1% vulnerabili, ClawHavoc) vive in agent-skills-ecosystem ma non dialoga con [[wiki/pages/forgetting-memory-governance]] che tratta lo stesso tema dal lato memoria.
- **Nessuna nuova sorgente dal 5 maggio**: la vault è statica da oltre due mesi. Se l'obiettivo è tenere traccia di un campo in rapida evoluzione (agent skills + agentic memory), questo silenzio è un segnale.

## Una domanda che vale la pena sedersi sopra

La vault ha 36 sorgenti e 7 pagine, e la struttura regge. Ma la pagina skill-extraction-from-memory continua a chiamare l'externalizzazione "parzialmente coperta" dopo aver citato SoK, AgentSkillOS, EvoSkill, SkillFoundry, SkillX, SkillFlow e il mining di repo. Quale parte del gap è davvero aperta, e quale parte viene tenuta aperta perché richiederebbe di sintetizzare una posizione che va oltre la mera citazione delle sorgenti?
