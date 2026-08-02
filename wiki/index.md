---
type: page
created: 2026-07-22
updated: 2026-08-01
tags: [index, weekly-review-W30]
---

# Index

Catalog of the vault. Updated on every write operation.

## Pages

- [[wiki/pages/harness-design]] — Harness come ambiente del loop; cinque visioni (Osmani, Zhang, Wang eval, OpenAI ARC-AGI, Anthropic); behavior localization, harness come variabile misurata, harness meno prescrittivi
- [[wiki/pages/comprehension-debt]] — Divario tra codice esistente e codice capito; dark vs lit factory; back pressure
- [[wiki/pages/compositional-generalization]] — RLM, locally in-distribution, equivalence classes; generalizzazione via harness
- [[wiki/pages/moe-sparsity]] — Trend sparsity nei modelli aperti; active vs total params; compute-to-storage shift
- [[wiki/pages/agent-failure-analysis]] — Failure come processo temporale; errori epistemici; OAT attribution
- [[wiki/pages/memory-skills-co-evolution]] — Memoria attiva vs passiva; gerarchia L1/L2/L3 + programmatic memory (PRO-LONG) + auto-memory (Claude 5); skill crystallization

## Sources

### Agentic Engineering & Harness Design
- [[wiki/sources/addy-osmani-software-factories]] — Software factories: loops, harnesses, dark vs lit, comprehension debt, back pressure
- [[wiki/sources/pragmatic-engineer-code-review-load]] — Code review bottleneck: AI generation shifted load to review, tool boom, verification vs review
- [[wiki/sources/alex-zhang-harness-2026]] — Harnesses as compositional generalizers: RLM, locally in-distribution, equivalence classes
- [[wiki/sources/arxiv-2607-12227-harness-evaluation]] — Rethinking harness evolution evaluation: doesn't beat test-time scaling, limited generalization
- [[wiki/sources/arxiv-2607.13285-harness-handbook]] — Harness Handbook: behavior localization come bottleneck; representation behavior-centric + BGPD
- [[wiki/sources/anthropic-claude-5-context-engineering]] — Claude 5: rimosso 80% system prompt; rules→judgement, progressive disclosure, auto-memory
- [[wiki/sources/openai-arc-agi-3-harness]] — ARC-AGI-3: retained reasoning + compaction = 3x score, 6x meno token; l'harness è la variabile misurata
- [[wiki/sources/arxiv-2607-16621-msce-memory-skills]] — Memory-to-skills co-evolution: L1/L2/L3 memory hierarchy, skill crystallization
- [[wiki/sources/arxiv-2607-09510-failure-as-process]] — CLI coding agent failure trajectories: epistemic errors, early onset, late discovery
- [[wiki/sources/arxiv-2607-12747-oat-failure-attribution]] — OAT: unsupervised failure attribution from successful trajectories via neural CDEs

### Multi-Model Systems & Routing
- [[wiki/sources/arxiv-2607-09197-routing-meaningful]] — When routing is meaningful: diversity (HSE), robustness, diminishing returns (<10 agents)

### Long-Horizon Reasoning & Memory
- [[wiki/sources/arxiv-2607.20064-pro-long]] — PRO-LONG: programmatic memory (append-all log + code-based read); +18pt ARC-AGI-3, fidelity-tractability tradeoff

### Model Scaling & Architecture
- [[wiki/sources/akash-bajwa-sparse-by-design]] — MoE sparsity trend: Kimi K3, active vs total params, compute-to-storage shift
- [[wiki/sources/thinking-machines-inkling-small]] — Inkling-Small: 276B/12B MoE open-weights, multimodal nativo, reasoning effort controllabile, 1M context
- [[wiki/sources/openai-gpt-5-6-pricing]] — GPT-5.6: Luna -80%, Terra -20%, Sol Fast mode; Sol auto-ottimizza kernel (-20% serving cost)
- [[wiki/sources/google-gemini-3-6-flash]] — Gemini 3.6 Flash, 3.5 Flash Lite, 3.5 Flash Cyber

### Robotics & Embodied Reasoning
- [[wiki/sources/gemini-robotics-er-2]] — Gemini Robotics ER 2: embodied reasoning, temporal intelligence, multi-robot collaboration

### Multimodal & Image Generation
- [[wiki/sources/qwen-image-3]] — Qwen-Image-3.0: rich content, authentic details, deep knowledge

### Industry & Security
- [[wiki/sources/openai-hf-security-incident]] — OpenAI/Hugging Face model evaluation security incident
- [[wiki/sources/antirez-news-170]] — antirez.com news #170

### Model Releases
- [[wiki/sources/anthropic-claude-opus-5]] — Claude Opus 5: near-Fable 5 intelligence at half cost; SOTA on Frontier-Bench, CursorBench, ARC-AGI 3; most aligned model to date

## Views

- [[wiki/views/comparison-graph-vs-loop]] — Tutto grafo vs tutto loop: 4 tensioni irrisolte (routing, visibilità, design vs search, bitter lesson)
- [[wiki/views/weekly/2026-W30]] — Weekly review W30: 15 fonti, 6 pagine, harness come fulcro convergente

## Timeline

| Week | Sources Ingested | Pages Touched | Notes |
|------|-----------------|---------------|-------|
| W30/2026 (Jul 18–Aug 1) | 20 | 9 | Vault v2 reset + bulk ingest (12 sources Jul 23) + 6 conceptual pages + 1 comparison view. +1 source Jul 24 (code review load). +2 sources Jul 25 (Harness Handbook, Claude Opus 5). +1 source Jul 31 (Inkling-Small), moe-sparsity page updated. +6 sources Aug 1 (Gemini Robotics ER 2, GPT-5.6 pricing, ARC-AGI-3 harness, Claude 5 context eng, Harness Handbook, PRO-LONG); harness-design + memory-skills pages updated. Weekly review W30 generated. |

## Reflections

- [[wiki/compass.md]] — Bussola della vault
