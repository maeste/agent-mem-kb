---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [llm-agents, skills, skill-retrieval, information-retrieval, reranking, skill-library]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable and Efficient Agent Skill Retrieval System

Fangzhou Li, Pagkratios Tagkopoulos, Ilias Tagkopoulos (UC Davis), arXiv:2504.06188, 2026.

## Summary

SkillFlow è la prima pipeline multi-stage di retrieval progettata specificamente per il discovery di agent skill. Inquadrando l'acquisizione di skill come problema di information retrieval su un corpus di ~36K definizioni SKILL.md indicizzate da GitHub, il sistema restringe progressivamente i candidati attraverso quattro stage: (1) dense retrieval bi-encoder (da 36K a ~1K), (2) shallow cross-encoder reranking (~100), (3) deep cross-encoder reranking (~10), (4) selezione via LLM (≤5 skill). Su SkillsBench (87 task, 229 skill oracle), le skill recuperate migliorano Pass@1 da 9.2% a 16.4% (+78.3%), raggiungendo l'84.1% del tetto oracle. Su Terminal-Bench, l'agente usa le skill recuperate nel 70.1% dei casi ma senza miglioramento di performance, dimostrando che retrieval alone non basta se il corpus manca di skill eseguibili per il dominio target.

## Key claims

- Il retrieval di skill è formalizzabile come problema IR standard con pipeline multi-stage che bilancia recall e precisione [[wiki/pages/skill-extraction-from-memory]]
- Il collo di bottiglia per gli skill-augmented agent non è il retrieval ma la qualità e copertura della skill library: le skill oracle contengono significativamente più codice eseguibile e sono 3× più probabili di includere script runnable
- Un corpus di 36K skill dalla community può essere indicizzato e interrogato efficacemente con latenza praticabile per workflow agentici interattivi
