---
type: source
created: 2026-05-05
updated: 2026-06-13
tags: [skills, retrieval, agents, benchmark, augmentation]
source_path: raw/papers/arxiv-2604.24594.pdf
---

# Skill Retrieval Augmentation (SRA) for Agentic AI

**Su, Long, Ai, Tang, Wang, Tu & Liu** (Tsinghua University) — arXiv:2604.24594, Apr 2026

## Summary

Introduce **Skill Retrieval Augmentation (SRA)**, un nuovo paradigma in cui agenti dynamicamente recuperano e applicano skills da corpora esterni su demanda, invece di enumerarle esplicitamente nel context window. Costruisce **SRA-Bench**, il primo benchmark per valutazione decomposta del pipeline SRA.

## Key claims

- **Enumerazione in-context non scala**: quando i corpora di skill crescono, i context budget si consumano rapidamente e l'agent perde accuratezza nell'identificare la skill giusta.
- **SRA-Bench**: 5.400 test instances capability-intensive, 636 gold skills manuali + 26.262 skill totali (con distrattori web-collected). Valuta retrieval, incorporation ed end-task execution separatamente.
- **Retrieval-based skill augmentation migliora sostanzialmente** le performance dell'agente.
- **Bottleneck nell'incorporation**: gli attuali LLM agent tendono a caricare skill a tassi simili indipendentemente dal fatto che una gold skill sia stata recuperata o che il task richieda effettivamente capacità esterne.
- **Il gap non è solo nel retrieval**: il modello base deve determinare *quale* skill caricare e *quando* il loading esterno è necessario.

## Positioning

Primo benchmark strutturato per il problema del skill retrieval negli agenti. Rileva un gap fondamentale tra "trovare la skill giusta" e "usarla al momento giusto".
