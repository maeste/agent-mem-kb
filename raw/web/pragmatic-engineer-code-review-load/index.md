# The Pulse: New trend - concern about massive increase in code review load

**Author:** Gergely Orosz (The Pragmatic Engineer)
**Date:** Jul 23, 2026
**URL:** https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-concern-about

---

Top of mind for engineering leaders: what to do about the growing code review load, and how devs are starting to review code less thoroughly than before? Many questions, but few proven solutions.

## Body

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics of a past The Pulse issue. Full subscribers received the article below a week ago.

One thing I am hearing that's top of mind for many engineering leaders is what is being done to deal with the continuous increase in code review load. It's been a topic for a while, and more such conversations seem to be taking place.

For me, it began in January, when Opus 4.5 and GPT 5.4 started to write more and better code at most companies. Around then, Director-level folks started talking about the bottleneck of building software moving from coding to the review phase.

There's been a boom in AI code review tools to deal with the increase in load since February, and an explosion of experimentation with and adoption of dedicated AI code review tools like CodeRabbit, Greptile, Qodo, SonarQube (now also Gitar). There's also tools offered by coding harnesses themselves like Claude Code review, Cursor review, GitHub Copilot review. And then tools previously not involved in code reviews, but which have context on the codebase, are also adding this, like Sentry's Seer AI reviews, Linear code reviews.

Larger companies are building in-house tools to improve the code review experience. Uber's Code Inbox is one case. Smart assignments are a feature inside Code Inbox for having reviews progress. Then there's Risk Profiles which estimate the impact of a change, and encourage devs to pay extra attention to risky ones.

It's not just Uber: companies like Cloudflare (AI Code Reviewer), Faire (Fairey), and HubSpot (Sidekick) and many others have also built tools to make their code review flows more fluid, after finding that an in-house implementation worked better than integrating a vendor.

Another approach is thinking about how to verify code, instead of reviewing. This is easier said than done; in theory, thorough testing should be able to verify that code works as expected. But how much testing is 'thorough'? What type of tests are we talking about? Integration and end-to-end as well? What about fuzz testing? Or formal methods? What about verifying that new tests exercise the functionality as expected? And how do we connect all of this with observability?

Too much thorough code review is burning out engineers, and resulting in sub-par code reviews. I hear a lot anecdotally that devs see others as no longer able to review code with intent, whereby, if the AI code review has no real comments, they just approve it. Meanwhile, those devs who put the same effort and energy into code review as before feel overloaded by AI slop PRs sent their way.

The problems exist, and the solutions feel more like experiments.
