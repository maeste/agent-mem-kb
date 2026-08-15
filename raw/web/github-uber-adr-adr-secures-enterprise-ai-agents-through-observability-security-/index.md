---
source_url: https://github.com/uber/ADR
title: "GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber."
author: Uber
published: 2026-04-19
fetched: 2026-08-07
---

# GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber.

---
title: "GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber."
author: Uber
url: https://github.com/uber/ADR
hostname: github.com
description: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. - uber/ADR
sitename: GitHub
date: "2026-04-19"
categories: ['repository:1215280164']
---
ADR (Agentic AI Detection and Response) is an enterprise security system for AI agents. It helps organizations secure employee-facing agents such as Cursor, Claude Code, and Codex, as well as customer-facing agents such as AI support agents.

ADR is **deployed in production at Uber**, and the accompanying paper was accepted to **MLSys 2026**: [Paper PDF](https://github.com/uber/ADR/blob/main/docs/adr-paper.pdf) · [Slides PDF](https://github.com/uber/ADR/blob/main/docs/adr-mlsys-2026-slides.pdf)

ADR secures enterprise AI agents through four complementary capabilities: observing agent activity, evaluating defenses, detecting threats, and preventing unsafe actions.

1. **ADR Observability: Understand what AI agents are doing and why.** In production, ADR captures agent intent, tool use, and execution traces across 7+ AI coding tools on macOS, Linux, and Windows, as well as internal automation and customer-facing support agents.
2. **ADR Benchmark: Test agent security under realistic enterprise conditions.** ADR-Bench includes 300+ tasks, 133 MCP servers, and coverage of all 17 agent attack techniques.
3. **ADR Detection: Detect risky agent behavior efficiently.** Its two-tier architecture combines high-recall triage with deeper agentic reasoning for suspicious sessions.
4. **ADR Prevention: Stop unsafe actions before they cause harm.** This component is not included in the current open-source release.**Stay tuned.**

This repository contains the open-source **ADR Sensor**, **ADR-Bench**, and **ADR Detector** described in the paper. The offline **ADR Explorer** engine, which hardens ADR Detection through pre-deployment red teaming, is not included here.

| Path | ADR component | Description | 
|---|---|---|
| [Sensor/](https://github.com/uber/ADR/blob/main/Sensor) | ADR Observability | Collect and normalize agent telemetry from Claude Code, Cursor, Codex, and others | 
| [Detection/](https://github.com/uber/ADR/blob/main/Detection) | ADR Benchmark + Detection | Dual-agent detector, 133 MCP servers, 303 benchmark tasks, baselines, figure scripts | 
| [docs/REPRODUCIBILITY.md](https://github.com/uber/ADR/blob/main/docs/REPRODUCIBILITY.md) | Evaluation | Step-by-step workflow to reproduce benchmark detection and paper figures | 

```
git clone https://github.com/uber/ADR
cd ADR/Detection
uv sync
export ANTHROPIC_API_KEY="..." OPENAI_API_KEY="..."
```
Default detector is `adr` (ADR dual-agent). For keyless smoke tests, use `--detector llamafirewall` (see [Detection/README.md](https://github.com/uber/ADR/blob/main/Detection/README.md)).

See **[docs/REPRODUCIBILITY.md](https://github.com/uber/ADR/blob/main/docs/REPRODUCIBILITY.md)** for the full evaluation workflow (inflate packed benchmark → run detectors → plot figures).

Component documentation:

- [Sensor/README.md](https://github.com/uber/ADR/blob/main/Sensor/README.md) : telemetry collection and unified schema
- [Detection/README.md](https://github.com/uber/ADR/blob/main/Detection/README.md) : ADR-Bench, detector baselines, MCP infrastructure

```
@inproceedings{li2026adr,
  title={ADR: An Agentic Detection System for Enterprise Agentic AI Security},
  author={Li, Chenning and Hu, Pan and Xu, Justin and Ozbas, Baris and Liu, Olivia and Van, Caroline and Li, Manxue and Zhou, Wei and Alizadeh, Mohammad and Zhang, Pengyu and Sriramadhesikan, KK and Zhang, Ming},
  booktitle={Proceedings of the Ninth Conference on Machine Learning and Systems},
  year={2026}
}
```
Or use [CITATION.cff](https://github.com/uber/ADR/blob/main/CITATION.cff).

Apache License 2.0. See [LICENSE](https://github.com/uber/ADR/blob/main/LICENSE). `Detection/benchmark/agentdojo/` is vendored third-party code under its own [LICENSE](https://github.com/uber/ADR/blob/main/Detection/benchmark/agentdojo/LICENSE) (MIT).

`Detection/` includes **synthetic** benchmark fixtures (fake credentials, emulated environments, prompt-injection scenarios) for defensive security research only. Details: [docs/OPEN_SOURCE_REVIEW.md](https://github.com/uber/ADR/blob/main/docs/OPEN_SOURCE_REVIEW.md).
