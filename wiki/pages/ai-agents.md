---
type: page
created: 2026-07-23
updated: 2026-07-23
tags: [agents, harnesses, software-factories, memory, skills, failure-analysis]
---

# AI Agents

Pagina hub su agent LLM: architettura, harnesses, failure analysis, memory e skills.

## Harnesses e compositional generalizzazione

L'harness non e solo plumbing tra modello e ambiente; e il veicolo principale per **inductive bias di alto livello** che abilita compositional generalization [[wiki/sources/alex-zhang-harnesses]]. I Transformer sono intrinsecamente poveri nel comporre conoscenza da domini diversi; un buon harness riduce problemi complessi a sequenze di sottoproblemi **localmente in-distribution** per il neural network.

Componenti chiave di un harness efficace [[wiki/sources/alex-zhang-harnesses]]:
- **Context offloading**: contesto specifico passato come variabile simbolica, non iniettato nel prompt root
- **Programmatic sub-agent calling**: sub-call trattate come funzioni in REPL; output mai visti dal root LM
- Equivalenza di task (~_H): task strutturalmente simili appaiono token-for-token identici al root LM

Il Recursive Language Model (RLM) dimostra training su task brevi che generalizza a task 8-32x piu lunghi con ~10x eval lift [[wiki/sources/alex-zhang-harnesses]].

## Software factory metafora

La "fabbrica software" organizza il lavoro agentic in tre strati [[wiki/sources/software-factories-light-dark]]:
- **Loop**: unita atomica (gather context -> action -> check -> repeat)
- **Harness**: sandbox, tools, memory, gate di completamento
- **Factory**: molti loop harnessed, queue-driven, review gate prima di production

Distinzione critica **dark vs light**:
- Dark: code ships senza review umano; accumula comprehension debt; dopo ~4 mesi richiede debugging manuale massiccio
- Light: giudizio umano upstream (design/architettura) + review; safety net = architettura ordinaria (tipi, test seams, boundary nette)

**Back pressure principle**: autonomia del loop non puo superare capacita di verifica. Loop corti (3-10 step) verificabili; lunghi (>20) nascondono errori [[wiki/sources/software-factories-light-dark]].

## Memory e skills da traiettorie

### MSCE: Memory-Skill Co-Evolution
Framework training-free con gerarchia a 3 livelli [[wiki/sources/arxiv-2607-16621-msce]]:
- L1 traces (evidence grounded), L2 policies (pattern procedurali), L3 env cognition (conoscenza dichiarativa)
- Skill crystallization: solo L2 policies con evidence support, positive gain, stability diventano skill callable
- Reflection-weighted value backfilling propaga sparse terminal feedback via dense self-reflections
- Risultati SOTA su EvoAgentBench e LoCoMo, forte cross-domain transfer

### Harness evolution: evaluation gap
I paper su harness evolution potrebbero sovrastimare i guadagni: confrontando contro test-time scaling baselines under matched budget, harness evolution non supera consistentemente parallel sampling o sequential refinement [[wiki/sources/arxiv-2607-12227-harness-evolution]]. Bisogna sempre includere baselines di search e held-out evaluation.

## Failure analysis

### Failure come processo temporale
Studio su 1,794 CLI coding trajectories (63k+ steps): le failures iniziano tipicamente nei primi pochi step, driven da **epistemic errors**, rimangono hidden finche recovery e impossibile [[wiki/sources/arxiv-2607-09510-cli-failure]]. Implicazione: validazione precoce > final-outcome evaluation.

### OAT: unsupervised failure attribution
Training esclusivamente su 100 traiettorie successful, zero failure data. Usa Neural CDEs per modellare dinamica successful in latent space; anomaly scores per step identificano error contributing steps [[wiki/sources/arxiv-2607-12747-oat]]. 200-5000x piu veloce di prompting-based approaches, +20% F1 in-domain, +7% OOD.
