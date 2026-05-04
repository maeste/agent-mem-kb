---
type: page
created: 2026-05-04
updated: 2026-05-04
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-05-04*

## Dove sta andando il mio pensiero

La vault si è riempita rapidamente con 19 paper arXiv tutti centrati su un tema molto specifico: **memoria per agenti LLM**. L'interesse è chiaramente rivolto a come rendere gli agenti capaci di persistere, riutilizzare esperienza e apprendere continuamente. Si delinea un arco narrativo che va dalle architetture pratiche (sistemi multi-tipo, multi-agente) alle riflessioni teoriche sul significato stesso di "memoria" per un agente artificiale, passando per la dimenticanza come componente essenziale.

## Cosa non sto guardando

- **Memoria embodied e multimodale** — solo MIRIX e OCR-Memory toccano il mondo visivo/multimodale; mancano paper su memoria per robotica e agenti fisici [[wiki/pages/llm-agent-memory]]
- **Valutazione standardizzata** — i benchmark sono frammentati (LOCOMO, LongMemEval, SWE-Bench, ALFWorld, ecc.); manca una comprensione di come si confrontano [[wiki/sources/du-2026-memory-survey]]
- **Applicazioni produttive** — la maggior parte dei paper è accademica; mancano casi studio di deploy reale in produzione
- **Memoria condivisa tra agenti** — il focus è individuale; la letteratura su memoria collaborativa multi-agente è assente dalla vault
- **Il gap teorico di Xu et al.** — la critica che retrieval = lookup ≠ memory è potente ma non ha ancora una pagina dedicata e merita approfondimento [[wiki/sources/xu-2026-contextual-agentic-memory]]

## Una domanda che vale la pena sedersi sopra

Se la memoria esterna è fondamentalmente *lookup per similarità* e ha un limite di generalizzazione compositiva provabile (come argomenta Xu et al.), quali combinazioni di retrieval + weight consolidation sono fattibili oggi con la tecnologia disponibile, e a quale costo? In altre parole: quanto manca per avere agenti che *imparano* invece di solo *archiviare*?
