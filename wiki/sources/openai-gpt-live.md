---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [voice-ai, realtime, architecture, openai, gpt-live, system-design]
source_path: raw/web/how-we-built-a-realtime-system-for-responsive-voice-ai-in-six-months/index.md
ingested: 2026-W31 (Sat-Sat)
---

# GPT-Live: How We Built a Realtime System for Responsive Voice AI in Six Months

Uberti, Malkani (OpenAI, Aug 2026). GPT-Live è il sistema voice di terza generazione: modello full-duplex (ascolta e parla simultaneamente) senza turn detector. Può delegare a modelli frontier (GPT-5.5) per reasoning profondo senza interrompere il flusso.

## Principio: the voice must flow

Separazione netta tra **media path** (audio in/out, fast path) e **application logic** (delegation, tool use, async RPC boundary). Un tool call lento ritarda il proprio risultato ma non può stallare il flusso media.

## Decisioni ingegneristiche

- **Go** per media frontend e inference logic (sostituisce Python asyncio): p95 del nuovo = p50 del vecchio
- **WebRTC** come transport foundation; sviluppato **WARP** (WebRTC Abridged Roundtrip Protocol): 6 round trip → 1
- **Stateful inference**: handoff seamless tra istanze modello (warm replacement + parallel inference + cutover)
- **Dynamic context compaction** come transizione gestita: compact in background mentre l'istanza originale continua a chattare, switch senza interruzione
- **Delegation**: frontier model pre-warmed e prefilled a inizio sessione, session affinity stabile, prompt caching
- **Instant Connect**: SDP pre-negotiated, session materializzata al primo pacchetto media

## Lezioni operative

- Capacità ≠ GPU throughput: CPU-side stream handler, queue e network path scalano con le sessioni
- Geografia first-order: routing a capacity distante aggiunge delay a più punti
- Session lifecycle lunghi espongono memory/persistence pressure; reconnect esercitano compaction; disconnect rivelano race nello shutdown

## Connessioni

Architettura di sistema che separa clean boundary tra live path (WHAT: l'esperienza conversazionale) e async path (HOW: tool, delegation, logging). La compaction come transizione gestita parallela è una strategia diversa da [[wiki/pages/harness-design|harness tradizionali]] dove la compaction blocca.
