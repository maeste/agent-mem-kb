---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [routing, model-society, diversity, robustness, multi-model, moe]
source_path: raw/papers/2607.09197.pdf
ingested: 2026-W30 (Sat-Sat)
---

# When is Routing Meaningful? Diversity and Robustness in Language Model Societies

**Authors:** Fantine Huot, Michael Kaisers, Mirella Lapata | **arXiv:** 2607.09197 | **Date:** Jul 10, 2026

## Summary

Examines whether routing in multi-model systems is actually meaningful. Two properties orthogonal to performance determine this: (1) the society must contain **behaviourally differentiated** actors, and (2) the routing policy must be **stable** under surface-form variation. Introduces adapted Hierarchic Social Entropy (HSE) to measure diversity and a perturbation-based robustness metric.

## Key Findings

### Diminishing Returns on Diversity
- Fewer than **10 agents** suffice to capture most available diversity in EmbedLLM
- Only **4 agents** needed in RouterBench
- Specialist societies achieve substantially higher HSE than pools of real-world models

### Robustness vs Accuracy Trade-off
- KNN routers achieve best accuracy on specialist societies but **worst robustness** under perturbation
- Prompted routing remains stable across all HSE levels and perturbation types
- High diversity does not imply high robustness

### Practical Implications
A curated subset of fewer than 10 agents recovers most diversity, serving as a coreset heuristic for society design. Real-world model pools have lower behavioural diversity than commonly assumed.
