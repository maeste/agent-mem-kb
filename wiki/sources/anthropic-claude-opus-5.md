---
type: source
created: 2026-07-25
updated: 2026-07-25
tags: [anthropic, claude, model-release, opus, agentic, coding-agent, llm-benchmark]
source_path: raw/web/introducing-claude-opus-5/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Introducing Claude Opus 5

**Publisher:** Anthropic | **Date:** Jul 23, 2026 | **URL:** https://www.anthropic.com/news/claude-opus-5

## Summary

Claude Opus 5 launches as the new default model on Claude Max and strongest on Claude Pro. Positioned as near-frontier intelligence at roughly half the cost of Fable 5, with state-of-the-art results on coding and knowledge work benchmarks. Priced at $5/M input, $25/M output (same as Opus 4.8). Emphasis on long-running agency, self-verification, and lower variance across runs.

## Benchmark highlights

- **Frontier-Bench v0.1**: new SOTA, more than doubles Opus 4.8 performance at lower cost per task.
- **CursorBench 3.2**: within 0.5% of Fable 5 peak at half the cost per task.
- **ARC-AGI 3**: 3x the next-best model score.
- **Zapier AutomationBench**: ~1.5x next-best model pass rate; even at lowest effort beats all others.
- **OSWorld 2.0** (computer use): outperforms all models at any given cost; beats Fable 5 at one-third the cost.

## Agentic behavior

Early-access reports emphasize self-verification and thoroughness: writing its own computer vision pipeline to reconstruct a 3D model from raw pixels, finding root causes of bugs a community patch missed, building test harnesses when no validation feed existed. Lower run-to-run variance, sharper planning pushback (challenged a design proposal with narrowed objections rather than folding).

## Safety and alignment

- Most aligned model to date on automated behavioral audit (2.3 misalignment score, lowest among recent models).
- Intentionally not trained on cyber tasks, yet improved through general capability gains. Close to Mythos 5 at finding vulnerabilities, substantially behind on exploitation.
- Cyber classifiers ~85% less restrictive than Fable 5; binary-based scanning, penetration testing, and exploit generation blocked. Cyber Verification Program offers fewer restrictions for vetted enterprises.
- Biology safeguards similar to Opus 4.8; biology requests blocked on Fable 5 now route to Opus 5.

## Two beta features

- **Mid-conversation tool changes**: switch Claude's available tools without invalidating the prompt cache.
- **Automatic fallbacks**: classifier-flagged requests route to the best available model instead of blocking.

## Connection to the vault

Relevant to the harness-design thread ([[wiki/pages/harness-design]]): Opus 5's self-verification and long-running agency behaviors test harness quality, and the mid-conversation tool change feature directly affects harness construction. Adds context to the code-review-load discussion ([[wiki/sources/pragmatic-engineer-code-review-load]]): a more capable coding model shifts more pressure onto review and verification.
