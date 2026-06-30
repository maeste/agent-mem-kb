---
type: source
created: 2026-06-30
updated: 2026-06-30
tags: [memory, SLM, lightweight, agents, multi-tier-memory]
source_path: raw/papers/arxiv-2604.07798.pdf
---

# LightMem: Lightweight LLM Agent Memory with Small Language Models

**Zhang et al. (2026)** — UESTC / Kyung Hee University / CityU HK / Oxford

## Summary

LightMem è un sistema di memoria **lightweight per agenti LLM guidato da Small Language Models (SLM)**. Il problema identificato: i sistemi retrieval-based hanno overhead online basso ma accuracy instabile; i sistemi che usano chiamate ripetute a modelli grandi accumulano latenza su interazioni lunghe.

L'idea chiave: separare il processing **online** (leggero, controllabile) dalla **consolidazione offline** (pesante). Gli SLM rendono questa separazione pratica.

## Architettura a 3 tier

- **STM** (Short-Term Memory): contesto conversazionale immediato
- **MTM** (Mid-Term Memory): summary di interazioni riutilizzabili
- **LTM** (Long-Term Memory): conoscenza consolidata

User identifiers supportano retrieval indipendente e manutenzione incrementale in setting multi-user.

## Retrieval

Due stage sotto budget fisso: vector-based coarse retrieval + semantic consistency re-ranking. Offline: astrazione di evidenze di interazione riutilizzabili e integrazione incrementale in LTM.

## Risultati

- F1 improvement medio ~2.5 su A-MEM (LoCoMo)
- Retrieval latency mediana: **83 ms**
- End-to-end latency: **581 ms**
- Guadagni consistenti across model scales

## Claim chiave

- La separazione online/offline con SLM per decisioni memoria ad alta frequenza è superiore sia al retrieval puro che alle chiamate LLM ripetute [[wiki/sources/arxiv-2604.07798]]
