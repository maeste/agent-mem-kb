---
type: source
created: 2026-06-11
updated: 2026-06-11
tags: [skills, retrieval, agents, llm, information-retrieval]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable and Efficient Agent Skill Retrieval System

Li, Tagkopoulos, Tagkopoulos (UC Davis), March 2026.

SkillFlow è il primo pipeline multi-stadio per il reperimento di skill agent, formulato come problema di information retrieval su un corpus di ~36K definizioni SKILL.md da GitHub. Il pipeline restringe progressivamente i candidati in quattro stadi: dense retrieval (1K candidati), shallow cross-encoder reranking (100), deep cross-encoder reranking (10), e LLM-based selection (≤5 skill). Valutato su SkillsBench (87 task, 229 skill matchate) e Terminal-Bench (89 task, nessuna skill matchata). Su SkillsBench: Pass@1 sale dal 9.2% al 16.4% (+78.3%), raggiungendo l'84.1% del ceiling oracle. Su Terminal-Bench: gli agenti usano le skill recuperate (70.1% use rate) ma senza guadagno di performance, rivelando che la qualità del corpus (non il retrieval) è il collo di bottiglia principale. Le skill oracle contengono significativamente più codice eseguibile e sono 3x più probabili includere script runnable rispetto alle skill community.
