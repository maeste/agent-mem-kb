---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, retrieval, agents, benchmark, capability-augmentation]
source_path: raw/papers/arxiv-2604.24594.pdf
---

# Skill Retrieval Augmentation for Agentic AI (SRA)

**Autori:** Weihang Su, Jianming Long, Qingyao Ai, Yichen Tang, Changyue Wang, Yiteng Tu, Yiqun Liu (Tsinghua University)
**arXiv:** 2604.24594 (apr 2026) | **Code:** github.com/oneal2000/SR-Agents | **Data:** SRA-Bench su HuggingFace

## Summary

Introduce **Skill Retrieval Augmentation (SRA)**: un nuovo paradigma dove agenti recuperano dinamicamente skill rilevanti da corpora esterni grandi invece di enumerarle in-context. La differenza fondamentale con RAG classico: SRA recupera **capability eseguibili** (non knowledge dichiarativo), e il retrieval deve essere valutato per downstream utility, non solo semantic relevance.

## SRA-Bench

- **5.400** test instances capability-intensive
- **636** gold skills manuali + distrattori web = corpus di **26.262 skills**
- Valutazione decomposta su 3 stage: Skill Retrieval → Skill Incorporation → Skill Application

## Risultati chiave

1. SRA pipeline semplice (retrieval singolo skill + injection) migliora già gli agenti rispetto a skill-free baseline → validazione del paradigma
2. **Bottleneck critico nella Skill Incorporation**: gli agenti tendono a caricare skill a tassi simili indipendentemente che sia gold skill o meno, e indipendentemente che il task richieda o meno capacità esterne. Il problema non è solo retrieval ma la capacità del modello base di decidere *quale* skill caricare e *quando* serve
3. SRA è distinto da RAG: target = capabilities eseguibili vs declarative evidence; evaluation = downstream utility vs semantic relevance

## Relazione con altri lavori

- Complementare a [[wiki/sources/xu-2026-agent-skills-survey]] (survey su agent skills): SRA fornisce paradigma operativo + benchmark
- Converge con [[wiki/sources/li-2026-skillflow]] sul tema di skill retrieval scalabile
- Si collega a [[wiki/sources/xia-2026-skill-rl]] per l'aspetto di selezione/learning delle skill
- Rilevante per [[wiki/sources/ling-2026-agent-skills-analysis]]
