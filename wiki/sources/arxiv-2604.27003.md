---
type: source
created: 2026-05-25
updated: 2026-05-25
tags: [continual-learning, memory-retrieval, agent-memory, experience-reuse, alfworld]
source_path: raw/papers/arxiv-2604.27003.pdf
---

# When Continual Learning Moves to Memory: Experience Reuse in LLM Agents

**Autori:** Qisheng Hu, Quanyu Long, Wenya Wang (NTU Singapore) | **arXiv:** 2604.27003 | **Aprile 2026**

## Sintesi

Questo lavoro indaga come la memoria esterna negli agent LLM riposiziona il problema del continual learning anziche risolverlo. Invece dell'interferenza nello spazio dei pesi (stability-plasticity dilemma classico), il collo di bottiglia si sposta al livello della memoria: esperienze vecchie e nuove competono per l'accesso al contesto finito durante il retrieval.

## Framework (k, v)

Gli autori introducono un framework a due assi:
- **k (representation):** come l'esperienza viene rappresentata (traiettorie dettagliate vs memorie procedurali astratte)
- **v (organization):** come e organizzata per il retrieval (granularita dell'organizzazione)

## Risultati chiave

- Le memorie procedurali astratte trasferiscono meglio delle traiettorie dettagliate
- Il **negative transfer** colpisce sproporzionatamente i casi difficili
- Organizzazione piu fine-grained non e universalmente benefica: design che producono forte forward transfer possono simultaneamente indurre severo forgetting
- La memoria esterna non risolve il continual learning problem; lo **rimodella** in un problema di rappresentazione e retrieval

## Benchmark

Esperimenti su task sequenziali in **ALFWorld** e **BabyAI**, con protocollo di valutazione A-to-B (apprendimento task A, riutilizzo memoria su task B).

## Collegamenti nel vault

- [[wiki/pages/experience-reuse-continual-learning]] — contributo diretto sul transfer negativo e astrazione procedurale
- [[wiki/pages/memory-architectures-retrieval]] — evidenza che retrieval granularity non e monotona
