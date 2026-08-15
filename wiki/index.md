---
type: page
created: 2026-07-22
updated: 2026-08-15
tags: [index, weekly-review-W30, weekly-review-W31, weekly-W31-corrected, weekly-review-W33]
---

# Index

Catalog of the vault. Updated on every write operation.

## Pages

- [[wiki/pages/harness-design]] — Harness come ambiente del loop; sei visioni (Osmani, Zhang, Wang eval, OpenAI ARC-AGI, Anthropic, Miessler + LoopX) + cornice WHAT vs HOW; behavior localization, harness come variabile misurata, spettro auto-prodotto vs externalizzato
- [[wiki/pages/comprehension-debt]] — Divario tra codice esistente e codice capito; dark vs lit factory; back pressure
- [[wiki/pages/compositional-generalization]] — RLM, locally in-distribution, equivalence classes; generalizzazione via harness
- [[wiki/pages/moe-sparsity]] — Trend sparsity nei modelli aperti; active vs total params; compute-to-storage shift; ByteDance 10T in pre-training
- [[wiki/pages/agent-failure-analysis]] — Failure come processo temporale; errori epistemici; OAT attribution
- [[wiki/pages/memory-skills-co-evolution]] — Memoria attiva vs passiva; gerarchia L1/L2/L3 + programmatic memory (PRO-LONG) + auto-memory (Claude 5); skill crystallization

## Sources

### Agentic Engineering & Harness Design
- [[wiki/sources/prime-agent]] — Prime Intellect: RLM + Continual Harness, `/refine` self-improvement CRUD; 95.5% RHAE ARC-AGI-3 con Opus 5
- [[wiki/sources/kiro-agent-harness]] — Kiro/AWS: harness come processo server standalone, Agent Client Protocol, permission Cedar capability-based
- [[wiki/sources/meta-muse-code-spark-1-2]] — Meta: Muse Code (async agents, event log) + Muse Spark 1.2 co-trained con harness; self-improvement loop
- [[wiki/sources/arxiv-2607.28576-more-reflect-less]] — Self-Refine/Reflexion perdono vs repeated sampling a pari costo token; 18/18 self-inspection negativi
- [[wiki/sources/addy-osmani-software-factories]] — Software factories: loops, harnesses, dark vs lit, comprehension debt, back pressure
- [[wiki/sources/pragmatic-engineer-code-review-load]] — Code review bottleneck: AI generation shifted load to review, tool boom, verification vs review
- [[wiki/sources/alex-zhang-harness-2026]] — Harnesses as compositional generalizers: RLM, locally in-distribution, equivalence classes
- [[wiki/sources/arxiv-2607-12227-harness-evaluation]] — Rethinking harness evolution evaluation: doesn't beat test-time scaling, limited generalization
- [[wiki/sources/arxiv-2607.13285-harness-handbook]] — Harness Handbook: behavior localization come bottleneck; representation behavior-centric + BGPD
- [[wiki/sources/anthropic-claude-5-context-engineering]] — Claude 5: rimosso 80% system prompt; rules→judgement, progressive disclosure, auto-memory
- [[wiki/sources/openai-arc-agi-3-harness]] — ARC-AGI-3: retained reasoning + compaction = 3x score, 6x meno token; l'harness è la variabile misurata
- [[wiki/sources/danielmiessler-harness-question]] — Harness = WHAT (apprezza) + HOW (marcisce); intent engineering; risolve tensione ARC-AGI-3 vs Claude 5
- [[wiki/sources/agent-behavior]] — Formato standard per behavior spec: BEHAVIOR.md vs AGENTS.md, dimensioni (Intent/Evidence/Decision/Execution/Recovery)
- [[wiki/sources/loopx]] — LoopX: state kernel provider-neutral per loop engineering long-running; control plane externalizzato vs harness auto-prodotto
- [[wiki/sources/arxiv-2607-16621-msce-memory-skills]] — Memory-to-skills co-evolution: L1/L2/L3 memory hierarchy, skill crystallization
- [[wiki/sources/arxiv-2607-09510-failure-as-process]] — CLI coding agent failure trajectories: epistemic errors, early onset, late discovery
- [[wiki/sources/arxiv-2607-12747-oat-failure-attribution]] — OAT: unsupervised failure attribution from successful trajectories via neural CDEs

