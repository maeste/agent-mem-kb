---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [skill-retrieval, information-retrieval, agents, benchmark]
source_path: raw/papers/arxiv-2504.06188.pdf
---

# SkillFlow: Scalable and Efficient Agent Skill Retrieval System

**Autori:** Fangzhou Li, Pagkratidis Tagkopoulos, Ilias Tagkopoulos (UC Davis)
**arXiv:** 2504.06188 | Marzo 2026

## Riassunto

SkillFlow affronta il problema del reperimento selettivo di skills da repository di grandi dimensioni per agenti LLM. Il sistema tratta l'acquisizione di skills come un problema di information retrieval su un corpus di ~36K definizioni SKILL.md indicizzate da GitHub.

La pipeline ha quattro stadi progressivi:
1. **Dense retrieval**: restringe il set candidato iniziale
2. **Cross-encoder reranking (round 1)**: primo raffinamento
3. **Cross-encoder reranking (round 2)**: secondo passaggio di precisione
4. **LLM-based selection**: selezione finale guidata da modello

Valutato su due benchmark: SkillsBench (87 task, 229 skills) e Terminal-Bench (89 task, nessuna skill matching). Su SkillsBench, SkillFlow migliora Pass@1 dal 9.2% al 16.4% (+78.3%), raggiungendo il 84.1% dell'oracle ceiling. Su Terminal-Bench, il tasso di utilizzo delle skills recuperate è 70.1% ma senza guadagno di performance, rivelando che la retrieval da sola non basta se il corpus manca di skills eseguibili di qualità per il dominio target.

## Claim chiave

- Il reperimento di skill a più stadi bilancia recall e precisione meglio di approcci single-stage [[wiki/sources/arxiv-2504.06188.md]]
- L'impatto pratico di skill-augmented agents dipende dalla copertura del corpus e dalla qualità delle skills [[wiki/sources/arxiv-2504.06188.md]]
- Un corpus ampio senza skills domain-specific eseguibili limita il beneficio della retrieval [[wiki/sources/arxiv-2504.06188.md]]

## Collegamenti

- Implementa idee discusse in [[wiki/sources/xu-2026-agent-skills-survey.md]] (survey su agent skills)
- Relazionato a [[wiki/pages/skill-management]]
- Benchmark complementare a [[wiki/sources/ling-2026-agent-skills-analysis.md]] (analisi data-driven di skills)
