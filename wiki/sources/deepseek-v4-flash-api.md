---
type: source
created: 2026-08-01
updated: 2026-08-01
tags: [deepseek, api, pricing, model-release, v4-flash, v4-pro]
source_path: (web — Reddit post blocked, data from official docs api-docs.deepseek.com)
ingested: 2026-W30 (Sat-Sat)
---

# DeepSeek V4 Flash — Official API Live

DeepSeek V4 Flash API ufficialmente live. Dati recuperati dai docs ufficiali (Reddit post originale bloccato da CAPTCHA/block).

## Modelli disponibili

| Modello | Versione | Context | Max Output | Thinking |
|---------|----------|---------|------------|----------|
| deepseek-v4-flash | V4-Flash-0731 | 1M | 384K | thinking (default) + non-thinking |
| deepseek-v4-pro | DeepSeek-V4-Pro | - | - | thinking + non-thinking |

Entrambi supportano: JSON output, tool calls, Anthropic API format, chat prefix completion, FIM completion (non-thinking only). V4-Flash supporta anche Responses API.

## Prezzi (per 1M token)

| | V4-Flash | V4-Pro |
|---|----------|--------|
| Input (cache hit) | $0.0028 | $0.003625 |
| Input (cache miss) | $0.14 | $0.435 |
| Output | $0.28 | $0.87 |

Policy peak/off-peak in arrivo: 2x nelle ore peak (9-12, 14-18 Beijing Time).

## Concurrency

V4-Flash: 2500, V4-Pro: 500.

## Rilevanza per il vault

V4-Flash a $0.14/$0.28 per 1M token (cache miss) è estremamente competitivo, sotto quasi tutti i modelli occidentali equivalenti. Context 1M + output 384K lo posiziona per workload agentic long-horizon. Si confronta diretto con GPT-5.6 Luna ([[wiki/sources/openai-gpt-5-6-pricing]]) che è scesa del 80% ma rimane superiore di prezzo. Vedi anche [[wiki/pages/moe-sparsity]]: DeepSeek V4-Pro ha MLA/CSA per compressione KV cache (~10% del predecessore a 1M context).
