---
type: source
created: 2026-07-03
updated: 2026-07-03
tags: [memory, short-term-memory, tool-calling, mcp, multi-turn]
source_path: raw/papers/arxiv-2507.21428.pdf
---

# MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling

**Autori:** Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah et al. (PwC)
**arXiv:** 2507.21428 | Luglio 2025

## Riassunto

MemTool affronta il problema della gestione del contesto in conversazioni multi-turno dove agenti LLM devono richiamare ripetutamente tool o server MCP diversi. Il sistema propone tre architetture agentiche per la gestione dello short-term memory dei tool:

1. **Autonomous Agent Mode**: piena autonomia nella gestione dei tool
2. **Workflow Mode**: controllo deterministico senza autonomia
3. **Hybrid Mode**: combinazione di controllo autonomo e deterministico

Valutato su 13+ LLMs con il benchmark ScaleMCP su 100 interazioni consecutive. I reasoning LLM raggiungono alta efficienza di rimozione tool (90-94% su media 3-window), mentre modelli medi mostrano efficienza significativamente più bassa (0-60%). Workflow e Hybrid modes gestiscono consistentemente la rimozione tool; Autonomous e Hybrid mode eccellono nel task completion.

## Claim chiave

- La gestione dello short-term memory per tool/MCP context è critica per le performance in conversazioni multi-turno [[wiki/sources/arxiv-2507.21428.md]]
- Modelli reasoning mostrano capacità di tool-removal molto superiori ai modelli medium [[wiki/sources/arxiv-2507.21428.md]]
- Non esiste un'architettura ottimale unica: trade-off tra accuratezza, agency e capacità del modello [[wiki/sources/arxiv-2507.21428.md]]

## Collegamenti

- Complementa [[wiki/sources/zhang-2026-lightmem.md]] (LightMem) che gestisce STM/MTM/LTM a livello generale
- Relazionato a [[wiki/pages/memory-systems]]
- MCP-specific, utile per [[wiki/pages/tool-use]]