### Multi-Model Systems & Routing
- [[wiki/sources/arxiv-2607-09197-routing-meaningful]] — When routing is meaningful: diversity (HSE), robustness, diminishing returns (<10 agents)

### Long-Horizon Reasoning & Memory
- [[wiki/sources/arxiv-2607.20064-pro-long]] — PRO-LONG: programmatic memory (append-all log + code-based read); +18pt ARC-AGI-3, fidelity-tractability tradeoff
- [[wiki/sources/zero-mem]] — Zero-Mem: operazioni di memoria a costo zero, nessuna LLM call fuori final QA; entity-context graph + temporal hierarchy

### Model Scaling & Architecture
- [[wiki/sources/diffusiongemma]] — Google DeepMind: discrete diffusion per generazione testo, ~1.500 token/s H100, nuova Pareto speed/capability
- [[wiki/sources/openai-astra-math]] — OpenAI Astra (unreleased): 10 problemi matematici aperti risolti per ~$2k token, certificati Lean; verifiability come abilitatore
- [[wiki/sources/akash-bajwa-sparse-by-design]] — MoE sparsity trend: Kimi K3, active vs total params, compute-to-storage shift
- [[wiki/sources/thinking-machines-inkling-small]] — Inkling-Small: 276B/12B MoE open-weights, multimodal nativo, reasoning effort controllabile, 1M context
- [[wiki/sources/openai-gpt-5-6-pricing]] — GPT-5.6: Luna -80%, Terra -20%, Sol Fast mode; Sol auto-ottimizza kernel (-20% serving cost)
- [[wiki/sources/google-gemini-3-6-flash]] — Gemini 3.6 Flash, 3.5 Flash Lite, 3.5 Flash Cyber
- [[wiki/sources/kaitchup-agentic-two-scales]] — Nanbeige4.2-3B (Looped Transformer, sparsity temporale) + Laguna S 2.1 (118B/8B MoE coding); benchmark transparency
- [[wiki/sources/deepseek-v4-flash-api]] — DeepSeek V4-Flash/Pro API: $0.14/$0.28 per 1M, 1M context, 384K output, thinking + non-thinking modes
- [[wiki/sources/qwen3-8-max]] — Qwen3.8-Max: 2.4T/95B MoE, primo Max-class open weights; self-evolving harness (oh-my-cli), coding autonomo 16 giorni, multimodal feedback loop
- [[wiki/sources/bytedance-10t-model]] — ByteDance: ~10T params in pre-training (FT via 3 insider), ~3x Kimi K3; scala finale non fissata

### Robotics & Embodied Reasoning
- [[wiki/sources/gemini-robotics-er-2]] — Gemini Robotics ER 2: embodied reasoning, temporal intelligence, multi-robot collaboration
- [[wiki/sources/xiaomi-robotics-1]] — Xiaomi: foundation model embodied AI open-source, 100k+ ore UMI data, cross-embodiment post-training

### Multimodal & Image Generation
- [[wiki/sources/qwen-image-3]] — Qwen-Image-3.0: rich content, authentic details, deep knowledge

