---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [lifelong-learning, self-updating, fine-tuning, dpo, autonomous]
source_path: raw/papers/arxiv-2508.15805.pdf
---

# ALAS: Autonomous Learning Agent for Self-Updating Language Models

**Autori:** Dhruv Atreja
**arXiv:** 2508.15805 | Agosto 2025

## Riassunto

ALAS è una pipeline modulare che aggiorna continuamente la conoscenza di un LLM con intervento umano minimo. Il sistema genera autonomamente un curriculum di apprendimento per un dominio target, recupera informazioni aggiornate dal web (con citazioni), le distilla in dati di training Q&A, e fine-tuna il modello tramite SFT e DPO. Valuta iterativamente performance e revises il curriculum.

Dimostrato su domini a rapida evoluzione (nuovi release Python, security CVE, trend accademici), migliorando l'accuratezza QA post-cutoff dal 15% al 90% in media. Ogni componente (planning, retrieval, distillation, memory, fine-tuning) è intercambiabile e basato su API standard. Raggiunge 85-90% di accuratezza su query con conoscenza aggiornata.

## Claim chiave

- Il pipeline autonomo planning-retrieval-distillation-fine-tuning può mantenere LLM aggiornati senza curation manuale di dataset [[wiki/sources/arxiv-2508.15805.md]]
- La combinazione SFT + DPO supera RAG per accuratezza su knowledge-updated queries [[wiki/sources/arxiv-2508.15805.md]]
- La modularità dei componenti abilita sostituzione e riproducibilità [[wiki/sources/arxiv-2508.15805.md]]

## Collegamenti

- Alternativa all'approccio memory-based di [[wiki/sources/du-2026-memory-survey.md]] (survey memory)
- Relazionato a [[wiki/pages/lifelong-learning]]
- Confronta con [[wiki/sources/cai-2026-proactagent.md]] (ProactAgent) su lifelong learning
