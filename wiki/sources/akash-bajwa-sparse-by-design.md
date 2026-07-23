---
type: source
created: 2026-07-23
updated: 2026-07-23
tags: [moe, sparsity, kimi-k3, inference, model-scaling, open-models]
source_path: raw/web/akash-bajwa-sparse-by-design/index.md
ingested: 2026-W30 (Sat-Sat)
---

# Sparse By Design: Kimi K3 And Open Model Scaling

**Author:** Akash Bajwa (Software Synthesis) | **Date:** Jul 20, 2026 | **URL:** https://www.akashbajwa.co/p/sparse-by-design

## Summary

Analysis of the sparsity trend in open-weight MoE models, centered on Kimi K3 (2.8T params, 896 experts, 16 active per token). The core insight: total parameters have grown ~20x since Mixtral, but **active parameters have barely moved** (17-49B band for 27+ months). Sparsity is the dominant architectural strategy in open models.

## Key Claims

### From 28% to 2%
- Mixtral activated ~28% of experts per token; K3 activates under 2% (16 of 896)
- Moonshot shipped K2, K2.5, K2.6 across 9 months with identical 1T total / 32B active skeleton: three releases, **zero growth in active parameters**
- Trend with variance: GLM-5.2 is actually *less* sparse than V4-Pro

### Why Sparsity
At fixed training compute budget, more experts means lower loss. The bill is paid in storage (cheap) rather than compute and memory bandwidth (scarce). Sparsity is partly adaptation: when FLOPs are rationed, scale the axis outside export controls.

### KV Cache Compression
Expert sparsity shrinks weight-bytes per token. Attention compression (DeepSeek CSA/HCA, MLA, K3 attention) shrinks cache-bytes per token. V4-Pro KV cache at 1M context is **10%** of its predecessor. Nothing shrinks bytes *stored*: that only goes up.

### Constraint Shift: Compute to Storage
- At MXFP4, K3 weights alone are ~1.4TB: 10+ H200s just to load, before KV cache
- Moonshot recommends 64+ accelerator supernode configurations
- At low batch (enterprise self-hosting): experts genuinely cold, tiering to DRAM viable
- At hyperscale batch: full batch lights up most experts every pass, no cold experts, sparsity doesn't reduce HBM purchased

### Routing as Bottleneck
Today's routers spread tokens uniformly, defeating hot/cold tiering at scale. Deliberate expert locality in routing could make tiering viable even at high batch.
