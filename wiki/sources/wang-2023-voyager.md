---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [agents, embodied-ai, minecraft, skill-library, lifelong-learning, llm]
source_path: raw/papers/arxiv-2305.16291.pdf
---

# Voyager: An Open-Ended Embodied Agent with LLMs

**Guanzhi Wang et al.** (NVIDIA, Caltech, UT Austin, Stanford), arXiv:2305.16291, Oct 2023.

## Summary

Voyager è il primo agente LLM-powered con apprendimento lifelong in Minecraft, capace di esplorare continuamente il mondo, acquisire skills diverse e fare scoperte senza intervento umano. L'architettura si compone di tre componenti chiave:

1. **Automatic Curriculum**: massimizza l'esplorazione proponendo automaticamente nuovi obiettivi adattivi basati sullo stato corrente dell'agente e sulle capacità già acquisite.
2. **Skill Library**: un repository in crescita di codice eseguibile che memorizza e recupera comportamenti complessi come funzioni riutilizzabili.
3. **Iterative Prompting Mechanism**: incorpora feedback dall'ambiente, errori di esecuzione e auto-verifica per migliorare iterativamente i programmi generati.

Voyager interagisce con GPT-4 tramite query blackbox, bypassando la necessità di fine-tuning. Le skills sviluppate sono temporalmente estese, interpretabili e componibili, permettendo una rapida composizione delle capacità dell'agente e mitigando il catastrophic forgetting.

## Key Claims

- Voyager ottiene **3.3x più item unici**, percorre **2.3x distanze più lunghe** e sblocca milestone tech-tree fino a **15.3x più velocemente** rispetto allo SOTA precedente [[wiki/sources/wang-2023-voyager]](raw/papers/arxiv-2305.16291.pdf).
- Le skills acquisite possono essere riutilizzate in un nuovo mondo Minecraft per risolvere task novel da zero, mentre altre tecniche faticano a generalizzare [[wiki/sources/wang-2023-voyager]](raw/papers/arxiv-2305.16291.pdf).
- L'approccio dimostra che le LLM possono essere usate come motori di ragionamento per agenti embodied senza training dedicato sull'ambiente specifico [[wiki/sources/wang-2023-voyager]](raw/papers/arxiv-2305.16291.pdf).

## Significato per la ricerca su agentic memory

Voyager rappresenta uno dei primi esempi di **skill library** come forma di memoria procedurale per agenti LLM. Il concetto di memorizzare comportamenti come codice eseguibile piuttosto che come testo ha influenzato successivamente sistemi come MemTool, SkillFlow e altri approcci di agent skills.
