---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [skill-retrieval, information-retrieval, agent-skills, benchmark]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable Agent Skill Retrieval System

**Autori:** Li, Tagkopoulos, Tagkopoulos (UC Davis) | **arXiv:** 2504.06188 | **Mar 2026**

## Summary

SkillFlow è il primo pipeline multi-stadio per il retrieval di skill agent, formulato come problema di information retrieval su un corpus di ~36K definizioni SKILL.md indicizzate da GitHub. Il pipeline restringe progressivamente i candidati attraverso quattro stage: dense retrieval, due round di cross-encoder reranking, e selezione LLM-based.

Valutato su due benchmark:
- **SkillsBench**: 87 task, 229 skill matchate. SkillFlow alza Pass@1 dal 9.2% al 16.4% (+78.3%), raggiungendo 84.1% del ceiling oracle.
- **Terminal-Bench**: 89 task senza skill matchate. Gli agenti usano le skill recuperate (70.1% use rate) ma nessun guadagno di performance, rivelando che il retrieval da solo non basta quando il corpus manca di skill eseguibili di qualità.

## Key claims

- L'acquisizione di skill come task di IR è efficace, ma l'impatto pratico dipende dalla copertura del corpus e dalla qualità delle skill [[wiki/pages/skillflow]]
- La densità di codice runnable e artifact bundlettati è predittiva dell'utilità delle skill recuperate
- Il reranking a più stadi bilancia recall e precisione meglio del retrieval singolo
