---
type: page
created: 2026-05-04
updated: 2026-05-25
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-05-25*

## Dove sta andando il mio pensiero

La vault ha raggiunto una fase di maturita relativa: 36 sorgenti, 6 pagine concettuali, copertura su due assi principali (memoria agent LLM e agent skills). Il punto di sutura rimane [[wiki/pages/skill-extraction-from-memory]] — la cristallizzazione della memoria in artefatti riutilizzabili. Dopo tre settimane di silenzio (5-25 maggio), nessuna nuova fonte e entrata; il lavoro di oggi e stato di manutenzione: verifica consistenza tra raw/papers/ e wiki/sources/, aggiornamento di stub a contenuto completo, e un nuovo paper (Hu et al. 2604.27003) che rafforza l'asse experience-reuse con evidenza empirica sul framework (k,v) representation/organization.

La direzione di ricerca sembra stabilizzarsi attorno a due tensioni strutturali: (1) retrieval passivo vs proattivo — ProactAgent, ActMem, Evo-Memory tutti convergono sull'idea che recuperare non basta, bisogna *sapere quando* e *cosa* recuperare; (2) complessita architetturale vs efficienza operativa — Memanto (89.8% con singola query, sub-90ms) vs AMA (multi-agent, -80% token) vs LightMem (SLM-based, 83ms) mostrano percorsi diversi verso lo stesso obiettivo.

## Cosa non sto guardando

- **wiki/views/ vuota**: due view proposte il 5 maggio (confronto architetture skill library, timeline 2023-2026 agent skills) non sono mai state costruite. Il materiale c'e, manca l'azione.
- **Critica Xu et al.** (lookup ≠ memory): ancora senza pagina dedicata dopo tre settimane. Vive distribuita in citazioni sparse in [[wiki/pages/llm-agent-memory]].
- **Memoria condivisa multi-agente**: nessuna delle 36 fonti la affronta direttamente. Gap strutturale, non accidentale.
- **Tensione skill auto-generate**: SoK avverte degradazione, EvoSkill/SkillFoundry/SkVM mostrano evidenze miste (15% task peggiorano con skill abilitate). Merita sezione concettuale dedicata in [[wiki/pages/skill-extraction-from-memory]] o pagina autonoma.
- **9 paper piu vecchi** (arxiv-2305.16291, arxiv-2504.06188, arxiv-2507.07957, arxiv-2507.21428, arxiv-2508.15805, arxiv-2511.20857, arxiv-2601.01885, arxiv-2601.20352, arxiv-2602.20867) hanno entry wiki/sources/ ma alcuni sono stub minimi da espandere (ALAS, MemTool, Evo-Memory, AgeMem, AMA, SoK).

## Una domanda che vale la pena sederci sopra

La vault ha smesso di crescere dal 5 maggio. Le 36 sorgenti coprono bene lo stato dell'arte fino ad aprile 2026, ma il campo si muove rapidamente — nuovi paper escono ogni settimana. La domanda non e "cosa manca" ma "quale sara il prossimo segnale che giustifica una nuova fetch": un paper che cambia radicalmente uno dei due assi (memoria o skills), o un terzo asse che emerge dalla loro intersezione?
