---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, skills, empirical-analysis, marketplace, safety, ecosystem]
source_path: raw/papers/arxiv-2602.08004.pdf
---

# Agent Skills: A Data-Driven Analysis of Claude Skills for Extending LLM Functionality

George Ling (Bosch Research), Shanshan Zhong, Richard Huang (CMU), arXiv:2602.08004, 2026.

## Summary

Analisi quantitativa su larga scala di 40.285 skill pubbliche da un marketplace di agent skills. Lo studio rivela che: (1) la pubblicazione di skill avviene in burst che tracciano i cambiamenti nell'attenzione della community; (2) il contenuto è altamente concentrato in workflow di software engineering, con information retrieval e content creation che dominano l'adozione; (3) c'è un pronunciato sbilanciamento domanda-offerta tra categorie; (4) la maggior parte delle skill rientra nei budget di prompt tipici nonostante distribuzione heavy-tailed della lunghezza; (5) l'ecosistema mostra forte omogeneità con ridondanza a livello di intent; (6) esistono rischi di sicurezza non banali, incluse skill che abilitano azioni state-changing o system-level. Il lavoro fornisce uno snapshot quantitativo dell'infrastruttura skill come layer emergente per agenti.

## Key claims

- L'ecosistema delle agent skills cresce rapidamente ma in modo diseguale: supply dominata da software engineering, adozione concentrata su IR e content creation [[wiki/pages/skill-extraction-from-memory]]
- La ridondanza a livello di intent è pervasiva — molte skill differiscono nella forma ma condividono lo stesso proposito, suggerendo la necessità di de-duplicazione semantica
- Un sottoinsieme non banale di skill pubbliche abilita azioni a livello di sistema, creando superfici di attacco per prompt injection realistici e banali
