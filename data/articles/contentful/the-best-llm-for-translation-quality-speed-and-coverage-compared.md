---
title: The best LLM for translation: Quality, speed, and coverage compared
url: https://www.contentful.com/blog/best-llm-translation/
---

Blog
/
Guides
/
The best LLM for translation: Quality, speed, and coverage compared
The best LLM for translation: Quality, speed, and coverage compared
Published on November 21, 2025
Written by
Alex Wake
Senior Product Manager
,
Contentful
On this page
LLM vs. NMT
The top 5 LLMs for translation
How to choose the right LLM for translation
Open source vs. proprietary LLMs
Challenges and how to optimize translation quality
Contentful helps with multilingual content workflows
Contentful allows you to bring your own model
Inspiration for your inbox
Subscribe and stay up-to-date on best practices for delivering modern digital experiences.
TL;DR
powered by AI Actions
Large language models (LLMs) now dominate translation, outperforming traditional neural machine translation (NMT) in quality and adaptability while being 10-100 times cheaper per character, though they remain slower.
GPT-4 ranks as the best overall LLM for translation, excelling in quality and customization, while Claude 3.5 Sonnet offers strong data privacy, and Gemini 1.5 Pro provides superior speed for large documents.
Organizations should choose translation models based on their specific needs, considering factors like language coverage, speed, customization options, and whether to use proprietary models or open-source alternatives.
Translation quality can be optimized by combining multiple LLMs in unified systems, using prompt injection with glossaries or style guides, fine-tuning, and utilizing retrieval-augmented generation to provide contextual information.
In recent years, large language models (LLMs) have been considered serious competitors when it comes to AI translation. LLMs now account for
89% of the top-performing systems
in their benchmarks due to their ability to adapt terminology, tone, and formatting to business requirements.
This article draws information from the
WMT 2024 conference on machine translation
and Intento’s State of Translation Automation 2025 to find the best LLM for translation and how other models compare to give you an overview on what will be best for your use case.
Interactive demo: Bulk Translation
Run AI Actions on multiple pieces of content simultaneously and speed up production.
LLM vs. NMT
Machine translation started with the success of wartime cryptography (such as the cracking of the Enigma code), leading researchers to ponder whether language could also be decoded in a similar way. After many experiments and failures, IBM pioneered statistical machine translation (SMT) in the late 1980s, and by the 2000s SMT became the industry standard, powering early versions of Google Translate. Around 2014, neural networks using deep learning to model entire sentences and capture context overtook SMT, and neural machine translation (NMT) became the new baseline (used in Google Translate, DeepL, etc.). It has speed, efficiency, and accuracy, but struggles with context, nuance, and adaptability.
Now, large language models (LLMs) are the new, more flexible approach to translation that’s
surpassing NMT
in quality and adaptability. LLMs outperform traditional NMT overall when judged on terminology, tone, formatting, and full-text consistency, not just sentence similarity.
LLMs are able to grasp a broader context, preserve cultural nuance, and maintain consistency. But what really sets LLMs apart is the ability to set up multi-agent flows instead of relying on a single model trying to solve everything end to end. Combined with their adaptability to specialized terminology, broad multilingual support, and the fact that they’re on average 10–100 times cheaper per character than NMT engines, it's clear why LLMs are becoming ubiquitous in the translation world.
Despite these advantages, there are still some limitations to note: LLMs remain 10–100 times slower than specialized NMT engines, so real-time (live chat, customer support) use still favors NMT. However, hardware and software developments to reduce inference are slowly closing the gap. LLMs can also "hallucinate" — introducing terms, false “facts,” or stylistic choices not present in the source text — which can be devastatingly risky in legal, medical, or technical domains where accuracy is paramount. Despite the overall consensus being that LLMs are surpassing traditional methods, fine-tuned NMT models can still be more effective for low-resource languages.
The top 5 LLMs for translation
We've sifted through the latest research to find the best LLM model for translation. There are many different factors to consider when choosing a model that suits your needs, so to make your evaluation easier, we’ve ranked each model against the key criteria that matter most:
Translation quality
is based on scores such as COMET, BLEURT, and
Intento’s LQA
(a framework derived from MQM).
Language and domain coverage
takes into account the number of supported languages and domain-specific performance.
Speed and scalability
measure latency and throughput.
Customization and fine-tuning
evaluate how well models adapt to glossary prompts or specialized data.
Integration and compatibility
consider API support and workflow fit.
Data privacy
is compliant with standards like GDPR and CCPA.
We gave each a ranking between 1 and 5, with 5 being the best.
Based on the data, Open AI’s GPT-4 consistently scored the highest overall, particularly in translation quality and customization; it's a particularly good fit for organizations already invested in OpenAI’s ecosystem. Anthropic’s Claude was close behind, scoring well in fluency and data privacy. Google’s Gemini 1.5 Pro also performed well, showing impressive speed and scalability, especially when handling larger documents. All of the proprietary models are straightforward to integrate, with well-documented APIs.
Open-source models like DeepSeekV3 had good results with Asian-European language pairs and also scored high in speed and scalability. Meta’s NLLB-200 excels in low-resource languages, offering the broadest coverage for over 200 languages.
The following graph shows the top five models for
AI translation
and how each of them performed across the different categories:
Model
Best categories
Best for
GPT-4
Translation quality
Integration & compatibility
Accuracy and customization, best all rounder for enterprise use
Claude 3.5 Sonnet
Data privacy
Integration & compatibility
Top-quality translations with strong compliance
Gemini 1.5 Pro
Speed & scalability
Integration & compatibility
Speed, handles large documents well
DeepSeek V3
Speed & scalability
Fast translations with open-source flexibility
Meta NLLB-200
Language & domain coverage
Currently the best choice for low-resource languages
Though not included in the reports, an honorable mention would be Mixtral 8x7B. It brings in the
Mixture of Experts
design, which is still experimental, but has the potential to outperform today's LLMs in specific areas (like low-resource languages) because it has the ability to allocate expert subnetworks to those tasks.
How to choose the right LLM for translation
There’s no universal “right choice” when choosing an LLM for translation. The correct choice is subjective and really comes down to what your needs are as an organization. Perhaps speed’s most important when translating large documents, or maybe data privacy’s what matters most in your case. To begin the process, define your use case clearly, as this will clear up what factors are most important to you.
Consider the types of content you’ll be translating: will it be for low-resource languages or content that requires customizability for a certain context? You’ll also want to consider your budget and the existing infrastructure to see what you can afford and how difficult it might be to integrate. If you have a need to customize and fine-tune the model and also want a high level of data privacy, you’ll need to carefully consider between open source vs. proprietary models.
Open source vs. proprietary LLMs
When choosing between LLMs, one of the biggest decisions is whether you should go with an open source or proprietary model. Our ranking list contains a mix of both types of LLMs, which makes it easy to see some of the tradeoffs. Generally, proprietary models tend toward better performance and ease of integration, whereas open-source models are more transparent and allow for more customizability and control. Below is a breakdown of some of the features and challenges of both:
Proprietary
Ease of integration:
Extensive APIs make it straightforward to get started without heavy engineering effort.
State-of-the-art performance:
Proprietary models often lead in benchmarks for quality and fluency.
Enterprise reliability:
Backed by SLAs, customer support, and security/compliance certifications.
Rapid feature development:
Providers have huge development teams that roll out frequent improvements you can benefit from immediately.
Challenges:
There’s a risk of vendor lock-in, customization limits, data privacy concerns, and usage-based costs that can grow quickly.
Open source
Transparency:
You can inspect weights, training data, and architecture to understand how the model works.
Customization and fine-tuning:
You can easily use third-party models and self-train them to adapt to your data needs.
Deployment control:
Run the model on your own infrastructure for full ownership of performance and compliance.
Cost efficiency:
No recurring API fees; costs are mostly infrastructure and engineering time.
Innovation:
Open communities experiment rapidly, often producing novel techniques and niche optimizations.
Challenges:
Requires in-house machine learning expertise to fine-tune and maintain, introduces infrastructure overhead, and lacks support.
Challenges and how to optimize translation quality
LLMs are accelerating the progress of machine translation, but there are still several challenges that need to be solved until the field can reach its full potential. Models can inherit biases from the data they're trained on, struggle with low-resource languages, and introduce inconsistencies across large volumes of content. Cost is also a consideration, particularly when you need translations across multiple languages and different channels.
One way you can optimize translation is by combining multiple LLMs together to work as a unified system. You could build an automated workflow that checks incoming translation tasks and selects the best model for that language pair. For example, when high-resource languages are submitted, it uses a state-of-the-art model like GPT-4 or Claude for speed and quality, while low-resource languages might route through Meta's NLLB. You could even go a step further and have it evaluate which model performs best for that specific pair each time, such as using DeepSeek for European-Asian translations. By avoiding "putting all of your eggs in one basket," you can ensure you get the best translation quality available for every language pair.
The default performance of any one model is rarely enough for specialized domains. Terminology accuracy often demands fine-tuned or multi-agent setups. Tone compliance can reach near-perfect levels when you give models explicit instructions and brand guidelines to follow.
Even state-of-the-art models will underperform if they lack the right context. There are several ways to inject this context:
Use prompt injection to provide glossaries, style guides, or translation memories.
Use fine-tuning or adapters to adapt the base model to your domain.
Use retrieval-augmented generation (RAG) to fetch relevant contextual content from a
CMS
, knowledge base, or glossary, and then inject this information into the model before it generates a translation.
The
Model Context Protocol (MCP)
has recently begun to connect LLMs with live data sources and tools in real-time, helping reduce hallucinations.
Even with the best model setup, organizations still face challenges in scaling and managing multilingual content across channels. These challenges are often due to domain drift and the difficulty of evaluating multilingual content.
Contentful helps with multilingual content workflows
Contentful combines integrated translation capabilities and
AI-driven features
to help you orchestrate scalable, consistent, and intelligent multilingual content workflows that go beyond raw model output.
For example, Contentful could act as the retrieval layer in a RAG setup, supplying glossaries, brand guidelines, and structured metadata directly into the translation pipeline. This pairs well with multi-agent flows where different LLMs handle translation, review, and QA.
Inspired by
Google's adaptive translation
, Contentful is exploring ways to use vector embeddings to ensure translations have richer contextual grounding. This would allow your translations to adapt dynamically to domain-specific terminology, tone, and channel requirements, improving accuracy without having to retrain the base model.
Contentful allows you to bring your own model
Contentful also solves vendor lock-in with its bring-your-own-model approach. This means that, unlike proprietary CMSes that lock you into a single translation vendor, Contentful enables organizations to choose the LLM or translation provider that best fits their needs, whether that's for cost efficiency, compliance, or specific language coverage. Contentful orchestrates the workflow and context and allows you to make a choice on what the best LLM for translation is, ensuring freedom from vendor lock-in.
You can bring tone, terminology, and post-editing checks directly into Contentful's editorial and approval workflows. Contentful can validate translation quality not only by a model in a multi-agent workflow but also a human-in-the-loop QA for final checks, delivering quality and consistency across all channels.
When it comes to what the best LLM for translation is, it ultimately rests on what is most important to your organization and what you’re trying to achieve. For some it might be a matter of ease of integration into a certain ecosystem; for others, quality alongside privacy might be what tips the scales. There is also the possibility that some might go for a multi-agent workflow, incorporating a mix of different models using each LLM to perform tasks it naturally excels in. Whatever you decide, Contentful has you covered when handling complex multilingual workflows.
Take a tour
Chat with our team
Your experiences should wow, not wait. Let's talk.
Inspiration for your inbox
Subscribe and stay up-to-date on best practices for delivering modern digital experiences.
Content platform
Composability
Artificial intelligence
Copy Page Url
Linkedin
Facebook
Twitter
Meet the authors
Alex
Wake
Senior Product Manager
Contentful
Alex is an AI Product Manager at Contentful with a focus on leveraging LLMs, natural language processing, and knowledge graphs to shape the next generation of digital experiences. He's passionate about building intelligent, scalable solutions that enhance personalization and content operations.
See more
Related articles
Guides
How to build a product page with Commerce Layer, Cloudinary and Contentful
November 22, 2024
Guides
Static vs. dynamic websites: Building the best website for your users
April 2, 2024
Guides
Which is the best React rich text editor? Five options compared
March 18, 2025
Ready to start building?
Put everything you learned into action. Create and publish your content with Contentful — no credit card required.
Get started