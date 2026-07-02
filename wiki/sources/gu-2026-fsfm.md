---
type: source
created: 2026-07-02
updated: 2026-07-02
tags: [selective-forgetting, neuro-inspired-memory, hippocampal-theory, ebbinghaus-curve, memory-security, privacy]
source_path: raw/papers/arxiv-2604.20300.pdf
---

# FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

**Autori:** Yingjie Gu, Wenjian Xiong, Liqiang Wang, Pengcheng Ren, Chao Li, Xiaojing Zhang, Yijuan Guo, Qi Sun, Jingyao Ma, Shidang Shi (China Mobile)  
**Data:** Aprile 2026 | arXiv:2604.20300

## Sintesi

FSFM introduce un framework **neuro-ispirato** per il selective forgetting negli agent LLM, argumento che in ambienti resource-constrained un meccanismo di forgetting ben progettato e' cruciale quanto la retention.

### Motivazione (quattro problemi della retention illimitata)

1. **Resource constraints:** memoria che cresce indefinitamente = storage + computational overhead esponenziale
2. **Decline di memory quality:** contenuti ridondanti (saluti, domande ripetute) occupano spazio e degradano retrieval quality
3. **Information obsolescence:** preferenze utente e fatti diventano obsoleti; memorie stale possono essere controproducenti
4. **Security vulnerabilities:** retention indiscriminata crea superficie di attacco per memory poisoning

### Taxonomy dei meccanismi di forgetting

1. **Passive decay-based:** decadimento temporale (ispirato alla curva di dimenticanza di Ebbinghaus)
2. **Active deletion-based:** rimozione esplicita basata su criteri
3. **Safety-triggered:** forget attivato da segnali di sicurezza
4. **Adaptive reinforcement-based:** apprendimento di cosa dimenticare via RL

### Fondamenti teorici

- **Hippocampal memory indexing/consolidation theory:** l'ippocampo indicizza le memorie nuove; la consolidazione durante il "sonno" trasferisce rappresentazioni stabili alla neocorteccia
- **Ebbinghaus forgetting curve:** il tasso di dimenticanza segue una curva prevedibile che puo' essere sfruttata per pruning intelligente

### Risultati

- Access efficiency: **+8.49%**
- Content quality: **+29.2% signal-to-noise ratio**
- Security: **100% elimination** di security risks identificati

## Claim chiave

- Il selective forgetting e' una capability fondamentale, non un'ottimizzazione [[wiki/sources/simsek-2026-when-to-forget.md]]
- I quattro problemi della retention illimitata sono empiricamente dimostrabili e quantificabili
- L'ispirazione biologica (ippocampo + Ebbinghaus) fornisce principi progettuali concreti, non solo analogie

## Posizione nel vault

Paper piu' completo sul tema del forgetting nella memoria agentica. Complementa Simsek 2026 (Memory Worth come primitiva di governance) con un framework architetturale completo.
