---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [agents, harnesses, evaluation, test-time-scaling, benchmarking]
source_path: raw/papers/arxiv-2607.12227.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Rethinking the Evaluation of Harness Evolution for Agents

**Yike Wang et al.** (AI2, UW, Independent) — arXiv:2607.12227, 14 lug 2026 [[raw/papers/arxiv-2607.12227.pdf]]

Critica del protocollo di valutazione per automatic harness evolution: i reported gains potrebbero derivare da search budget extra而非 reali miglioramenti di design.

## Problemi identificati

1. **Missing baseline comparison**: harness evolution e una procedura di search iterativa; dovrebbe essere confrontata con **test-time scaling baselines** (parallel sampling, sequential refinement) under matched feedback e inference budgets [[raw/papers/arxiv-2607.12227.pdf]]
2. **Data leakage/overfitting**: search e final evaluation condividono lo stesso benchmark; i gains possono riflettere overfitting al task set, non transferabili improvements

## Metodologia

Confronto su Terminal-Bench 2.1 con GPT-5.4 e Claude Opus 4.6:
- **Parallel sampling**: fixed harness, explore in width
- **Sequential refinement**: fixed harness, explore in depth
- **Harness evolution**: modifica il harness stesso
- Valutazione anche su **held-out tasks** per testare generalizzazione

## Risultati principali

- Harness evolution **non consistently outperforms** simple test-time scaling baselines
- Senza unit test feedback, harness evolution **underperforms** parallel sampling e sequential refinement in media (Fig. 1: ~67-68% vs ~71-72% per Opus 4.6/GPT-5.4)
- Limitata generalizzazione su held-out tasks
- Conclusion: i reported gains negli harness evolution papers potrebbero essere largely attribuibili a **additional search compute**, non a superior harness design

## Implicazione

Serve un protocollo di valutazione che: (1) separi optimization feedback da final measurement, (2) confronti contro test-time scaling baselines, (3) evalui su held-out sets.
