---
type: page
created: 2026-05-04
updated: 2026-07-16
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-07-16*

## Dove sta andando il mio pensiero

La vault è ferma dal 5 maggio, ma il contenuto che ha accumulato in due giorni è denso: 36 sorgenti su memoria per agenti LLM e agent skills, 5 pagine concettuali ben collegate tra loro. L'asse principale rimane la transizione da "memoria come lookup" a "memoria che cristallizza in skill riutilizzabili" — e la pagina [[wiki/pages/skill-extraction-from-memory]] è diventata il cuore della collezione, con quattro mattoni empiricamente supportati. La vault ha raggiunto una densità critica su questo asse: le domande aperte non sono più sulla fattibilità dei singoli componenti (estrazione, retrieval proattivo, registry esterno) ma su come si compongono insieme in un sistema coerente.

## Cosa non sto guardando

- **La vault è congelata da oltre 2 mesi** (5 maggio → 16 luglio). Nessun nuovo ingresso, nessuna view costruita, nessun aggiornamento delle pagine concettuali. Le 26 sorgenti arXiv senza source entry nominale (ma coperte da entry con nome autore) sono un artefatto di nomenclatura, non un reale gap di contenuto.
- **`wiki/views/` è ancora vuota**: due view erano state proposte in hot.md il 5 maggio — confronto architetture skill library e timeline 2023→2026 dell'evoluzione agent skills — e non sono mai state realizzate. Il materiale c'è tutto.
- **La critica di Xu et al.** (lookup ≠ memory) merita ancora una pagina dedicata: vive distribuita in citazioni sparse in [[wiki/pages/llm-agent-memory]] e [[wiki/pages/skill-extraction-from-memory]] senza un luogo proprio dove sviluppare l'implicazione teorica completa.
- **Memoria condivisa multi-agente**: nessuna delle 36 fonti affronta direttamente il problema della memoria condivisa tra agenti. Il registry esterno di skill tocca il tema lateralmente ma non lo risolve.
- **Il cluster sicurezza/governance delle skill** ([[wiki/sources/arxiv-2604.23080]], [[wiki/sources/arxiv-2604.16911]], [[wiki/sources/ling-2026-agent-skills-analysis]]) è presente in [[wiki/pages/forgetting-memory-governance]] ma potrebbe meritare una propria sottosezione o mini-pagina data la densità di evidenze.
- **Tensione SoK vs ottimismo auto-generazione**: SoK avverte che skill auto-generate possono degradare performance, EvoSkill/SkillFoundry/SkillX spingono sull'auto-generazione, SkVM mostra che il 15% dei task peggiora con skill abilitate. Questa tensione non è mai stata sintetizzata esplicitamente.

## Una domanda che vale la pena sedersi sopra

La vault ha smesso di crescere esattamente quando raggiungeva la massa critica necessaria per produrre sintesi originali (view, confronti, timeline). È un segnale che il modello di curatela — utente aggiunge sorgenti, agente ingesta — ha funzionato per l'accumulo ma non per la distillazione. Cosa servirebbe per sbloccare la fase successiva: una sessione dedicata alla costruzione di view, o nuove sorgenti che riaccendano l'interesse?
