---
type: page
created: 2026-05-04
updated: 2026-05-05
tags: [llm-agents, memory, retrieval, context-management, graph-memory, agent-skills]
---

# Architetture di Memoria e Retrieval

## Sistemi multi-agente per la memoria

- **MIRIX**: sei componenti (Core, Episodica, Semantica, Procedurale, Resource, Knowledge Vault) coordinate da un multi-agent framework. SOTA su LOCOMO (85.4%) e ScreenshotVQA, con 99.9% riduzione dello storage vs. RAG baseline [[wiki/sources/wang-2025-mirix]]
- **AMA**: agenti Constructor/Retriever/Judge/Refresher che gestiscono memoria multi-granularità con verifica di consistenza e refresh iterativo. -80% consumo token vs. full-context [[wiki/sources/huang-2026-ama]]
- **Agentic Memory (AgeMem)**: unifica LTM e STM come azioni tool-based nell'policy dell'agente, addestrate con RL progressivo in tre fasi (step-wise GRPO) [[wiki/sources/yu-2026-agemem]]

## Retrieval ottimizzato

- **MemTool**: gestisce contesto di tool/MCP in conversazioni multi-turno con tre modalità (Autonomous, Workflow, Hybrid). LLM reasoning raggiungono 90-94% efficienza di rimozione tool [[wiki/sources/lumer-2025-memtool]]
- **ContextWeaver**: organizza la traccia di interazione in un grafo di step di reasoning con dipendenze, serializzando percorsi radice-foglia per contesto futuro. Migliora pass@1 su SWE-Bench riducendo token [[wiki/sources/wu-2026-contextweaver]]
- **OCR-Memory**: codifica traiettorie storiche come immagini ad alta densità con anchor visivi, recuperando tramite paradigma locate-and-transcribe per evitare allucinazione [[wiki/sources/li-2026-ocr-memory]]
- **Memanto**: 13 categorie di memoria tipizzata con search information-theoretic senza indicizzazione. SOTA su LongMemEval (89.8%) e LoCoMo (87.1%) con singola query di retrieval [[wiki/sources/abtahi-2026-memanto]]
- **LightMem**: usa Small Language Models per retrieval + writing + consolidation offline. +2.5 F1 medio su LoCoMo vs. A-MEM, latenza 83ms retrieval [[wiki/sources/zhang-2026-lightmem]]

## Grafi della conoscenza

La survey di Yang et al. (2026) classifica la memoria basata su grafi secondo il lifecycle: estrazione, storage, retrieval ed evoluzione, coprendo knowledge vs. experience memory e implementazioni strutturate vs. non-strutturate [[wiki/sources/yang-2026-graph-memory]].

## Skill Retrieval Augmentation come paradigma di scaling

SRA formalizza un paradigma distinto da RAG classico: invece di iniettare tutte le skill disponibili nel prompt, le skill vivono in un corpus esterno e vengono recuperate, incorporate ed eseguite on-demand. La differenza è che gli item recuperati sono *capacità eseguibili* che aumentano la competenza funzionale, non conoscenza dichiarativa che ancora la generazione. SRA-Bench (5.400 task, 636 gold skill in un corpus di 26.262) decompone la pipeline in tre stadi (retrieval → incorporation → execution) ed evidenzia che il vero collo di bottiglia non è il retrieval ma l'*incorporation*: gli agenti caricano skill a tassi simili indipendentemente dal fatto che una gold skill sia stata recuperata o che il task la richieda davvero [[wiki/sources/arxiv-2604.24594]].

## Portabilità cross-LLM delle skill

SkVM applica i principi del compiler design alle skill — skill come codice, LLM come processori eterogenei. Su un corpus di 118.000 skill da clawhub.ai e skills.sh, gli autori mostrano che abilitare le skill *degrada* le prestazioni nel 15% dei task (7% per Opus 4.6, 25% per Qwen3-30B), rivelando un mismatch fondamentale tra spec statica e capacità variabile del modello. Il sistema introduce capability-based compilation (26 dimensioni primitive di capacità misurate per modello-harness), JIT code solidification per template ad alta frequenza, e recompilation adattiva quando il gap di capacità emerge in esecuzione: +15.3% di completion rate, fino a -40% di token, 3.2×–50× di speedup [[wiki/sources/arxiv-2604.03088]].
