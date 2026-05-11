---
type: page
created: 2026-05-04
updated: 2026-05-11
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-05-11*

## Dove sta andando il mio pensiero

Sei giorni dopo il burst iniziale (19 paper il 4 maggio, 17 il 5 maggio), la vault si è stabilizzata: 36 sorgenti, 6 pagine concettuali, zero gap di ingestione. L'asse dominante è passato dalla domanda "come ricordano gli agenti?" a "come la memoria si cristallizza in artefatti riutilizzabili e condivisibili?" — e poi ancora più in là, verso "come si governa un ecosistema di 280K+ artefatti eseguibili condivisi tra agenti eterogenei?". La pagina [[wiki/pages/agent-skills-ecosystem]] è diventata la più ricca e la più vicina a un'ipotesi operativa: le agent skills seguono la traiettoria dei package manager, con gli stessi problemi di sicurezza e composizione che npm e pip hanno dovuto affrontare — solo che qui il costo di una dipendenza malevola è esfiltrazione di API key, non un build rotto.

## Cosa non sto guardando

- **La critica di Xu et al. merita ancora una pagina dedicata.** La tesi "lookup ≠ memory" è citata in tre pagine ([[wiki/pages/llm-agent-memory]], [[wiki/pages/skill-extraction-from-memory]], [[wiki/pages/forgetting-memory-governance]]) ma non ha un luogo proprio dove il suo argomento — generalizzazione compositiva, teoria CLS, proposta di co-esistenza peso+retrieval — possa essere sviluppato in profondità. Rimane la domanda più teoricamente ambiziosa della vault.
- **Due view proposte e mai costruite:** confronto architetture skill library (VOYAGER, SkillFlow, SKILL RL, SkillFoundry, SkillX) e timeline 2023→2026 dell'evoluzione delle agent skills. La cartella `wiki/views/` è vuota dopo una settimana. Il materiale c'è, la sintesi no.
- **Le pagine sulla memoria pura ([[wiki/pages/llm-agent-memory]], [[wiki/pages/memory-architectures-retrieval]], [[wiki/pages/experience-reuse-continual-learning]], [[wiki/pages/forgetting-memory-governance]])** sono ferme al 4-5 maggio. Nessuna ha assorbito i paper più recenti (arxiv-2604.*) che riguardano contestualmente il loro dominio — ad esempio ContextWeaver ([[wiki/sources/wu-2026-contextweaver]]) è citato solo in architetture-retrieval, ma la sua tesi sulle dipendenze causali tra step di reasoning potrebbe arricchire la pagina sul riutilizzo dell'esperienza.
- **Memoria condivisa multi-agente:** nessuna delle 36 fonti la affronta direttamente. Il più vicino è MIRIX con il suo modulo Knowledge Vault, ma il focus resta individuale. Il discovery decentralizzato (Dazzi et al.) tocca la coordinazione ma non la memoria condivisa *per sé*.
- **Tensione non risolta tra ottimismo e cautela sulle skill auto-generate:** SkVM mostra che il 15% dei task peggiora con skill abilitate, il SoK avverte che skill auto-generate possono degradare la performance, SRA mostra che l'incorporation è il collo di bottiglia — ma SkillFoundry (71.1% di skill uniche) e SkillX (miglioramento su agenti più deboli) spingono nella direzione opposta. Non c'è una pagina che metta sistematicamente a confronto l'evidenza pro e contro.

## Una domanda che vale la pena sedersi sopra

Hai costruito una vault che documenta come un intero campo di ricerca sta passando dal "come faccio ricordare un agente?" al "come faccio condividere ciò che ha imparato con altri agenti?" — ma tutte le 36 fonti descrivono sistemi chiusi, experimental, single-agent o multi-agent con memoria privata. Se il passo successivo è davvero un ecosistema condiviso (registry, discovery, governance), chi sono gli utenti finali che lo richiedono? Sono gli sviluppatori che orchestrano agenti, oppure gli agenti stessi che negoziano? La risposta cambia radicalmente l'architettura di trust che stai documentando.
