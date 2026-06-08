---
type: source
created: 2026-06-08
updated: 2026-06-08
tags: [short-term-memory, tool-calling, mcp, context-management]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Optimizing Short-Term Memory for Dynamic Tool Calling

**Elias Lumer et al.** (PwC) — arXiv:2507.21428, Jul 2025

## Summary

MemTool è un framework di memoria a breve termine che permette agli agenti LLM di gestire dinamicamente il contesto di tools o MCP server attraverso conversazioni multi-turn. Il problema affrontato: agenti possono scoprire e aggiungere centinaia di nuovi tools al loro contesto window, ma devono rimuoverli quando non più necessari per non saturare il contesto.

Tre architetture agentiche proposte:
1. **Autonomous Agent Mode**: piena autonomia nella gestione dei tool
2. **Workflow Mode**: controllo deterministico senza autonomia
3. **Hybrid Mode**: combinazione di autonomia e controllo deterministico

Valutato su ScaleMCP benchmark con 13+ LLMs su 100 interazioni consecutive. Risultati: reasoning LLMs raggiungono 90-94% tool-removal efficiency (media 3-window), mentre modelli medi mostrano 0-60%. Workflow e Hybrid mode gestiscono efficacemente la rimozione; Autonomous ed Hybrid eccellono nel task completion.

## Key claims
- La gestione della STM per tools è un problema distinto dalla compressione conversazionale ([§1](raw/papers/arxiv-2507.21428.pdf))
- Esistono trade-off chiari tra task accuracy, agency e capacità del modello ([§4](raw/papers/arxiv-2507.21428.pdf))
- I modelli reasoning sono significativamente migliori nella gestione autonoma dei tool ([§4](raw/papers/arxiv-2507.21428.pdf))

## Connections
- [[wiki/sources/lumer-2025-memtool]] — fonte primaria
- [[wiki/pages/short-term-memory]] — gestione STM in agenti
