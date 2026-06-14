---
type: source
created: 2026-06-14
updated: 2026-06-14
tags: [short-term-memory, tool-calling, mcp, context-management]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Optimizing Short-Term Memory for Dynamic Tool Calling

**Elias Lumer et al.** (PwC), arXiv:2507.21428, Jul 2025.

## Summary

MemTool è un framework di **short-term memory** per agenti LLM che gestiscono dinamicamente tool o server MCP in conversazioni multi-turno. Offre tre architetture agentiche: **Autonomous Agent Mode** (piena autonomia), **Workflow Mode** (controllo deterministico), e **Hybrid Mode** (combinazione dei due). Valutato su 13+ LLM con il benchmark ScaleMCP su 100 interazioni consecutive.

## Key Claims

- I reasoning LLM raggiungono **90-94% di efficienza di rimozione tool** (media a 3 window) in Autonomous Agent Mode [[wiki/sources/lumer-2025-memtool]](raw/papers/arxiv-2507.21428.pdf).
- I modelli di dimensione media mostrano efficienza significativamente inferiore (**0-60%**) nella gestione autonoma dei tool [[wiki/sources/lumer-2025-memtool]](raw/papers/arxiv-2507.21428.pdf).
- Workflow e Hybrid modes gestiscono consistentemente la rimozione dei tool; Autonomous ed Hybrid eccellono nel task completion [[wiki/sources/lumer-2025-memtool]](raw/papers/arxiv-2507.21428.pdf).
