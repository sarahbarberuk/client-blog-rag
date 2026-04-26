---
title: Understanding AI by its building blocks: An interactive breakdown of a prompt
url: https://www.contentful.com/blog/understanding-ai-building-blocks-anatomy-prompt/
---

Blog
/
Guides
/
Understanding AI by its building blocks: An interactive breakdown of a prompt
Understanding AI by its building blocks: An interactive breakdown of a prompt
Published on February 26, 2026
Written by
Scott Rouse
Senior Product Architect - Internal Tools
,
Contentful
On this page
The prompt as the primitive
Tokens: How the model actually sees text
Building a prompt from nothing
Why prompts don’t persist
The hidden prompt stack
Beyond free-form text
Tools as constrained actions
Putting it all together
Designing around the call
Inspiration for your inbox
Subscribe and stay up-to-date on best practices for delivering modern digital experiences.
TL;DR
powered by AI Actions
This post explains how AI systems work by examining the fundamental unit of interaction: a single prompt sent to a language model.
Language models process text as tokens rather than words, have no memory between calls, and only see the exact text included in each request—meaning reliability depends entirely on what context is provided every time
The prompt a user writes is often combined with hidden system instructions, formatting rules, and dynamically retrieved content that the model cannot distinguish from user input, making prompt ordering and context assembly critical
Structured outputs and tools constrain probabilistic text generation into predictable formats that software can validate and act upon, forming the foundation for building reliable AI systems around an inherently stateless primitive
AI systems often feel impressive but unreliable. You’ll see moments where a response feels thoughtful and well reasoned, followed by answers that are vague, inconsistent, or hard to reproduce. When that happens, it’s tempting to assume the Large Language Model (LLM) is the problem—that you need a newer version, more parameters, or a different provider.
More often, the issue isn’t intelligence at all. It’s context.
This interactive article is the first in a two-part series that looks at modern AI systems from the inside out. We’ll start at the smallest meaningful unit: a single AI call. Each section includes a live module you can run and modify to see how output changes.
By understanding what actually happens in that call—and what
doesn’t
—you can explain the most surprising model behaviors. That mental model sets the foundation for
Part 2
, where we’ll zoom out and examine the ecosystem built around this primitive.
The prompt as the primitive
No matter how sophisticated an AI product appears, everything eventually reduces to the same operation: text goes in, something comes out. That single request to a model is the primitive unit of modern AI systems.
This can be difficult to internalize because most products deliberately hide it. Chat interfaces feel conversational. Developer tools feel stateful. Applications appear to remember what just happened. But none of that continuity exists inside the model itself.
From the model’s perspective, there is no app, no workflow, and no conversation. There is only the text included in the current call. Everything else—memory, guardrails, tools, and formatting—is supplied by systems outside the model.
Once you accept this constraint, many confusing behaviors stop feeling mysterious. Next, let’s take a look at what the model actually receives when you type out a prompt. That starts with tokens.
Tokens: How the model actually sees text
Before a model can respond, it breaks all input into tokens. Tokens are not words in the human sense. They are fragments of characters shaped by frequency and training data.
This detail is important because it exposes a fundamental mismatch between human intuition and model behavior. Where you see meaning and intent, the model initially sees reusable text fragments and patterns of co-occurrence.
A single word may be split into multiple tokens, while a common phrase may collapse into fewer. This segmentation is mechanical, not semantic. The model doesn’t start from understanding and works forward. It starts from tokens and predicts what is likely to come next.
This doesn’t make models ineffective, but it does mean expectations need to be calibrated. Apparent misunderstandings are often a consequence of representation, not a failure to “think.”
Building a prompt from nothing
Now that we’ve seen how text is broken into tokens, we can build up a prompt from the simplest possible starting point. We’ll begin with a broad request and then add context to see exactly what changes—and what doesn’t.
Consider a simple prompt on a broad topic, such as asking how to help the environment. The response is usually sensible but generic: familiar suggestions, high-level advice, and little specificity.
This outcome is not a failure. It reflects exactly what the model has to work with. In the absence of additional information, it draws from widely represented patterns in its training data and produces a statistically plausible answer.
The important lesson here is not that the prompt was poorly written. It’s that the model had no reason to be specific. Without context, the safest response is a general one.
This is also why small wording changes often fail to meaningfully improve results. If the underlying information hasn’t changed, the output usually won’t either.
What reliably improves output quality is relevant context. When you add details—your location, your role, your constraints, or your goal—the model’s response becomes more concrete and actionable.
That’s because the “real input” is not the cleverness of the question. It’s the total set of information the model receives in the call. If the call includes only a broad request, the model will stay broad. If the call includes the constraints that matter, it can narrow down to what’s actually useful.
Why prompts don’t persist
Another common source of confusion is memory. Large language models do not retain information between calls. Each request is processed as if it were the first one.
When products feel conversational, that continuity is created by surrounding systems that store prior messages and re-inject them into subsequent calls. If part of that history is missing, the model has no way to notice. It will still respond confidently, even if crucial context has been dropped.
This statelessness is a design constraint, not a flaw. It enables scale and predictability at the infrastructure level. But it also means reliability depends entirely on what context is supplied every time.
The hidden prompt stack
The prompt you write is rarely the only text the model sees. Applications often inject additional instructions before or after user input: system messages, safety policies, formatting rules, or dynamically retrieved content.
These layers can help, but they can also conflict. Critically, the model has no reliable way to distinguish which text came from you and which was added automatically. Everything is treated as a single sequence.
This matters because in production systems, some of the most important context is assembled outside the user’s prompt: account data, recent activity, retrieved documents, product rules, or internal knowledge. From the model’s point of view, none of that distinction is relevant. It only “sees” what is included in the call.
Order is prioritized over intent. Instructions that appear later in the input often override earlier ones, even when that wasn’t the goal. This is why prompts that look correct can still fail in practice.
Seen this way, prompt quality is often a systems problem. The hard part isn’t phrasing a clever question. It’s deciding what information matters right now, gathering it, and sequencing it correctly in the input—without accidentally introducing conflicting instructions elsewhere in the stack.
Understanding the hidden prompt stack is essential for diagnosing unexpected behavior. When outputs don’t align with expectations, the problem is often invisible context rather than the visible prompt itself.
Beyond free-form text
Free-form text works well for explanation and exploration, but it breaks down when AI output needs to be consumed by software. Databases, APIs, and workflows require predictable structure.
Structured output addresses this by constraining responses into defined shapes, such as JSON. This doesn’t make the model more intelligent. It makes the output easier for software to validate and act on.
Structure creates a boundary between probabilistic generation and deterministic systems. On its own, it doesn’t guarantee correctness—but it makes integration possible.
Tools as constrained actions
Tools extend the same idea. A tool defines an allowed action with a known input shape and a specific purpose, such as fetching data or triggering a process. The model does not execute the action itself. It produces a structured description of what should happen.
At this level, tools are vocabulary. They give the model a way to express intent in a form that software can interpret. Everything that follows—execution, validation, retries, and side effects—remains outside the model.
Putting it all together
By this point, the individual pieces should feel familiar: tokens are the raw units the model receives, prompts don’t persist between calls, hidden instructions can shift outcomes, and structure plus tools are how software turns probabilistic text into something it can safely act on.
This final module combines those building blocks into a single place to experiment. Instead of changing one variable at a time, you can see how the same call behaves when you adjust the parts that actually matter: what text is included, where instructions are placed, whether output is constrained, and whether the model is allowed to request an action through a tool.
A useful way to use this is to work in passes. Start with the simplest version of the prompt and run it once. Then add one layer at a time: first a bit of context that makes the request concrete, then a constraint that forces the response into a predictable shape, and finally a tool that can fill in a missing piece of information. Each step should make the result more usable—not because the model is “smarter,” but because the call is better designed.
You can also flip the experiment around and intentionally break it. Move instructions earlier or later. Add a conflicting line above the user prompt. Relax the output format and watch how quickly responses become harder for software to consume. The point isn’t to memorize tricks. It’s to internalize a mental model: reliability emerges from how you assemble and constrain a single call.
Designing around the call
Every limitation we’ve explored traces back to the same place: a single AI call with limited context, no memory, and no awareness of its surroundings. The more predictable you want outcomes to be, the more deliberately that call must be designed.
This is why modern AI systems look the way they do. Structured responses, retrieval mechanisms, orchestration layers, and agents don’t exist to make models smarter. They exist to compensate for these constraints.
Now that we understand the anatomy of a single prompt, we can step back and look at what’s been built around it. In
Part 2
, we’ll examine how these constraints give rise to the AI ecosystem—and why most progress comes from better system design, not better wording.
Take a tour
Chat with our team
Your experiences should wow, not wait. Let's talk.
Inspiration for your inbox
Subscribe and stay up-to-date on best practices for delivering modern digital experiences.
Artificial intelligence
Copy Page Url
Linkedin
Facebook
Twitter
Meet the authors
Scott
Rouse
Senior Product Architect - Internal Tools
Contentful
Scott is a Senior Product Architect - Internal Tools at Contentful, based in Madison, WI. He specializes in telling the story of Contentful through a blend of design and development expertise, with a particular focus on design systems. His extensive experience spans across sectors from startups to heavily regulated industries like finance and insurance, enabling him to drive innovation and enhance design practices in a variety of organizational contexts.
See more
Related articles
Guides
Prompt engineering: 10 tips for content editors using generative AI
July 16, 2024
Guides
Using React with Node.js
February 6, 2025
Guides
How to build an API with the best GraphQL performance
July 9, 2025
Ready to start building?
Put everything you learned into action. Create and publish your content with Contentful — no credit card required.
Get started