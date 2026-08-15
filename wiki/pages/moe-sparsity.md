---
type: page
created: 2026-07-23
updated: 2026-08-08
tags: [moe, sparsity, inference, scaling, model-architecture, concept]
---

# MoE Sparsity

La tendenza architetturale dominante nei modelli aperti: aumentare i parametri totali mentre si mantengono i parametri attivi per token approssimativamente costanti. Il costo si sposta dalla generazione (compute) allo storage.

## I numeri

Dati da Bajwa ([[wiki/sources/akash-bajwa-sparse-by-design]]):

| Modello | Param totali | Attivi/token | % attiva |
|---------|-------------|-------------|----------|
| Mixtral | ~46B | ~13B | ~28% |
| Kimi K2/K2.5/K2.6 | 1T | 32B | ~3% |
| Kimi K3 | 2.8T | 16B | <2% |
| Inkling-Small | 276B | 12B | ~4.4% |
| Qwen3.8-Max | 2.4T | 95B | ~4% |
| GLM-5.2 | meno sparse di V4-Pro | - | - |

Inkling-Small ([[wiki/sources/thinking-machines-inkling-small]], Thinking Machines Lab, Jul 2026) si colloca nel range 2-5%: meno estremo di K3 ma più efficiente di Mixtral. Raggiunge prestazioni comparabili al modello maggiore Inkling (41B/975B, ~4.2% attivi) a un quarto della dimensione, con reasoning effort controllabile come grado di libertà.

Moonshot ha rilasciato K2, K2.5, K2.6 in 9 mesi con identico scheletro (1T/32B): **zero crescita nei parametri attivi**.

## Perché funziona

A budget di compute fisso, più expert significa loss minore. La fattura si paga in storage (economico, a livelli) anziché in compute e bandwidth (scarsi). Sparsity è anche adattamento: quando i FLOPs sono razionati (export control), si scala l'asse non controllato.

## Compressione KV Cache

La sparsity degli expert riduce i weight-byte per token. La compressione attention (DeepSeek CSA/HCA, MLA, K3 attention) riduce i cache-byte per token. V4-Pro a 1M context ha KV cache al **10%** del predecessore. Ma i byte **stored** non diminuiscono mai.

## Due regimi di serving

**Low batch** (enterprise self-hosting): expert genuinely cold, tiering HBM→DRAM funziona. La sparsity è l'unica ragione per cui self-hosting di modelli trillion-scale è possibile.

**High batch** (hyperscale): l'intero batch accende quasi tutti gli 896 expert ogni forward pass. Nessun expert è affidabilmente cold. La sparsity non riduce l'HBM comprato, converte bandwidth demand in capacity demand.

## Bottleneck: routing

I router attuali distribuiscono i token uniformemente, sconfiggendo il tiering hot/cold a scale. Routing con locality deliberata potrebbe rendere il tiering viable anche ad alto batch.

## Alternativa: Looped Transformer (sparsity temporale)

Nanbeige4.2-3B ([[wiki/sources/kaitchup-agentic-two-scales]]) usa 22 layer fisici eseguiti due volte (stessi pesi): profondità computazionale ~44 layer senza almacenare 44 layer indipendenti. Invece di sparsity spaziale (expert routing), è **sparsity temporale**: stessa compute ripetuta sullo stesso set di pesi. Riduce weight memory ma non inference compute. KV-cache alta (~176 KiB/token, 8 KV heads). L'agentic capability a 3B dense dimostra che l'architettura conta più della scala assoluta.

Laguna S 2.1 (118B/8B MoE, 256 expert top-10 + 1 shared) per coding long-horizon: conferma il trend MoE ma con feedback community mixed sui benchmark (pool harness non open, presunto hidden advisor feature).

## DeepSeek V4 Flash

V4-Flash a $0.14/$0.28 per 1M token (cache miss/hit $0.0028), context 1M, max output 384K ([[wiki/sources/deepseek-v4-flash-api]]). Posizionamento ultra-competitivo per workload agentic. V4-Pro mantiene compressione KV cache (~10% predecessore a 1M context).

## Qwen3.8-Max: sparsity con parametri attivi alti

Qwen3.8-Max ([[wiki/sources/qwen3-8-max]], ago 2026) porta i parametri totali a **2.4T con 95B attivi** (~4%). La percentuale è simile a Inkling-Small, ma la scala dei parametri attivi è senza precedenti nella tabella: 95B vs 16B (K3) o 32B (K2.6). Il modello non massimizza la sparsity relativa, sceglie **più expert attivi contemporaneamente** su base parametrica più larga. Hint architetturale: la capability long-horizon (16 giorni autonomi, 500 turni RTL) potrebbe richiedere più expert concurrently attivi. Annunciati open weights (primo Max-class della serie).

## ByteDance 10T: la frontiera in pre-training

ByteDance ([[wiki/sources/bytedance-10t-model]], ago 2026, FT via 3 insider) è in fase di pre-training di un modello stimato a **~10T parametri**, ~3x sopra Kimi K3 (2.8T, il più grande modello cinese rilasciato). La scala finale non è ancora fissata; pre-training tipicamente 3-6 mesi. Per contesto: Anthropic Mythos 5 stimato ~8T, Fable 5 ~5T (non confermati da Anthropic). Se confermato MoE, supererebbe ogni voce della tabella. Nessuno ha risorse per 10T dense in pre-training: il salto suggerisce MoE estremo con parametri attivi probabilmente bassi. Fonte secondaria, da verificare con annuncio ufficiale.
