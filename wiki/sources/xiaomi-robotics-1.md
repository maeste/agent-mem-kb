---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [robotics, embodied-ai, open-source, xiaomi, foundation-model, manipulation]
source_path: raw/web/xiaomi-open-sources-embodied-ai-foundation-model-xiaomi-robotics-1/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Xiaomi Open-Sources Embodied AI Foundation Model Xiaomi-Robotics-1

Nkosi (Inside AI, Aug 2026). Xiaomi rilascia open-source il foundation model embodied AI con pipeline completa da real-robot post-training a deployment.

## Dati training

- Pretrained su **100.000+ ore** di **UMI data** (Universal Manipulation Interface)
- Post-trained su **10.000+ ore** di cross-embodiment data
- Codice per benchmark evaluation incluso

## Posizionamento

Sfida gli approcci walled-garden (Figure AI, Tesla) allineandosi a filosofia open (LeRobot di Hugging Face). Copre sim-to-real transfer e multi-embodiment learning. Include GitHub repo, Hugging Face page, project website.

## Limiti

- Mancano dettagli su architettura, parameter count, benchmark specifici
- UMI data: rumoroso, limitato a tabletop task → potenziale vincolo a manipulation scenario ristretti
- L'open-sourcing non garantisce adozione: diversità hardware e safety concern rallentano l'uptake community in robotics

## Contesto

Google DeepMind RT-2 (non fully open) ha settato benchmark con web-scale vision-language data. Meta Habitat fornisce simulator robusti ma manca foundation model unificato. Xiaomi si posiziona come toolkit deployment-focused più che research benchmark leader. CyberOne (humanoid) come piattaforma hardware di riferimento.

## Connessioni

Espande il cluster robotics oltre [[wiki/sources/gemini-robotics-er-2|Gemini Robotics ER 2]] con un'opzione open-source. Cross-embodiment learning è l'equivalente robotics del transfer learning: la domanda se un modello trained on manipulation tabletop generalizzi a embodiment diversi è aperta.
