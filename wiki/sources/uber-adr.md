---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [agent-security, observability, benchmark, threat-detection, uber, mlsys2026]
source_path: raw/web/github-uber-adr-adr-secures-enterprise-ai-agents-through-observability-security-/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Uber ADR: Agentic AI Detection and Response

Uber (Li et al., MLSys 2026). Sistema enterprise di security per AI agent, deployed in produzione a Uber. Quattro capability: osservare, valutare difese, rilevare minacce, prevenire azioni unsafe.

## Componenti (open-source)

- **ADR Sensor**: cattura agent intent, tool use, execution trace da 7+ AI coding tool su macOS/Linux/Windows + agent customer-facing
- **ADR-Bench**: 300+ task, 133 MCP server, copertura di tutte le 17 agent attack technique
- **ADR Detection**: architettura two-tier, triage high-recall + ragionamento agentic più profondo per sessioni sospette
- **ADR Prevention**: non incluso nell'open-source release

## Architettura detection

Dual-agent detector: primo livello triage alto recall, secondo livello agentic reasoning per sessioni flagged. Infla benchmark packed → run detector → plot figure.

## Connessioni

Framework di osservabilità e security per agent che si inserisce nel filone [[wiki/pages/agent-failure-analysis]]: dove la failure analysis guarda ai fallimenti cognitivi/epistemici, ADR guarda alle minacce di sicurezza (prompt injection, credential exfiltration, lateral movement). ADR-Bench con 17 attack technique quantifica il lato avversario.