### Industry & Security
- [[wiki/sources/hassabis-dean-exit]] — Google DeepMind reorg: Hassabis chief scientist Alphabet, Dean fonda Discovery Loop PBC; Gemini 4 confermato
- [[wiki/sources/openai-hf-black-hat-debrief]] — OpenAI Black Hat 2026: agenti autonomi colludono via message board emergente in Artifactory
- [[wiki/sources/uber-adr]] — Uber ADR: detection and response enterprise per AI agent, ADR-Bench 17 attack technique, dual-agent detector
- [[wiki/sources/openai-gpt-live]] — OpenAI GPT-Live: voice AI full-duplex, media path vs application logic separati, WARP protocol
- [[wiki/sources/firecrawl-anydoc]] — Firecrawl: libreria Rust doc-to-markdown sub-5ms, 13 formati, ships come Agent Skill
- [[wiki/sources/openai-hf-security-incident]] — OpenAI/Hugging Face model evaluation security incident
- [[wiki/sources/antirez-news-170]] — antirez.com news #170

### AI Economics & Continual Learning
- [[wiki/sources/dwarkesh-era-of-continual-learning]] — Dwarkesh: 8 previsioni continual learning; switching cost come moat, economies of scale inference, regolazione obsoleta

### Model Releases
- [[wiki/sources/anthropic-claude-opus-5]] — Claude Opus 5: near-Fable 5 intelligence at half cost; SOTA on Frontier-Bench, CursorBench, ARC-AGI 3; most aligned model to date

## Views

- [[wiki/views/slides-self-improvement-continuous-learning]] — Slide deck: self-improvement continuo degli agenti (modello + harness/memoria), 12 slide
- [[wiki/views/comparison-graph-vs-loop]] — Grafo vs loop: 8 dimensioni, 4 tensioni irrisolte
- [[wiki/views/weekly/2026-W30]] — Weekly review W30: 15 fonti, 6 pagine, harness come fulcro convergente
- [[wiki/views/weekly/2026-W31]] — Weekly review W31: 17 fonti, cluster harness espanso a 7 visioni, agent security, self-reflection debunked, 4 paradigmi memoria, continual learning
- [[wiki/views/weekly/2026-W33]] — Weekly review W33: 0 nuovi ingest, slides view, recupero incidente branch (15 fonti ripristinate)

## Timeline

*Convenzione label: la settimana 1-8 ago è etichettata W31 in tutta la vault (label inaugurale; ISO sarebbe W32). Dalla settimana di Aug 8-15 le label seguono `date +%Y-W%V` del sabato di generazione.*

| Week | Sources Ingested | Pages Touched | Notes |
|------|-----------------|---------------|-------|
| W30/2026 (Jul 22–Aug 1) | 24 | 6 created + 6 modified | Vault v2 reset + bulk ingest (12 sources Jul 23) + 6 conceptual pages + 1 comparison view. +1 source Jul 24 (code review load). +2 sources Jul 25 (Harness Handbook, Claude Opus 5). +1 source Jul 31 (Inkling-Small). +6 sources Aug 1 cron + 4 sources Aug 1 manual. harness-design cresciuta da 3 a 5 visioni + cornice WHAT/HOW. moe-sparsity (+Looped Transformer, +DeepSeek V4). Weekly reviews W30 + W31 generated. |
| W31/2026 (Aug 1–8) | 17 | 2 modified | Cluster harness espanso a 7 visioni: +auto-prodotto (Qwen), +externalizzato (LoopX), +continual (Prime Agent, Muse Code), +standalone (Kiro). Agent security emerso (HF Black Hat collusion + Uber ADR). Self-reflection debunked (More-Reflect-Less). Zero-Mem quarto paradigma memoria. Scale race: ByteDance 10T, Qwen 2.4T/95B. DiffusionGemma nuova Pareto speed/capability. Dwarkesh: continual learning come discontinuità (switching cost, moat, economies of scale inference). 6 fonti senza casa concettuale. |
| W33/2026 (Aug 8–15) | 0 | 0 (1 view created) | Inbox vuota tutta la settimana. Creata slides view self-improvement (12 slide, 14 based_on). Incidente recuperato: 15 source pages W31 + 2 aggiornamenti pagine + ~20 raw dirs rimasti su branch locale mai pushato (daily cron 7-8 ago), ripristinati su disco il 15 ago. Prima esecuzione lint. |

## Reflections

- [[wiki/compass.md]] — Bussola della vault
