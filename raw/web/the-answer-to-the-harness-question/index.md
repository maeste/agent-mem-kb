---
source_url: https://danielmiessler.com/blog/the-answer-to-the-harness-question
title: The Answer to the Harness Question
published: 2019-03-13
fetched: 2026-08-01
---

# The Answer to the Harness Question

---
title: The Answer to the Harness Question
url: https://danielmiessler.com/blog/the-answer-to-the-harness-question
hostname: danielmiessler.com
description: Harnesses are for intent; models are for execution
sitename: Danielmiessler
date: 2019-03-13
---
![The Answer to the Harness Question](assets/65ae5e52007e.webp)


Martin Casado posted something about AI harnesses that captures where a lot of smart people are stuck right now.

On harnesses, I vacillate between three beliefs: the less harness, the better. Models are the magic. Post training a model and harness is dramatically better and the model providers win. Harnesses have real independent value from the model. I have no idea which is right.[Martin Casado](https://x.com/martin_casado/status/2082527395920347362)

I think I can answer this.

The reason the question feels impossible is that we're treating the harness as one thing. It's actually two. Every harness carries some mix of WHAT and HOW—context about what you want, and instructions for how to get it. And those two halves age in opposite directions.

The HOW half rots. This is [Sutton's Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) playing out in your config files: the smarter models get, the dumber your step-by-step instructions look by comparison. If your harness is mostly HOW, then Martin's first belief is correct. Less harness is better, because the model is the magic.

The WHAT half appreciates. Who you are, what you're working on, what you're trying to accomplish, and what good looks like to you. A smarter model does more with that context, not less. If your harness is mostly WHAT, then his third belief is correct. It has real independent value, and that value grows with every model release.

So beliefs one and three are both right. They're just about different halves of the harness.

The second belief—that model providers post-train the harness into the model and win—is right about execution and wrong about intent. The labs can absolutely train models to be better agents, and they will. But they can't post-train YOUR context into the model. What you're trying to build, for whom, with your constraints and your taste. That has to be captured and conveyed from outside, every single time.

That's what the harness is for. I've been calling this [Intent Engineering](https://danielmiessler.com/blog/intent-engineering), and it's the whole design principle behind [my own harness](https://danielmiessler.com/blog/personal-ai-infrastructure): capture what the human actually wants, convey it to the model on every task, and otherwise stay out of the way.

So YES to harness. Extremely powerful. But for your context, while staying out of the way of the model for execution.

Martin's original post is [here](https://x.com/martin_casado/status/2082527395920347362), and my reply that this post expands on is [here](https://x.com/DanielMiessler/status/2082627476426273280).

I wrote about the WHAT vs. HOW distinction for prompts in [From Prompt Engineering to Intent Engineering](https://danielmiessler.com/blog/intent-engineering), and for harnesses in [Good and Bad Harness Engineering](https://danielmiessler.com/blog/good-and-bad-harness-engineering). This post is the same idea applied to the "do harnesses even matter" debate.

Citation: Richard Sutton, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.

🤖 **AIL 3:** I (Kai, Daniel's AI assistant) drafted this post from Daniel's X reply to Martin Casado, which provided the full structure and core argument, plus his prior published posts on the topic. Daniel's original words carry the thesis. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).
