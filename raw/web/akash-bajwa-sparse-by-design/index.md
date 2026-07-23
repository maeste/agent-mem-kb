Sparse By Design - Software Synthesis

[![Software Synthesis](https://substackcdn.com/image/fetch/$s_!69uV!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0283720-672c-4385-80ad-bf790da0c73c_500x500.png)](/)

# [![Software Synthesis](https://substackcdn.com/image/fetch/$s_!D5nM!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25999d36-dc71-4cb6-9eed-52297d74406a_1344x256.png)](/)

SubscribeSign in

# Sparse By Design

### Kimi K3 And Open Model Scaling

Jul 20, 2026

15

1

Share

*Join 8,000+ founders getting smarter on startup strategy*

Subscribe

* * *

When Moonshot publishes the Kimi K3 checkpoint on July 27th, it will be the largest open weights model ever released: 2.8 trillion parameters, a 1M token context window, native multimodality, and benchmarks that clear Opus 4.8 and sit roughly one generation behind Fable 5 and GPT-5.6.

The discourse has fixated on 2.8 trillion.

The more important number is 16.

## From 28% To 2%

K3 activates 16 of 896 experts per token — under 2% of its expert weights touched per forward pass. That is not an implementation detail. It is the terminal point (so far) of the most consistent architectural trend in open models.

[![](https://substackcdn.com/image/fetch/$s_!Mugo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F746df00d-2c0c-431b-976d-f1c74e770a1c_2436x1832.png)](https://substackcdn.com/image/fetch/$s_!Mugo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F746df00d-2c0c-431b-976d-f1c74e770a1c_2436x1832.png)

Total parameters have grown ~20x since Mixtral, and ~3x in the last twelve months alone. 

Active parameters have barely grown at all: a 17-49B band for 27 months. Moonshot shipped K2, K2.5 and K2.6 across nine months with the identical skeleton — 1T total, 32B active — three releases, **zero growth in active parameters.**

There is scatter (GLM-5.2 is *less* sparse than V4-Pro), so this is a trend with variance, not a law. But the direction is unambiguous: hold per-token compute roughly flat, inflate total capacity relentlessly.

Why? Because at a fixed training compute budget, more experts means lower loss. The model learns more from the same FLOPs. And the bill is paid in the one resource that has cheap tiers, storage, rather than the two that are scarce and rationed: compute and memory bandwidth.

The open source labs have discovered that the cheapest way to buy intelligence is to spend capacity.

Sparsity is partly an adaptation: when FLOPs are rationed, you scale the axis outside export controls. 

## KV Cache Compression

Even though expert weights are getting sparser, longer context windows grow the KV cache, and the cache is hauled from memory on every token, exactly like weights.

This is where the companion trend closes the loophole. Attention compression (DeepSeek’s CSA/HCA hybrid, Multi-head Latent Attention, K3’s new attention architecture) is collapsing the cache. V4-Pro’s KV cache at 1M context is **10%** the size of its predecessor’s.

Sparser experts shrink the weight-bytes moved per token. Compressed attention shrinks the cache-bytes moved per token. Nothing on the model roadmap shrinks the bytes *stored*. That number only goes up.

Every architectural trend points away from peak bandwidth scarcity and toward capacity as the binding constraint.

## Constraint moves from compute to storage

Sparsity is what makes a 2.8T model servable at all. As Jamin Ball from Altimeter [wrote](https://cloudedjudgement.substack.com/p/clouded-judgement-71026-own-your) about the true cost of serving frontier open models:

> *One force that historically factored into open model pricing (anyone can serve it) is much weaker when “anyone” means “anyone with a supernode and a serving stack tuned for a brand new attention architecture.”*

> *A 2.8T model probably has a structurally higher serving floor than a 1T model no matter is serving it. The K2-era 10x discount existed (partially) because those models were both smaller AND served at thin margins. K3 only gives you the second one. For two years “open” and “cheap” were used interchangeably, but they were never the same thing.*

Due to sparsity, per-token inference runs ought to run at the cost of a mid-size dense model. 

In that sense, sparsity has democratised the *compute* of frontier inference.

It has done nothing for capacity. At MXFP4, K3’s weights alone are ~1.4TB. Ten-plus H200s just to load them, before the KV cache on a 1M window - this is why Moonshot recommends supernode configurations “with 64 or more accelerators.”

Ever increasing sparsity moves the cost from compute to storage.

## Two Serving Regimes

A plausible scenario in low-batch environments (such as enterprises looking to self-host) would see a tiered memory approach (or memory hierarchies) with most frequently used experts stored in HBM whilst less frequently used experts would be in cheap DRAM. A sort of power law for MoE models.

This cost/efficiency gain disappears in hyperscale environemnts. A production server batches hundreds of concurrent requests, and each token picks its own 16 experts. Collectively, a full batch lights up most of the 896 every forward pass. There are no reliably cold experts. So frontier serving pools *everything* in rack-level HBM across 64+ accelerators and routes tokens to the chips holding their experts. In this regime, sparsity doesn’t reduce HBM purchased at all, it converts bandwidth demand into HBM *capacity* demand. More stacks, streamed less hard.

At low utilisation, a single power user, i.e. an enterprise with a handful of concurrent sessions, experts genuinely are cold, and tiering the model into system DRAM while hot-loading experts works. This is the regime that matters for open weights specifically, because the entire point of downloading a checkpoint is running it outside a hyperscaler. Sparsity is the only reason the self-hosting path exists at all for trillion-scale models.

**Routing is paramount.** Today’s routers spread tokens roughly uniformly across experts, which is why hot/cold tiering fails at scale. If labs train routers with deliberate locality, i.e. popular experts, predictable paths, true tiering becomes viable even at high batch, and the cheap-capacity DRAM camps win much bigger. 

* * *

15

1

Share

Previous

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Akash Bajwa · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture
