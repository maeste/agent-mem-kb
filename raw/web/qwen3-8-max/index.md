---
source_url: https://qwen.ai/blog?id=qwen3.8&utm_source=tldrai
title: "Qwen3.8-Max: A New Bar for Coding and Cowork"
author: Qwen Team
published: 2026-08-03
language: en
fetched: 2026-08-04
fetched_via: manual_api  # qwen.ai is CSR-only; content pulled from /api/v2/article/?path=qwen3.8
---

# Qwen3.8-Max: A New Bar for Coding and Cowork

August 3, 2026 · 31 min · 6460 words · Qwen Team

Today, we are officially releasing **Qwen 3.8-Max**, the most capable model in the Qwen family to date. This also marks the first time we will open-source the weights of a Qwen-Max-class model — the open weights will be released next week. Built upon the architectural foundation of Qwen 3.5, Qwen 3.8-Max scales to **2.4 trillion** parameters, delivering comprehensive improvements across coding, work, research, and long-horizon tasks. It can not only answer more challenging questions, but also complete complex tasks end-to-end with greater reliability, producing dependable deliverables.

- **Qwen3.8-Max** — now available via QwenCloud:
- 2.4T parameters (95B active), with open weights releasing next week
- comprehensive improvements across coding, work, research, and long-horizon tasks
- end-to-end and dependable delivery of complex tasks
- Call via API on QwenCloud.

## Coding

For a top model, coding today means far more than writing a function on request — it means taking a real, multi-day project from an empty folder all the way to a finished result, on its own. We tested Qwen3.8-Max on three such challenges, where every result had to be earned by actually writing and running code, with **no human help at all**. One thread runs through all three: Qwen3.8-Max doesn't just follow a fixed plan — it **self-evolves through feedback loops**, whether that means building a harness that upgrades itself, refining a research method experiment after experiment, or climbing a competition leaderboard submission after submission.

### 10+ Days of Autonomous Coding: Building a Self-Evolving Harness

In this case, Qwen3.8-Max was asked to create the oh-my-cli project from scratch and, over a 10+ day long-horizon autonomous coding run, build a self-evolving harness. It brings user feedback, advanced community practices, and the model's own self-test results into one engineering loop: requirements are normalized into issues, automatically claimed and executed by agents, and continuously iterated through code, tests, previews, and logs. The complete project trace is publicly available in the GitHub repository qwen-code-dev-bot/oh-my-cli.

**Key implementation details in the autonomous coding harness:**

- **Loop Engineering Setup: task state, dispatch, and recovery.** Qwen3.8-Max combines an issue state machine, dispatcher, monitor, and watchdog into one execution loop: after a new requirement enters GitHub Issues, an agent claims it through the state machine and moves through ready → leased → active; once implementation is complete, E2E tests and CI checks are triggered, and the PR is merged after passing.
- **Self-testing: product self-testing and maintenance.** After each update, the model triggers Build, Unit Test, E2E, and Desktop Lifecycle validation; abnormal states are routed back to the relevant issue / PR for fixes and re-verification.
- **Multi-source Evolution:** product upgrades from multiple demand signals. By converting community experience and user / developer feedback into executable work, the harness continuously evolves /goal, /resume, Dynamic Workflow, Session Replay, Desktop, and other capabilities.

As of **July 30, 2026**, after approximately **16 days** of fully autonomous AI operation, the repository had accumulated **265 commits, 127 PRs, and 151 issues**, demonstrating a continuously evolving autonomous coding capability.

### Reproduce a research paper — then improve it

We handed Qwen3.8-Max a recent research paper — *"Unified Data Selection for LLM Reasoning"* — and asked it to: **reproduce the paper's experiment in code, then try to do better.**

Working **completely on its own for about five days** (~125 hours of continuous effort), Qwen3.8-Max wrote roughly **7,600 lines of code**, took over **1,100 actions**, and ran **33 rounds of GPU training**. It first spent ~37 hours rebuilding the paper's full pipeline from zero and **reproduced its six main findings**. Then it went further, turning reproduction into **self-evolution**: over the next ~88 hours it ran a self-improving research loop, inventing and testing **18 improvement ideas of its own across four rounds**. By round 4 it evolved a new method ("nhighgate" — count the hard decision points) that **beats the paper's own approach by +2.71 points** on AIME24.

