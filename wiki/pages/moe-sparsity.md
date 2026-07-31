---
type: page
created: 2026-07-23
updated: 2026-07-31
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
