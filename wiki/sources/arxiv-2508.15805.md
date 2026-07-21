---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [self-updating-llm, continual-learning, autonomous-learning, fine-tuning]
source_path: raw/papers/arxiv-2508.15805.pdf
---

# ALAS: Autonomous Learning Agent for Self-Updating LLMs

**Autore:** Dhruv Atreja | **arXiv:** 2508.15805 | **Ago 2025**

## Summary

ALAS (Autonomous Learning Agent System) è un pipeline modulare che aggiorna continuamente la conoscenza di un LLM con intervento umano minimo. Genera autonomamente un curriculum di apprendimento per un target domain, recupera informazioni aggiornate dal web (con citazioni), le distilla in dati QA per training, e fine-tuna il modello via SFT e DPO. Valuta iterativamente performance e revisa il curriculum.

Risultati: accuracy su query post-cutoff da 15% a 90% in media su domini a rapida evoluzione (nuovi release Python, security CVE, trend accademici). Ogni componente (planning, retrieval, distillation, memory, fine-tuning) è intercambiabile e basata su API standard.

## Key claims

- L'approccio self-updating via SFT+DPO supera RAG per knowledge internalizzazione (85-90% accuracy) [[wiki/pages/alas]]
- La modularità permette swap di componenti senza riscrivere il sistema
- Limitazioni principali: costo computazionale e dipendenza dalla qualità delle sorgenti