| Round | Best idea that round | Score (AIME24) | Gain vs. baseline |
|-------|----------------------|----------------|-------------------|
| — | Paper's method, reproduced (baseline) | 49.58% | — |
| 1 | Split the data by difficulty before selecting | 50.42% | +0.84 |
| 2 | Weight examples by an entropy–score gap | 51.67% | +2.09 |
| 3 | Tune the selection width | 51.25% | +1.67 |
| 4 | **Count the hard decision points ("nhighgate")** ★ | **52.29%** | **+2.71** |

### Beat hundreds of human teams in 24 hours

Qwen3.8-Max entered the WWW2025 Multimodal Dialogue Intent Recognition Challenge (Alibaba Cloud's Tianchi platform), where **526 human teams** were competing. The task: read customer-service chats — both text and screenshots — and work out what the customer wants. Working entirely on its own under a **24-hour** limit, it built a full solution: fine-tuned and ensembled BERT, MacBERT, RoBERTa for text; Qwen2.5-VL-7B for screenshots; Chinese-CLIP as a tie-breaker; fused into a weighted-voting system. Across **45 submissions** its accuracy climbed from 0.60 to 0.853, beating **458 of 526 human teams (87%)**.

## Work

Making Qwen3.8-Max broadly competent and reliably robust across the messy, multi-step, tool-heavy tasks that fill the working day.

### Autonomous Hardware Design (EDA / RTL → Physical Silicon)

Qwen3.8-Max was given a modular exponentiation RTL design (RSA core) and asked to optimize it through an "edit-simulate-synthesize-layout" feedback loop over **500 turns**, no reference design. It drove gate count from **8,298 → 678** (8 stages of optimization: algorithmic rewrite of modulo divider to shift-subtract, redundancy elimination, bitwidth trimming, register/FSM pruning, module fusion, gate-level refinement). Verified through OpenROAD place-and-route (Nangate45 PDK): die area shrank from 106×106 µm² to 46×46 µm² (−81%), wirelength 33,369 → 4,187 µm, timing closure at 500 MHz (+0.66 ns slack).

### Continuous Learning in Long-term Operations (E-Commerce Bench)

365-day e-commerce operation simulation (12 store types, 60 product categories, ~600 suppliers, 7,000 products, ¥100,000 starting capital). Qwen3.8-Max achieved **¥416,252 total balance (4.16x return)**, surpassing second-place GLM 5.2 by 38% and +152% over its own previous Qwen3.7-Max. Demonstrated **continuous learning in supplier negotiations** (progressive price reductions, efficiency expanding over time) and forward-looking capital allocation.

## Multimodal Agents

Visual intelligence through the entire task lifecycle. Documents >200 pages → structured reports; videos >100 hours → video memory graph. Vision is not limited to input: during execution the model continuously observes and evaluates its own intermediate results, identifying deviations and correcting output autonomously (visual feedback loop across planning, execution, verification, iteration).

**RecreationBench**: long-horizon application-recreation benchmark across 5 platforms (Ubuntu, macOS, Windows, Android, web) — observe a running app as a black box, rebuild it from scratch.

**Qwen-MM-Plugins**: harness extension library for multimodal agents (image/video processing, multimodal memory, dynamic resolution, visual tool use, video editing, Blender, CAD) — any existing agent harness can be extended into a multimodal-native system.

## API Usage

Qwen3.8-Max supports `reasoning_effort` (xhigh default, medium, low) and `preserve_thinking` enabled by default. QwenCloud supports OpenAI-compatible chat completions / responses APIs and an Anthropic-compatible interface. Integrates with Claude Code (Anthropic API protocol), Codex (OpenAI Responses protocol), and Qoder CLI.

## Selected Benchmark Highlights

Coding Agent: Terminal Bench 2.1 86.6, SWE-bench Pro 67.7, FrontierSWE 73.5, PaperBench 93.0, AndroidBench 75.1. General Agent: CoWorkBench 74.8, Agents' Last Exam 27.0/52.4, WideSearch 81.9. General Capabilities: GPQA Diamond 92.6, HLE 43.6, MRCR v2 256K 92.9. Multimodal: MMMU-Pro 82.3, BabyVision 82.0/91.3, Visual Agent OSWorld-Verified 86.1, RecreationBench 51.7.
