---
type: source
created: 2026-05-05
updated: 2026-05-05
tags: [skills, agents, llm]
source_path: raw/papers/arxiv-2604.16911.pdf
---

# Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution

Saha, Hemanth (Pandemonium Research), April 2026.

Skilldex is a package manager and registry for LLM agent skill packages, addressing two gaps in existing skill tooling: the lack of spec-grounded conformance scoring against Anthropic's SKILL.md format specification, and the absence of a mechanism for bundling related skills with shared context assets. The system introduces compiler-style format conformance scoring (0–100 scale) that produces line-level diagnostics on description specificity, frontmatter validity, and structural adherence. Its novel *skillset abstraction* bundles related skills with shared assets (vocabulary files, templates, reference documents) to enforce cross-skill behavioral coherence — a property that independently installed skills cannot guarantee. Supporting infrastructure includes a three-tier hierarchical scope system (global, shared, project), a human-in-the-loop agent suggestion loop, a metadata-only community registry with trust tiers seeded from Anthropic's official skills, and a Model Context Protocol (MCP) server that exposes all operations to agents natively. The system is implemented as a TypeScript CLI (`skillpm`/`spm`) with a Hono/Supabase registry backend. Skilldex positions skill packages as analogous to software libraries, arguing that they need the same packaging, versioning, and dependency management disciplines that npm or pip provide for code.
