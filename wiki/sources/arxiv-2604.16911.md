---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [skills, package-manager, registry, distribution, tooling]
source_path: raw/papers/arxiv-2604.16911.pdf
---

# Skilldex: Package Manager and Registry for Agent Skill Packages

**Autori:** Sampriti Saha, Pranav Hemanth (Pandemonium Research)
**arXiv:** 2604.16911 (apr 2026)

## Summary

Skilldex è un **package manager e registry per skill packages** di agenti LLM. Chiude due gap nel tooling esistente: (1) nessuno strumento punteggia le skill contro la specifica formato di Anthropic, (2) nessun meccanismo bundle skill correlate con shared context per coerenza reciproca.

## Contributi chiave

1. **Compiler-style format conformance scoring**: validazione contro spec Anthropic con diagnostics line-level (description specificity, frontmatter validity, structural adherence)
2. **Skillset abstraction**: bundle di skill correlate + asset condivisi (vocabulary, templates, reference docs) che enforce cross-skill behavioral coherence
3. **Three-tier hierarchical scope system**: global / shared / project
4. **Human-in-the-loop agent suggestion loop**
5. **MCP server** che espone tutte le operazioni agli agenti nativamente
6. Implementazione: TypeScript CLI (`skillpm`/`spm`) + registry Hono/Supabase, open-source

## Relazione con altri lavori

- Complementare a [[wiki/sources/arxiv-2604.24026]] (SSL): Skilldex gestisce *packaging/distribuzione* delle skill, SSL gestisce *rappresentazione interna*
- Si collega a [[wiki/sources/arxiv-2604.22446]] (OMC): Talent Market di OMC potrebbe usare Skilldex come infrastruttura di distribuzione
- Rilevante per l'ecosistema skills di [[wiki/sources/xu-2026-agent-skills-survey]]
