---
source_url: https://kaitchup.substack.com/p/agentic-ai-at-two-different-scales?utm_source=tldrai
title: "Agentic AI at Two Different Scales: Nanbeige4.2-3B and Laguna S2.1"
author: Benjamin Marie
published: 2026-07-25
fetched: 2026-08-03
---

# Agentic AI at Two Different Scales: Nanbeige4.2-3B and Laguna S2.1

---
title: "Agentic AI at Two Different Scales: Nanbeige4.2-3B and Laguna S2.1"
author: Benjamin Marie
url: https://kaitchup.substack.com/p/agentic-ai-at-two-different-scales
hostname: substack.com
description: "The Weekly Kaitchup #152"
sitename: The Kaitchup – AI on a Budget
date: "2026-07-25"
---
In this edition of The Weekly Kaitchup, I’m looking at two of the week’s most interesting releases for agentic workloads: Nanbeige4.2-3B and Laguna S 2.1.

The Kaitchup – AI on a Budget is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Agentic workloads include multi-step reasoning, tool use, interaction with external environments, and tasks that may require many actions before completion.

Despite this shared focus, they operate at very different scales.

Nanbeige4.2-3B is a compact dense model with approximately 4 billion total parameters and 3 billion non-embedding parameters. It is intended to make capable agentic behavior practical on consumer and workstation hardware.

Laguna S 2.1 is a 118-billion-parameter Mixture-of-Experts (MoE) model. It activates approximately 8 billion parameters for each token.

The two models represent different approaches to agentic AI. Nanbeige uses repeated computation over a relatively small set of weights, while Laguna uses sparse access to a much larger pool of learned parameters.

Nanbeige4.2-3B

While Nanbeige4.1 used a basic Llama architecture, Nanbeige4.2-3B uses a Looped Transformer.

Instead of containing a large number of unique transformer layers, the model has 22 physical decoder layers that are executed twice. The same weights are reused during the second pass, giving the model the computational depth of approximately 44 layer executions without storing 44 independent layers.

This design reduces weight memory, but it does not reduce inference computation to that of a normal 22-layer model. Each token must still pass through the transformer stack twice.

The model has 48 attention heads with a dimension of 128, and eight key/value heads. This is a lot. For instance, Qwen3.6 35B A3B has only two KV heads.

Looping introduces a further memory consideration. Unless the implementation explicitly shares KV-cache state between the two passes, each loop may require separate key/value entries. Nanbeige’s default configuration does not appear to enable loop-level KV sharing.

Moreover, I think models using the Looped Transformer should be better named. When you use a 3B model, you don’t expect it to be nearly as slow as a 6B model. small MoE models, like Qwen3.6 and Gemma 4, show the number of active parameters in their name, like 26B-A4B. For Looped Transformers, we should adopt a similar convention, like 3B-2P (for “2 passes”), for instance.

Nanbeige4.2-3B’s memory consumption

A 16GB GPU should be able to run the model, without quantization, at moderate context lengths with careful settings. A 24GB GPU provides more room for longer prompts, greater concurrency, and runtime overhead.

Based on the model’s 22 physical layers, two loop passes, eight key/value heads, 128-dimensional heads, and BF16 KV values, a conservative estimate places KV-cache consumption at approximately 176 KiB per cached token for each active sequence.

I show in the following article how to estimate the KV cache memory consumption:

At 16K tokens, this would require roughly 2.75 GiB of KV-cache memory. Using the complete 256K context could require roughly 44 GiB of KV-cache memory for a single active sequence.

This is very large. Almost twice as much as what Qwen3.6 27B would consume for the same context length.

Using Nanbeige4.2-3B with vLLM

At release, Nanbeige provided a dedicated vLLM branch for the model:

The model can then be served through vLLM’s OpenAI-compatible API:

vllm serve Nanbeige/Nanbeige4.2-3B \
--host 0.0.0.0 \
--port 8000 \
--enable-auto-tool-choice \
--tool-call-parser nanbeige \
--reasoning-parser nanbeige
#use --host 127.0.0.1 if you are running it locally

The reasoning and tool-call parsers are important for agent frameworks. They allow vLLM to separate reasoning content and structured tool calls from ordinary assistant text.

Nanbeige’s chat template exposes two controls.

The enable_thinking option determines whether the current response contains an explicit reasoning phase. The preserve_thinking option determines whether reasoning content from previous assistant turns remains in the conversation history.

