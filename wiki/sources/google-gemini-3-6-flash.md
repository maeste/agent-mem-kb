---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [google, gemini, flash-models, ai-agents, efficiency, cybersecurity]
source_path: raw/web/google-gemini-flash/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Google: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber

**Author:** Tulsee Doshi (Google Gemini team) | **Date:** July 21, 2026 | **URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/

## Summary

Google announces three new Flash-series models focused on token efficiency, latency, and reliability for production AI agents at scale.

## Models Announced

### Gemini 3.6 Flash
- **Workhorse model**: better coding, knowledge work, multimodal performance
- **17% fewer output tokens** than 3.5 Flash (Artificial Analysis Index)
- Up to **65% reduction** on DeepSWE benchmark (Datacurve)
- **Pricing:** $1.50/1M input tokens, $7.50/1M output tokens
- Benchmarks:
  - DeepSWE: 49% vs 37% (3.5 Flash)
  - MLE Bench: 63.9% vs 49.7%
  - OSWorld-Verified: 83.0% vs 78.4%
  - GDPval-AA v2: 1421 vs 1349
- Computer use now a built-in client-side tool via Gemini API and Gemini Enterprise
- Enhanced Frontier Safety safeguards (CBRN, cyber offense)

### Gemini 3.5 Flash-Lite
- **Fastest in 3.5 series**: 350 output tokens/s
- **Pricing:** $0.30/1M input, $2.50/1M output
- Outperforms 3.1 Flash-Lite significantly; even beats 3 Flash on some evals:
  - SWE-Bench Pro: 54.2% vs 49.6%
  - OSWorld-Verified: 74.0% vs 65.1%
  - Terminal-Bench 2.1: 54% vs 31%
  - GDM-MRCR v2: 72.2% vs 60.1%
- Configurable thinking levels for different workloads
- Computer use as built-in tool

### Gemini 3.5 Flash Cyber (in CodeMender)
- Fine-tuned for finding/fixing cybersecurity vulnerabilities
- Multiple agents produce combined report
- Competitive performance on CyberGym benchmark
- **Limited access**: governments + trusted partners only via CodeMender pilot

## Notable Mentions
- Gemini 3.5 Pro testing with partners, broad availability planned soon
- **Gemini 4 pre-training run started** ("most ambitious yet")
