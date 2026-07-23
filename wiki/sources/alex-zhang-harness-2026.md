---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [harness, compositional-generalization, rlm, inductive-bias, scaling, agent-architecture]
source_path: raw/web/alex-zhang-harness-2026/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Language Model Harnesses Are Compositional Generalizers

**Author:** Alex Zhang, Omar Khattab | **Date:** Jul 2026 | **URL:** https://alexzhang13.github.io/blog/2026/harness/

## Summary

Argues that compositional generalization (solving unseen problems by composing familiar ones) should live in the **harness**, not the neural network. Introduces the Recursive Language Model (RLM) harness: context offloading + programmatic sub-agent calling, which makes each individual LM call **locally in-distribution (LID)**. Experiments show training RLMs on short tasks generalizes to tasks 8-32x longer, and training on one domain transfers to unseen domains.

## Core Argument

### The Problem
Transformers are poor at compositional generalization. Modern post-training brute-forces this with ever more environments and longer horizons. Scaling data is the biggest driver of progress, but the machinery's inductive biases determine the coefficients of that scaling.

### Harness as Inductive Bias Carrier
A harness H: s → a sits between environment and neural network. Its fundamental power: simplifying arbitrarily complex state s into smaller observations o that each LM call handles in-distribution. A good harness reduces unfamiliar problems to familiar ones.

### Locally In-Distribution (LID)
Existing harnesses (Claude Code, Codex) fail at LID because they flood context with interleaved tool calls and reasoning, causing context rot. RLM fixes this via:
1. **Context offloading**: input-specific context passed as symbolic variable, root LM doesn't see it directly
2. **Programmatic sub-agent calling**: sub-agents treated as REPL functions, outputs stored in variables, root LM never needs to see task-specific information

### Equivalence Classes
RLM induces an equivalence relation ∼_H over task states. Structurally similar tasks fall under the same class and produce near token-for-token identical trajectories for the root LM. This enables transitive generalization: if system can solve X, it can solve Y.

## Experimental Results

### Length Generalization
- 6 benchmarks (MRCRv2, GraphWalks, OOLONG, etc.)
- Train on short splits, eval on 8-32x longer
- RLM with Qwen3-30B-A3B approaches or exceeds GPT-5.5 with RLM harness
- Base Transformer eval stays flat despite growing train reward

### Strategy Generalization
- Train on one domain, eval on completely different domain sharing latent structure
- RLM generalizes; base Transformer doesn't
- Train reward of RLM closely matches eval reward trend

### Cost
RLM training is 1.5-3x slower than base Transformer due to multiple steps and sub-calls. But scales better with task complexity.
