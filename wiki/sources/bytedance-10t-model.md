---
type: source
created: 2026-08-08
updated: 2026-08-08
tags: [model-scaling, bytedance, china-ai, frontier-models, competition]
source_path: raw/web/bytedance-trains-a-10-trillion-parameter-ai-model-aiming-for-global-leadership-k/index.md
ingested: 2026-W31 (Sat-Sat)
---

# ByteDance trains a 10-trillion-parameter AI model

KuCoin/ChainCatcher via Financial Times (Aug 7 2026). Secondary reporting su fonti interne ByteDance.

## Fatti

- ByteDance in fase di **pre-training** di un modello stimato a **~10T parametri**
- Scala ~3x rispetto al più grande modello cinese rilasciato (Kimi K3 di Moonshot AI, 2.8T)
- Pre-training tipicamente 3-6 mesi; poi fine-tuning e release
- Scala finale non ancora definita
- Fonte: tre insider; FT non ha nomi ufficiali

## Contesto competitivo

- Anthropic Mythos 5 stimato ~8T parametri (non confermato da Anthropic)
- Anthropic Fable 5 stimato ~5T parametri
- ByteDance mira al livello Mythos, varco competitivo Cina→US

## Note

Fonte secondaria (news flash via crypto exchange newsfeed, riprende ChainCatcher/FT). Param count è capacity ceiling, non garantisce performance: data quality e training methodology pesano quanto la scala. Da verificare con annuncio ufficiale ByteDance.

## Connessioni

Aggiunge un data point al trend [[wiki/pages/moe-sparsity]]: se confermato, 10T supererebbe ogni modello nella tabella attuale (K3 2.8T, Qwen3.8-Max 2.4T). La domanda aperta è se sarà MoE (parametri attivi bassi) o denso. Il salto 3x sopra K3 suggerisce MoE estremo: nessuno ha risorse per 10T dense in pre-training.
