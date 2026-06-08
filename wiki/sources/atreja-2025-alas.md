---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [self-updating-llm, autonomous-learning, continual-learning, fine-tuning]
source_path: raw/papers/arxiv-2508.15805.pdf
---

# ALAS: Autonomous Learning Agent for Self-Updating Language Models

**Dhruv Atreja** — arXiv:2508.15805, Aug 2025

## Summary

ALAS (Autonomous Learning Agent System) è una pipeline modulare che aggiorna continuamente la conoscenza di un LLM con intervento umano minimo. Il sistema genera autonomamente un curriculum di apprendimento per un dominio target, recupera informazioni aggiornate dal web (con citazioni), le distilla in dati di training Q&A, e fine-tuna il modello tramite SFT e DPO. Valuta iterativamente le performance e revisa il curriculum.

Componenti modulari (ognuno intercambiabile): planning, retrieval, distillation, memory, fine-tuning. Testato su domini a rapida evoluzione (nuovi release Python, security CVEs, trend accademici): accuracy su query post-cutoff da ~15% al ~90% in media. Usa API standard (OpenAI Deep Research, Fine-Tuning) e LangGraph come orchestrator.

## Key claims
- L'auto-generazione di dati di training con citazioni elimina la necessità di dataset curati ([§Abstract](raw/papers/arxiv-2508.15805.pdf))
- La combinazione SFT + DPO supera RAG puro o SFT senza DPO ([§5](raw/papers/arxiv-2508.15805.pdf))
- La modularità rende il sistema riproducibile con overhead ingegneristico minimo ([§4](raw/papers/arxiv-2508.15805.pdf))

## Connections
- [[wiki/sources/atreja-2025-alas]] — fonte primaria
- [[wiki/pages/continual-learning]] — apprendimento continuo in agenti
