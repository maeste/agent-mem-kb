---
type: page
created: 2026-05-04
updated: 2026-06-22
tags: [compass, reflection]
---

# Bussola

*Ultimo aggiornamento: 2026-06-22*

## Dove sta andando il mio pensiero

La vault è ferma dal 5 maggio, quasi sette settimane senza operazioni. In quel periodo il campo ha continuato a muoversi: le 36 sorgenti che abbiamo coprono memoria agentica (tassonomia, architetture, retrieval, dimenticanza) e agent skills (ecosistema, registry, discovery, lifecycle), ma la letteratura di aprile-maggio 2026 che ho letto oggi mostra che i temi si stanno saldando in modo interessante. La critica di Xu et al. su lookup vs true memory trova riscontro empirico nello studio Hu et al. sul continual learning via memory: l'astrazione delle traiettorie aiuta, ma il negative transfer colpisce i casi difficili. Contemporaneamente, l'ecosistema delle skill sta maturando verso un modello da package manager (Skilldex, SkVM) con problemi reali di sicurezza e portabilità cross-LLM. Il filo conduttore che emerge con più forza rispetto a maggio è la tensione tra *quanto* memorizzare/estrarre e *quale* livello di astrazione serve: troppa granularità fa rumore, poca perde dettagli critici, e non c'è ancora un principio generale per scegliere.

## Cosa non sto guardando

- **La pagina [[wiki/pages/memory-architectures-retrieval]] è ferma al 4 maggio** e non include OCR-Memory (rappresentazione visuale come high-density memory store), ContextWeaver (dependency-graph memory construction), né Memanto (information-theoretic retrieval senza knowledge graph). Tre architetture significative entrate nella vault ma mai sintetizzate.
- **La pagina [[wiki/pages/experience-reuse-continual-learning]] è ferma al 5 maggio** e non ha assorbito i risultati del paper Hu et al. (arxiv-2604.27003) che studia esplicitamente continual learning in memory-augmented agents con evidenze su abstraction shaping, negative transfer su hard cases, e trade-off stabilità-plasticità nel retrieval.
- **Nessuna view è stata costruita**: `wiki/views/` è vuota. Due view erano state proposte in hot.md il 5 maggio (confronto architetture skill library, timeline 2023-2026 evoluzione skills) e restano aperte.
- **La critica Xu et al.** continua a vivere distribuita in citazioni sparse. Merita una pagina dedicata o almeno una sezione strutturata in llm-agent-memory, perché è il punto di riferimento teorico contro cui tutto il resto si misura.
- **Memoria condivisa multi-agente**: confermato gap anche dai nuovi paper. Nessuna delle 36 fonti affronta direttamente il problema della memoria condivisa tra agenti autonomi.
- **FSFM (Gu 2026)** e **When to Forget (Simsek 2026)** sono due lavori complementari sulla dimenticanza selettiva che potrebbero arricchire [[wiki/pages/forgetting-memory-governance]] con prospettive neuro-ispirate (hippocampal indexing, Ebbinghaus curve) e governance operativa (Memory Worth statistic).

## Una domanda che vale la pena sedersi sopra

La vault ha 36 sorgenti e 6 pagine concettuali ben sviluppate, ma l'ultima scrittura risale a sette settimane fa. Il campo sta producendo paper a ritmo sostenuto (solo ad aprile 2026 ci sono oltre 20 paper rilevanti), e la struttura attuale della vault — pagine monografiche per tema + sorgenti nominate per autore — regge finché il volume è gestibile. A quale punto la tassonomia corrente (memory / skills / forgetting / continual-learning / architectures) inizia a frammentarsi invece di organizzare? E vale la pena iniziare a costruire view (timeline, confronti) prima che il numero di sorgenti renda impossibile vederne i pattern?
