---
type: page
created: 2026-05-04
updated: 2026-07-02
tags: [reflection, compass]
---

# Bussola

## Dove sta andando il mio pensiero

Il vault ha raggiunto una massa critica su due fronti paralleli che stanno convergendo: **memoria agentica** e **agent skills**. Il batch di oggi (15 sorgenti) completa il quadro sulla memoria con contributi che toccano tutti gli angoli: dalla critica teorica radicale (Xu et al.: lookup ≠ memory) alla governance operativa (Simsek: Memory Worth), passando per architetture concrete (Memanto, ContextWeaver, OCR-Memory, LightMem, ActMem, RSCB-MC). La tesi di Xu et al. sta emergendo come filo conduttore che riorganizza l'intero campo: i 36 paper del vault possono essere letti come tentativi di risolvere problemi diversi dello stesso sistema C-engineering, mentre la riga "experiential" della taxonomy rimane vuota.

Sulle agent skills, il vault copre ora l'intero lifecycle dal discovery alla governance, con dati empirici su 40K+ skills pubbliche. La tensione tra ottimismo (skill auto-generate, librerie self-evolving) e cautela (26.1% vulnerabili, 15% task peggiorano con skill abilitate) è un pattern ricorrente che merita sintesi.

## Cosa non sto guardando

- **9 paper in raw/papers/ ancora senza wiki/sources/** (i più vecchi: arxiv-2305.16291, arxiv-2504.06188, arxiv-2507.07957, arxiv-2507.21428, arxiv-2508.15805, arxiv-2511.20857, arxiv-2601.01885, arxiv-2601.20352, arxiv-2602.05665). Sono i paper meno recenti, potrebbero contenere lavori fondazionali o essere fuori scope
- **Nessuna view è stata costruita**: mancano timeline, confronti architetturali, slide. Il materiale c'è ma non è stato sintetizzato in formati condivisibili
- **La pagina memory-fundamentals citata da diverse sorgenti non esiste**: le sorgenti puntano a `[[wiki/pages/memory-fundamentals]]` che non è mai stata creata. Stesso per `[[wiki/pages/agent-skills]]`
- **Multimodal embodied memory** è identificata come open challenge da Du survey e OCR-Memory offre un primo contributo, ma il tema resta sottorappresentato
- **Memoria condivisa multi-agente**: nessuna delle 36 fonti affronta direttamente questo problema

## Una domanda worth sitting with

Se Xu et al. hanno ragione e tutta la memoria agentica attuale è lookup mascherato da memoria, allora le agent skills (che sono essenzialmente lookup di procedure pre-scritte) soffrono dello stesso limite categoriale: uno skill library è una scatola degli attrezzi più organizzata, non un cervello che impara. Cosa significherebbe progettare un "experiential skill system" dove le skill vengono consolidate nei pesi invece che nel retrieval? SkillRL e ProactAgent fanno passi in questa direzione ma restano ancorati al paradigma C-engineering.
