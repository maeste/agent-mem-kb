---
type: page
created: 2026-05-04
updated: 2026-06-04
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-06-04 (un mese dopo l'ultima)*

## Dove sta andando il mio pensiero

La vault è rimasta ferma al 5 maggio per un mese intero: 36 sorgenti, 6 pagine concettuali, zero view costruite. L'asse principale resta [[wiki/pages/skill-extraction-from-memory]] — la domanda di come la memoria agentica si cristallizza in artefatti riutilizzabili (skill) — ed è la pagina più sviluppata della collezione con 4 mattoni empirici e una sezione di critica. Le altre pagine ([[wiki/pages/llm-agent-memory]], [[wiki/pages/experience-reuse-continual-learning]], [[wiki/pages/forgetting-memory-governance]], [[wiki/pages/memory-architectures-retrieval]], [[wiki/pages/agent-skills-ecosystem]]) sono meno dense e alcune non sono state aggiornate dall'ingest iniziale.

La collection ha raggiunto una massa critica su due fronti: (1) la tassonomia dei sistemi di memoria agentica è completa con survey Du 2026 e Yang 2026 che coprono rispettivamente l'approccio generale e il sotto-campo graph-based; (2) l'ecosistema delle agent skills ha copertura da Voyager (2023) fino ai paper aprile 2026, includendo survey Xu & Yan 2026, benchmark (Evo-Memory), runtime (SkVM), registry (Skilldex), e rappresentazione (SSL). Il materiale per view strutturate c'è e non è stato sfruttato.

## Cosa non sto guardando

- **wiki/views/ è vuota**: due view erano state identificate il 5 maggio (confronto architetture skill library, timeline 2023→2026) e non sono mai state costruite. Con 36 sorgenti sarebbe il momento giusto.
- **La critica Xu et al.** (lookup ≠ memory, soffitto di generalizzazione provabile, memory poisoning strutturale) continua a vivere distribuita in citazioni sparse senza pagina dedicata, nonostante sia stata segnalata tre volte (bussola 4/5, bussola 5/5, hot.md).
- **Tensione non risolta**: SoK avverte che skill auto-generate possono degradare performance; SkVM mostra 15% task peggiorano con skill abilitate; EvoSkill/SkillFoundry/SkillX sono ottimisti sull'estrazione automatica. Questa tensione meriterebbe sintesi esplicita.
- **Memoria condivisa multi-agente**: nessuna delle 36 fonti affronta direttamente il problema. La vault è tutta sul singolo agente.
- **Sicurezza e governance**: cluster di paper (26.1% skill vulnerabili, RSCB-MC con abstention, FSFM con security-triggered forgetting) presente in sorgenti ma non integrato in [[wiki/pages/forgetting-memory-governance]].
- **ActMem** (retrieval-reasoning gap) è una sorgente sottile con implicazioni profonde per tutta la architettura della memoria, citata solo nella sezione critica di skill-extraction-from-memory.

## Una domanda che vale la pena sedersi sopra

La vault ha accumulato 36 sorgenti in due sessioni intense (4-5 maggio) e poi si è fermata per un mese. La struttura c'è, le connessioni tra sorgenti sono state tracciate nelle pagine, ma nessuna view è stata prodotta e la critica più radicale (Xu) non ha ancora un suo spazio. La domanda è: questa vault serve come bibliografia annotata (e in quel caso è completa e ben organizzata) o come motore di sintesi che deve ancora partire? Se è la seconda, il prossimo passo non è aggiungere sorgenti ma costruire le view che forcinganno a prendere posizione sui punti di tensione identificati.
