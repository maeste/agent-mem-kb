---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [skill-retrieval, information-retrieval, skill-library, coding-agents]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable and Efficient Agent Skill Retrieval System

**Fangzhou Li, Pagkratopoulos Tagkopoulos, Ilias Tagkopoulos** (UC Davis) — arXiv:2504.06188, Mar 2026

## Summary

SkillFlow è la prima pipeline multi-stadio per il retrieval di skills da agent LLM, formulando l'acquisizione di skills come problema di information retrieval su un corpus di ~36K definizioni SKILL.md indicizzate da GitHub. La pipeline restringe progressivamente il set di candidati attraverso quattro stadi:

1. **Dense retrieval** (bi-encoder): ~1000 candidati
2. **Shallow cross-encoder reranking**: ~100 candidati
3. **Deep cross-encoder reranking**: ~10 candidati
4. **LLM-based selection**: ≤5 skills finali

Valutato su due benchmark: SkillsBench (87 task, 229 skills matchate) e Terminal-Bench (89 task, nessuna skill matchata). Su SkillsBench, le skills recuperate da SkillFlow alzano Pass@1 dal 9.2% al 16.4% (+78.3%), raggiungendo l'84.1% del ceiling oracle. Su Terminal-Bench, gli agenti usano le skills recuperate (70.1% use rate) ma senza guadagno di performance, rivelando che il retrieval da solo non basta quando il corpus manca di skills eseguibili di qualità.

## Key claims
- Il framing dell'acquisizione di skills come IR problem è efficace ([§Abstract](raw/papers/arxiv-2504.06188.pdf))
- L'impatto pratico degli skill-augmented agents dipende dalla copertura del corpus e dalla qualità delle skills ([§5](raw/papers/arxiv-2504.06188.pdf))
- La pipeline a 4 stadi bilancia recall e precisione ad ogni livello ([§3](raw/papers/arxiv-2504.06188.pdf))

## Connections
- [[wiki/pages/skill-retrieval]] — pipeline di retrieval per skills
- [[wiki/sources/li-2026-skillflow]] — fonte primaria
