---
type: source
source_path: raw/web/the-new-rules-of-context-engineering-for-claude-5-generation-models-claude-by-an/index.md
ingested: 2026-W30 (Sat-Sat)
created: 2026-08-01
updated: 2026-08-01
tags: [context-engineering, prompt-design, harness-design, progressive-disclosure, anthropic, claude-5]
---

# Claude 5: nuove regole di context engineering

Anthropic (Shihipar; 2026-07-24). Anthropic ha rimosso oltre l'80% del system prompt di Claude Code per Opus 5 / Fable 5 senza perdita misurabile sulle coding evals. Cinque shift di paradigma nel context engineering.

## Punti chiave

- **Rules → Judgement**: i guardrail ("non scrivere commenti", "non creare documenti") erano necessari per evitare worst-case sui modelli vecchi. Modelli nuovi hanno judgement migliore: meglio "match the surrounding code" che regole assolute.
- **Examples → Interface design**: dare esempi vincola lo spazio di esplorazione. Meglio progettare parametri espressivi (enum status pending/in_progress/completed come hint semantico).
- **All upfront → Progressive disclosure**: caricare il contesto giusto al momento giusto. Skill selettivamente chiamate, tool deferred loading (ToolSearch), CLAUDE.md come albero di file caricati on-demand invece di monolite.
- **Repetition → Tool descriptions**: istruzioni duplicate nel system prompt e nel tool description erano necessarie per ascolto. Istruzioni ora vivono solo nel tool description.
- **Manual memory → Auto-memory**: l'utente non deve più scrivere a mano in CLAUDE.md con #hotkey. Claude salva automaticamente memorie rilevanti al lavoro.

## Collocazione nel vault

Direttamente rilevante per [[wiki/pages/harness-design]] (il system prompt è parte dell'harness) e [[wiki/pages/memory-skills-co-evolution]] (auto-memory, progressive disclosure, skill crystallization). Conferma evoluzione verso harness meno prescrittivi: il modello cresciuto rende la micro-gestione controproducente.

🔗 [raw/web/the-new-rules-of-context-engineering-for-claude-5-generation-models-claude-by-an/](../../raw/web/the-new-rules-of-context-engineering-for-claude-5-generation-models-claude-by-an/index.md)
