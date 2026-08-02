---
source_url: https://x.com/Vtrivedy10/status/2079976006644072796
title: @Vtrivedy10 — X thread 2079976006644072796
author: Vtrivedy10
published: Wed Jul 22 17:04:58 +0000 2026
likes: 696
retweets: 66
fetched: 2026-07-25
fetched_via: opencli
---

# @Vtrivedy10 — X thread (2079976006644072796)

https://t.co/Eb1h1RFPie


---

**@EnglessonElias** (reply):

@Vtrivedy10 Interviewing the user instead of oneshot eval gen feels like the key design choice.

When you tested on chat-langchain, what did users usually push back on first the eval directions, the live-vs-simulated tools, or the verifier?

Curious which of those ate the most iteration.


---

**@rohit9m** (reply):

@Vtrivedy10 Very cool. If the same model + context writes both task and verifier, how do you know that the verifier is right "at birth" and stays right as the agent evolves? Do you have some sort of calibration step against known-good and known-bad traces?


---

**@aurielws** (reply):

@Vtrivedy10 @himanshutwtxs Oh nice I think I’ll be needing this soon thanks!


---

**@Vtrivedy10** (reply):

@aurielws @himanshutwtxs love it, would love to incorporate anything you’re using it for if you end up having any feedback!


---

**@kn_neeraj1** (reply):

@Vtrivedy10 Why harbor framework?


---

**@FanofAITech** (reply):

@Vtrivedy10 Evals are training data for agents.


---

**@pro_kamath** (reply):

@Vtrivedy10 Looks like - will use this right away- is this compatible with Langfuse traces as well?


---

**@michaelcapizzi** (reply):

@Vtrivedy10 @hwchase17 @Vtrivedy10 how do you handle multi-turn scenarios?  I have a custom skill that I want to evaluate (using harbor) but that skill is like the one you describe here: it interviews the user.  That’s not a single turn that I can evaluate.  🤔


---

**@Vtrivedy10** (reply):

@michaelcapizzi @hwchase17 simulated users of pre-spec’d responses, will be adding to the skill thx for the note!


---

**@samirdamle** (reply):

@Vtrivedy10 @grok 10 key points please


---

**@xsmotsenigos** (reply):

@Vtrivedy10 I really like the idea.   I have been approaching the issue a different way, but I will try your skill, perhaps in concert to see what surfaces.  Thank you.


---

**@TheVidhate** (reply):

@Vtrivedy10 @hwchase17 V cool! I put out a similar thing a couple months back :)

https://t.co/8uCUMuhHLl


---

**@davefobare** (reply):

@Vtrivedy10 @hwchase17 “point to agent to a set of traces if available, and start with a simple prompt:”

Looks like there is meant to be a sample prompt after this.


---

**@Vtrivedy10** (reply):

@davefobare @hwchase17 this is a good start
“””
Use the eval-engineering skill to create an eval with me. Inspect the agent first, propose a few abilities worth testing, recommend one and then we can build it together”””


---

**@davefobare** (reply):

@Vtrivedy10 @hwchase17 Thank you!


---

**@Dandiggastech** (reply):

@Vtrivedy10 I’ve created my own eval engineering skill, however it will be good to try this out! Thanks @LangChain


---

**@mattlam_** (reply):

@Vtrivedy10 very cool building out a similar thing in OpenBench, hopefully can just use your guy's skill.

will be interested to hear what else you guys want to build in an eval framework?


---

**@Vtrivedy10** (reply):

awesome, would love feedback as you do, will be actively extending this set of skills!

a ton!  some stuff currently in testing:
- faithfully simulating users in environments using traces to calibrate (comes up in many agent tasks)

- better synthetic data generation for creating an environment, basically collecting more data on how to structure simulated data such that eval env and prod env aren’t too diverged


---

**@mattlam_** (reply):

@Vtrivedy10 dm'ed, sounds interesting


---

**@htahir111** (reply):

@Vtrivedy10 V cool btw! Love this


---

**@htahir111** (reply):

Interesting choice with the Harbor format. We've been wondering what the standard format will be and Harbor is emerging fast as a leader but I'm a big of @willccbb and the world at Prime Intellect. It would be cool if Prime and Harbor guys can get together and standardize this so we all can export to one standard eval / environment format


---

**@Vtrivedy10** (reply):

@htahir111 @willccbb love harbor format and of course everything prime for DX!  PI has an integration with harbor, will prob add reference in the skill later for common providers - more coming on extending this to the “what next” which includes post-training

pic from their latest verifiers v1 blog https://t.co/3GRqOWyIoX


---

**@GitMaxd** (reply):

@Vtrivedy10 Thanks Viv!  The Eval structure looks very familiar 🚀


---

**@Vtrivedy10** (reply):

@GitMaxd yeah haha we’re big fans of Harbor format!  also forces us humans to explicitly interact with both task and verifier design -&gt; verifier design is hard :)


---

**@GitMaxd** (reply):

@Vtrivedy10 Just used Harbor for the first time over the weekend, I’m sold

It’s changed the way I think about agent development


---

**@novasarc01** (reply):

@Vtrivedy10 another attempt to automate my man @xeophon


---

**@Vtrivedy10** (reply):

@novasarc01 @xeophon impossible https://t.co/9JT1cJagu8


---

**@ASTxRTYS** (reply):

@Vtrivedy10 the long awaited
