---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [coding-agents, failure-analysis, terminal-bench, empirical-study, reliability]
source_path: raw/papers/arxiv-2607.09510.pdf
ingested: 2026-W30 (Sat-Sat)
---

# Failure as a Process: An Anatomy of CLI Coding Agent Trajectories

**Xiangxin Zhao et al.** (UCL, Nanjing Univ) — arXiv:2607.09510, 10 lug 2026 [[raw/papers/arxiv-2607.09510.pdf]]

Primo large-scale empirical study di failure trajectories per coding agent in ambienti terminal-based, analizzando il failure come processo temporale (onset, evolution, recovery).

## Dataset

- **3,843 execution trajectories** da 7 frontier models x 3 scaffolds (OpenHands, MiniSWE, Terminus2) su Terminal-Bench
- Filtrate a **1,794 valide** (1,184 failed + 610 successful), **63k+ execution steps** annotate manualmente
- Dataset pubblico: https://github.com/xz-Sean/cli_trajectory_analysis

## 14 findings across 4 research questions

### RQ1: Occurrence — Quando l'error diventa unrecoverable?
- Le failures sono predominantemente driven da **epistemic errors** (non slip/execution errors)
- Tipicamente iniziano nei **primi pochi execution steps**
- Spesso rimangono **hidden** finche recovery non e piu possibile
- Implicazione: serve validazione e intervento precoce, non solo final-outcome evaluation

### RQ2: Root Cause
- Errori epistemici dominano: ragionamento errato, conoscenza mancante, evidenze mal interpretate
- Gli agenti spesso non riconoscano i propri errori (silent failure propagation)

### RQ3: Recovery
- Alcuni agenti recover da decisive errors; altri restano intrappolati in repair attempts infruttuosi
- Pattern di recovery correlano con capacità del modello e design dello scaffold

### RQ4: Cross-system consistency
- Alcuni pattern di failure sono consistenti across modelli e scaffolds (suggesting systemic issues)
- Altri variano significativamente (suggesting model/scaffold-specific behaviors)

## Contributo concettuale

Il paper argomenta che coding-agent failure va studiato come **processo temporale**, non come label statico success/failure. La framework di annotazione decompone failure in 3 stage con scalabile trajectory analysis.
