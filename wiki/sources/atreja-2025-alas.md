---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, continual-learning, self-updating, fine-tuning, autonomous]
source_path: raw/papers/arxiv-2508.15805.pdf
---

# ALAS: Autonomous Learning Agent for Self-Updating Language Models

**Autore:** Dhruv Atreja
**Data:** 2025-08-14

## Summary

ALAS è una pipeline modulare che aggiorna continuamente la conoscenza di un LLM con intervento umano minimo. Genera autonomamente curriculum di apprendimento, recupera informazioni aggiornate dal web con citazioni, distilla dati QA per training, e fine-tuna il modello via SFT e DPO. Valutato su domini in rapida evoluzione (nuovi release Python, CVE di sicurezza, trend accademici), migliora l'accuracy da ~15% a ~90% su query post-cutoff.

Dimostra che il fine-tuning supera il RAG puro per knowledge internalization, e che il loop autonomo può operare con overhead ingegneristico minimo componendo API esistenti (OpenAI Deep Research + LangGraph).

[[wiki/pages/experience-reuse-continual-learning]]
