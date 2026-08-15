---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [harness, agent-client-protocol, acp, architecture, kiro, aws]
source_path: raw/web/one-agent-every-surface-how-we-built-the-kiro-agent-harness/index.md
ingested: 2026-W31 (Sat-Sat)
---

# One Agent, Every Surface: How We Built the Kiro Agent Harness

Liguori, Dura, Harris, Threlkeld (Kiro/AWS, Aug 2026). Kiro ha consolidato tre codebase di agent harness separati (IDE/TypeScript, CLI/Rust, web/Python) in un unico harness standalone.

## Decisione architetturale chiave

L'harness è un **processo server standalone**, non una libreria compilata nei client. Questo rende reale la separazione: client e harness non condividono linguaggio o runtime. Lo stesso harness gira su laptop o in cloud sandbox senza che il client se ne accorga.

## Agent Client Protocol (ACP)

ACP (1.0, Jun 2026) definisce il confine client-harness. Kiro lo estende a **Kiro-ACP**: 20+ metodi agent-callable, 15 client-callable, 20 notification types sotto il namespace `_kiro/`. Estensioni notevoli: live steering (messaggio iniettato al prossimo inference turn), spec-driven development come metodi dedicati, permission system multi-scope.

- Transport: stdio (locale) + WebSocket custom (remote/cloud)
- Trasporti diversi, stesso binary, stessi tool, stesso comportamento

## Permission model basato su Cedar

Capability-based: `fs_read`, `fs_write`, `shell`, `web_fetch`, `mcp`, `subagent`. Un deny su `fs_read` blocca ogni tool che legge file. Policies compongono across scope con deny-always-wins. L'agente non può modificare i propri file di permission.

## Payoff

Feature prima locked a un client ora ovunque: spec-driven development, custom agents (`.kiro/agents/`), hooks (`.kiro/hooks/`). Global hooks e policy presets spediti con zero client changes.

## Connessioni

Esempio industriale di [[wiki/pages/harness-design]] come ambiente separato dal client: il processo standalone realizza fisicamente la separazione WHAT (protocollo + intent) vs HOW (implementazione interna). Cedar come enforcement formale del back pressure. La live steering è un pattern complementare al loop: invece di aspettare la fine del turno, si inietta contesto (WHAT) a runtime.
