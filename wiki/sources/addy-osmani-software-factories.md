---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [software-factory, agentic, harness, comprehension-debt, dark-factory, loop-engineering]
source_path: raw/web/addy-osmani-software-factories/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Software Factories, Light and Dark

**Author:** Addy Osmani | **Date:** Jul 22, 2026 | **URL:** https://addyo.substack.com/p/software-factories-light-and-dark

## Summary

Osmani defines three layered abstractions for agentic software development: **loop** (single agent doing one job on repeat), **harness** (walls around the loop: sandbox, tools, memory, gates), and **factory** (many harnessed loops fed by a queue, drained through a review gate into production). The core argument is that the bottleneck is not generation but **verification**: unbounded generation meets a narrow human-review gate, creating back pressure.

## Key Concepts

### Dark vs Lit Factory
- **Dark factory**: code ships with no human review. Borrowed from lights-out manufacturing (FANUC, Xiaomi). Feels fast but accumulates **comprehension debt**: the gap between code existing and humans understanding it.
- **Lit factory**: same pipeline, lights left on where judgment lives. Human review moves upstream to design and architecture, not just at the end.

### Comprehension Debt
The widening gap between how much code exists and how much any human understands. Dark factories don't pay it down; they take it on as fast as possible while tests stay green. The reckoning is quiet and late.

### Back Pressure
Rule: you can only hand a loop as much autonomy as you can cheaply and reliably verify. Volume isn't the problem; surplus of bad PRs is. Autonomy can't expand beyond verification capacity.

### Loops vs Graphs
Osmani argues for structured **graphs** (state machines, conditionally-linked service calls) over free-form loops. Graphs constrain agent freedom to sanctioned paths, making failure points legible. References LangGraph, LlamaIndex Workflows, Jerry Liu's hybrid workflow-graph-over-agents, 12-factor-agents.

### What earns a loop the dark
A loop earns full automation only if the check is cheap, runs at high frequency, and can't be easily faked. Short loops (3-10 steps) verify better than sprawling ones (20+ steps lose the thread).

### The Outer Loop
Engineers should own the **outer loop**: decide whether the approach is right, verify soundness, approve changes, carry consequences. The inner loop (investigate, fix, test) can be delegated. The boundary between them is evidence.
