---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [multimodal-memory, visual-retrieval, optical-context, long-horizon-agents, token-efficiency]
source_path: raw/papers/arxiv-2604.26622.pdf
---

# OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

**Autori:** Jinze Li, Yang Zhang, Xin Yang, Jiayi Qu, Jinfeng Xu, Shuo Yang, Junhua Ding, Edith Ngai (HKU, UNT, Tsukuba, Yonsei)  
**Data:** Aprile 2026 | arXiv:2604.26622

## Sintesi

OCR-Memory propone di usare la **modalita' visiva** come rappresentazione ad alta densita' dell'esperienza agentica, superando il trade-off tra capacita' di memoria e budget token testuale.

### Il problema

I sistemi di memoria agentica sono vincolati dai budget di contesto testuale:
- Memorizzare o rivisitare raw trajectories e' proibitivo in termini di token
- Summarization e retrieval text-only risparmiano token ma perdono informazione e frammentano l'evidenza

### Soluzione: Optical Context Retrieval

1. **Encoding:** le trajectory storiche vengono renderizzate come immagini annotate con identificatori visivi unici (bounding boxes indicizzati)
2. **Retrieval via locate-and-transcribe:** seleziona regioni rilevanti tramite anchor visivi e trascrive il testo corrispondente letteralmente, evitando free-form generation e riducendo l'allucinazione
3. **Vantaggio chiave:** la rappresentazione visiva consuma sostanzialmente meno token del testo originale mantenendo la fedelta' completa dell'informazione

### Risultati

- Gains consistenti su benchmark long-horizon agent con strict context limits
- L'encoding ottico aumenta la capacita' di memoria effettiva preservando il recovery fedele dell'evidenza

## Claim chiave

- La modalita' visiva e' un mezzo superiore al testo per rappresentare esperienze agentiche a lunga scadenza [[wiki/pages/memory-fundamentals]]
- Il paradigma locate-and-transcribe riduce l'allucinazione rispetto alla generazione free-form da immagini
- Questo approccio apre una direzione per **multimodal embodied memory** citata come open challenge da Du et al. 2026

## Posizione nel vault

Contributo innovativo che esplora una dimensione (multimodale) della memoria agentica poco esplorata. Rappresenta una possibile risposta alla sfida "multimodal embodied memory" nei survey.
