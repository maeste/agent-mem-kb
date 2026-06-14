---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [agent-skills, skill-retrieval, information-retrieval, coding-agents]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable and Efficient Agent Skill Retrieval System

**Fangzhou Li et al.** (UC Davis), arXiv:2504.06188, Mar 2026.

## Summary

SkillFlow è il primo pipeline multi-stadio di **retrieval** progettato per la scoperta di agent skills, che inquadra l'acquisizione di skills come un problema di information retrieval su un corpus di ~36K definizioni SKILL.md indicizzate da GitHub. Il pipeline restringe progressivamente il set di candidati attraverso quattro stadi: dense retrieval (1K candidati), shallow cross-encoder reranking (100), deep cross-encoder reranking (10), e LLM-based selection (≤5 skills).

## Key Claims

- Su SkillsBench (87 task, 229 skills matchate), le skills recuperate da SkillFlow alzano Pass@1 dal **9.2% al 16.4%** (+78.3%), raggiungendo l'84.1% del ceiling oracle [[wiki/sources/li-2026-skillflow]](raw/papers/arxiv-2504.06188.pdf).
- Su Terminal-Bench (89 task, nessuna skill matchata), gli agenti usano le skills recuperate con un tasso del **70.1%** ma non mostrano miglioramento di performance, rivelando che retrieval da sola non basta quando il corpus manca di skills eseguibili di alta qualità [[wiki/sources/li-2026-skillflow]](raw/papers/arxiv-2504.06188.pdf).
- La qualità e coverage del corpus sono fattori più critici della precisione del retriever per l'impatto pratico di skill-augmented agents [[wiki/sources/li-2026-skillflow]](raw/papers/arxiv-2504.06188.pdf).
