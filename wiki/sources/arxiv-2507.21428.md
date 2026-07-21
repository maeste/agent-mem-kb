---
type: source
created: 2026-07-21
updated: 2026-07-21
tags: [short-term-memory, tool-calling, mcp, context-management]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Short-Term Memory for Dynamic Tool Calling

**Autori:** Lumer et al. (PwC) | **arXiv:** 2507.21428 | **Lug 2025**

## Summary

MemTool è un framework per la gestione della memoria a breve termine in agenti LLM che usano dynamic tool calling (MCP server) in conversazioni multi-turno. Il problema: finestre di contesto fisse limitano l'efficacia quando lo stesso agente deve riutilizzare tool indipendentemente attraverso turni multipli.

Tre architetture agentic:
1. **Autonomous Agent Mode**: piena autonomia nella gestione dei tool
2. **Workflow Mode**: controllo deterministico senza autonomia
3. **Hybrid Mode**: combinazione di autonomia e controllo deterministico

Valutato su 13+ LLM con il benchmark ScaleMCP (100 interazioni consecutive).

## Key claims

- I reasoning LLM raggiungono 90-94% tool removal efficiency (media 3-window) in Autonomous Mode [[wiki/pages/memtool]]
- I modelli medium-sized mostrano efficienza significativamente inferiore (0-60%)
- Workflow e Hybrid modes gestiscono il tool removal consistentemente; Autonomous e Hybrid eccellono nel task completion
- Trade-off chiaro tra accuratezza del task, agency e capacità del modello
