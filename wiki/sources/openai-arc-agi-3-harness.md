---
type: source
source_path: raw/web/how-enabling-two-settings-tripled-our-scores-on-the-arc-agi-3-benchmark/index.md
ingested: 2026-W30 (Sat-Sat)
created: 2026-08-01
updated: 2026-08-01
tags: [arc-agi-3, harness-design, context-management, evals, openai, reasoning-retention]
---

# ARC-AGI-3: due impostazioni, 3x score

OpenAI (2026-07-29). GPT-5.6 Sol passa dal 13.3% al 38.3% su ARC-AGI-3 abilitando due impostazioni dell'harness: retained reasoning + compaction. Output token ridotti 6x.

## Punti chiave

- **L'harness è la variabile misurata, non solo il modello**: ARC usa un harness generic intenzionalmente (no tools, no features) per rendere i confronti equi e le mancanze del modello visibili. OpenAI scopre che la bassa performance era attribuibile a scelte dell'harness, non al modello.
- **Retained reasoning**: l'harness ARC scartava dopo ogni azione tutto il ragionamento privato. Il modello doveva re-interpretare il gioco da zero ogni turno. Mantenendo i pensieri precedenti, pensa meno per azione e impara strategie coerenti nel tempo.
- **Compaction vs rolling truncation**: ARC tronca i messaggi oltre 175K char (FIFO). Compaction (Responses API) rimpiazza con summary strutturato: preserva ciò che è imparato su ogni gioco attraverso run lunghi, score più alto con meno token.
- **Evals come bundle**: "evals raramente misurano modelli isolati — misurano un pacchetto di scelte meno visibili: API settings, harness design, prompting". Raccomandazione: confrontare modelli solo con settings che matchano l'uso reale (ChatGPT/Codex).

## Collocazione nel vault

Evidenza diretta per [[wiki/pages/harness-design]]: il punteggio di un modello è funzione dell'harness tanto quanto del modello. Collega a [[wiki/pages/memory-skills-co-evolution]]: retained reasoning è una forma di memoria cognitiva cross-turn, compaction è memory management. Conferma empiricamente la tesi harness-centrica già presente nel vault.

🔗 [raw/web/how-enabling-two-settings-tripled-our-scores-on-the-arc-agi-3-benchmark/](../../raw/web/how-enabling-two-settings-tripled-our-scores-on-the-arc-agi-3-benchmark/index.md)
