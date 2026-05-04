---
type: source
created: 2026-05-04
updated: 2026-05-04
tags: [llm-agents, memory, short-term, tool-calling, context-management]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling

**Autori:** Elias Lumer et al. (PricewaterhouseCoopers)
**Data:** 2025-07-29

## Summary

MemTool affronta la gestione della memoria a breve termine per agenti LLM che usano dinamicamente strumenti e server MCP in conversazioni multi-turno. Offre tre architetture: Autonomous Agent Mode (autonomia totale), Workflow Mode (controllo deterministico), e Hybrid Mode.

Testato su 13+ LLM con il benchmark ScaleMCP su 100 interazioni consecutive. I modelli di reasoning raggiungono 90-94% efficienza di rimozione tool (media su 3 finestre), mentre i modelli medium mostrano efficienza significativamente inferiore (0-60%). Workflow e Hybrid modes gestiscono efficacemente la rimozione; Autonomous e Hybrid eccellono nel completamento dei task.

[[wiki/pages/memory-architectures-retrieval]]