For normal chat and question answering, preserved reasoning can usually be disabled. For multi-turn tool use, office workflows, and coding agents, the developers recommend retaining earlier reasoning content but I don’t understand how this can work well. Reasoning traces can be very long, like 50K+ tokens. Keeping them in the context, even if it’s just one, means that the model may reach its max context length at next turn.

Performance

According to the published evaluation, Nanbeige exceeded Qwen3.5-9B on most of the included agent, coding, and reasoning tasks. It also surpassed Gemma 4 12B on benchmarks including GDPval, SWE-Bench Verified, SWE-Bench Pro, and Terminal-Bench 2.0.

Agent results are influenced not only by the base model but also by the allowed reasoning budget, tool definitions, prompting strategy, conversation-state handling, retry policy, and maximum number of actions.

Laguna S 2.1 is a much larger coding-focused MoE model.

It contains 118 billion total parameters but activates approximately 8 billion parameters for each token. A routing mechanism selects a subset of experts during inference, allowing the model to access a large learned parameter pool without executing every parameter for every token.

Laguna contains 48 transformer layers. Twelve use global attention, while the remaining 36 use sliding-window attention with a window of 512 tokens. The global and local layers are interleaved in approximately a one-to-three ratio.

The global layers allow information to move across the complete input context. The sliding-window layers restrict attention to nearby tokens, reducing the cost of long-context inference and limiting KV-cache growth.

The model contains 256 routed experts and one shared expert. For each token, the router selects the top ten routed experts in addition to the shared computation.

Laguna also uses per-head softplus output gating.

Per-head softplus output gating gives each attention head its own learned volume control. For every token, the model can reduce, preserve, or amplify the contribution of individual heads before combining their outputs. The softplus function keeps these gates positive while allowing values above one, so useful attention heads can be strengthened rather than merely switched on or off.

It uses interleaved reasoning. The model can reason, issue a tool call, receive the tool result, and resume its reasoning before selecting another action.

Poolside also provides a DFlash draft model for speculative decoding. These models generate candidate tokens that the main model can verify in parallel, potentially increasing output speed.

For coding-agent workloads, Poolside also recommends retaining prior reasoning_content in the conversation history.

As for the memory consumption of the KV cache, 256K tokens should consume around 24 GB.

Target tasks

Laguna S 2.1 is more specialized than Nanbeige.

Its primary target is long-horizon software engineering. This includes repository-level bug fixing, terminal interaction, shell-based workflows, multilingual code maintenance, codebase exploration, and answering questions that require understanding large software repositories.

Performance

Laguna’s sparse architecture and coding-focused training are particularly effective for terminal interaction, repository-level reasoning, and multilingual software engineering.

It looks like a very good model but so far, I have found community feedback to be mixed.

I’ll spend some time with Nanbeige and Laguna. If everything goes well, I’ll probably write an article using them for agentic coding.

A $50 Coupon to Try Verda’s GPUs

In collaboration with Verda, I’m sharing a $50 coupon that you can redeem in your Verda account, after provisionning your account with $5, to try their GPUs (B200, B300, RTX Pro 6000, …).

Note: I share this coupon because I really think it’s a good deal. I don’t receive any form of compensation from Verda, or any usage information, related to this coupon. Verda also provides compute sponsorship for some of my articles.

That’s all for this week.

If you like reading The Kaitchup, consider sharing it with friends and coworkers (there is a 20% discount for group subscriptions):

I haven't gotten very good results with any Laguna model. I ran Laguna S 2.1 on DeepSWE and it didn't even achieve a fraction of the claimed bench. It was then released they changed parameters of the benchmark to 6 hours per task, among other things. Also claim it only performs like that in their pool harness, not the DeepSWE default. Their pool harness isn't open source so who knows what is happening in their to achieve the score, but i have been told by someone who looked at the binary there is a hidden advisor feature in there to call a smarter model that is not in the public documentation of the pool harness. maybe that's just for RL training or maybe that explains the score.

Waiting your post about comparing Laguna S 2.1 with other models in similar size, Trust me bro benchmarks are nothing compared to your ones )

Thanks.

I haven't gotten very good results with any Laguna model. I ran Laguna S 2.1 on DeepSWE and it didn't even achieve a fraction of the claimed bench. It was then released they changed parameters of the benchmark to 6 hours per task, among other things. Also claim it only performs like that in their pool harness, not the DeepSWE default. Their pool harness isn't open source so who knows what is happening in their to achieve the score, but i have been told by someone who looked at the binary there is a hidden advisor feature in there to call a smarter model that is not in the public documentation of the pool harness. maybe that's just for RL training or maybe that explains the score.
