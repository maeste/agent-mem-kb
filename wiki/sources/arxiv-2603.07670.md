---
type: source
created: 2026-07-09
updated: 2026-07-09
tags: [survey, memory-mechanisms, memory-evaluation, agent-memory-taxonomy, benchmarks]
source_path: raw/papers/arxiv-2603.07670.pdf
---

# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**Du** (HK Research Institute of Technology) — arXiv:2603.07670, Mar 2026

## Summary

Survey completo sulla memoria in agent LLM (2022-early 2026), con tassonomia tridimensionale, analisi di 5 famiglie di meccanismi, review di benchmark e applicazioni, e identificazione delle frontiere aperte.

## Claim principali

- **Definizione formale**: agent memory come loop write-manage-read strettamente accoppiato con percezione e azione [[raw/papers/arxiv-2603.07670.pdf]].
- **Tassonomia tridimensionale**: (1) temporal scope; (2) representational substrate; (3) control policy [[raw/papers/arxiv-2603.07670.pdf]].
- **Cinque famiglie di meccanismi**: (1) context-resident compression; (2) retrieval-augmented stores; (3) reflective self-improvement; (4) hierarchical virtual context; (5) policy-learned management [[raw/papers/arxiv-2603.07670.pdf]].
- **Valutazione**: shift da static recall benchmark a multi-session agentic test che interlacciano memory con decision-making. Quattro benchmark recenti analizzati che espongono gap persistenti [[raw/papers/arxiv-2603.07670.pdf]].
- **Applicazioni dove memory è il differentiator**: personal assistants, coding agents, open-world games, scientific reasoning, multi-agent teamwork [[raw/papers/arxiv-2603.07670.pdf]].
- **Engineering realities**: write-path filtering, contradiction handling, latency budgets, privacy governance [[raw/papers/arxiv-2603.07670.pdf]].
- **Open challenges**: continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, multimodal embodied memory [[raw/papers/arxiv-2603.07670.pdf]].

## Posizione nel dibattito

Survey recente e completa. Utile come mappa del territorio. Le 5 famiglie di meccanismi e la tassonomia tridimensionale forniscono un vocabolario comune per classificare nuovi lavori.
