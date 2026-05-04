---
type: page
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, survey, taxonomy]
---

# Memoria per Agenti LLM

La memoria è il componente che trasforma un modello linguistico stateless in un agente adattivo capace di persistere informazioni, evitare errori ripetuti e personalizzare interazioni nel tempo [[wiki/sources/du-2026-memory-survey]].

## Tassonomia della memoria

La letteratura converge su diverse dimensioni di classificazione:

- **Scope temporale**: memoria a breve termine (STM, finestra di contesto corrente), a medio termine (MTM, riepiloghi di sessione) e a lungo termine (LTM, conoscenza consolidata) [[wiki/sources/yu-2026-agemem]] [[wiki/sources/zhang-2026-lightmem]]
- **Sottostante (substrate)**: finestra di contesto (working memory), store esterno (episodica), pesi del modello (esperienziale) [[wiki/sources/xu-2026-contextual-agentic-memory]]
- **Contenuto**: fattuale (entity, concetti), episodica (eventi, esperienze), procedurale (istruzioni passo-passo), risorse (documenti, file) [[wiki/sources/wang-2025-mirix]]
- **Controllo**: euristico vs. appreso via RL [[wiki/sources/yu-2026-agemem]] [[wiki/sources/cai-2026-proactagent]]

## Critica fondamentale

Xu et al. (2026) sostengono che i sistemi di memoria correnti implementano *lookup* (ricerca per somiglianza), non vera memoria: accumulano note senza sviluppare competenza e soffrono di un limite di generalizzazione compositiva [[wiki/sources/xu-2026-contextual-agentic-memory]]. La distinzione chiave è tra generalizzazione per similarità (ricerca) e generalizzazione per regole astratte (pesi del modello).

## Sfide aperte

- **Stabilità-plasticità nella memoria**: il problema del continual learning si trasferisce dalla parametrizzazione alla memoria esterna — vecchie e nuove esperienze competono per il retrieval sotto finestra di contesto finita [[wiki/sources/hu-2026-continual-learning-memory]]
- **Dimenticanza**: sapere cosa e quando dimenticare è tanto importante quanto ricordare [[wiki/sources/simsek-2026-when-to-forget]] [[wiki/sources/gu-2026-fsfm]]
- **Multimodalità**: la memoria deve gestire testo, immagini e schermate [[wiki/sources/wang-2025-mirix]] [[wiki/sources/li-2026-ocr-memory]]
- **Sicurezza**: memoria esterna vulnerabile a poisoning persistente [[wiki/sources/xu-2026-contextual-agentic-memory]] [[wiki/sources/iscan-2026-rscb-mc]]
