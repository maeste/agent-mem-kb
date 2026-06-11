---
type: source
created: 2026-06-11
updated: 2026-06-11
tags: [memory, agents, llm, reasoning, causal]
source_path: raw/papers/arxiv-2603.00026.pdf
---

# ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents

Zhang, Sun, Yang, Jin, Zhang, Hu (Nanjing University, Alibaba), February 2026.

ActMem identifica una lacuna critica nei sistemi di memoria agentica: la disconnessione tra reperimento di memoria e ragionamento. Mentre i framework esistenti trattano l'agente come un "registratore" passivo che recupera fatti basandosi su similarità semantica, ActMem argomenta che l'agente deve essere un "reasoner" attivo che usa la memoria per informare le decisioni correnti. Il framework trasforma la storia di dialogo non strutturata in un grafo causale e semantico strutturato. Usa ragionamento controfattuale e commonsense completion per dedurre vincoli impliciti e risolvere conflitti tra stati passati e intenzioni presenti. Introduce ActMemEval, un dataset che valuta capacità di ragionamento logic-driven piuttosto che solo fact-retrieval. L'esempio motivante: un utente chiede dove comprare "Sago Palms" mentre in passato ha menzionato un cucciolo che mastica tutto; un agente con ragionamento deduce il conflitto (Sago Palms sono tossici per i cani) e interviene con un warning.
