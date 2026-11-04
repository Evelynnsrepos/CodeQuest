---
title: Safety, ethics and the law
xp: 60
---
# Build things you'd be fine explaining in public

> **Warm-up:** your app screens job applications with an LLM. Who could be harmed, and how would you find out?

This lesson gives you a working map, **not legal advice**. Laws change; check the current text before you ship something serious.

## The EU AI Act (in force since August 2024)

It sorts AI systems by **risk**:

| Tier | Examples | What it means |
|---|---|---|
| **Prohibited** | social scoring of people; manipulating people in harmful ways; scraping faces from the internet for recognition databases; emotion recognition at work or school (with narrow exceptions) | not allowed (since February 2025) |
| **High risk** | hiring and managing workers, grading or admitting students, credit scoring, access to essential services, critical infrastructure, policing, migration, medical devices | risk management, data quality, logging, human oversight, documentation, registration; dates are being phased in from 2026, check the current timeline |
| **Transparency** | chatbots, AI-generated images, audio and video ("deepfakes") | tell people they're talking to an AI; label generated content |
| **Minimal** | spam filters, games, most coding helpers | no new duties |

Providers of **general-purpose models** (like Llama or GPT) have their own duties (documentation, copyright policy) since August 2025.

## GDPR (DSGVO)

Personal data needs a **legal basis** (consent, contract, legitimate interest…), must be **minimized** (only what you need), kept **no longer than needed**, and people can ask to see or delete it. Sending personal data to an API in another country is a data transfer with its own rules. The Data cleaning course's redaction (lesson 12) is a first technical step.

## Licenses

Code, models and data all have licenses. **Apache-2.0** and **MIT** allow commercial use. Many "open" models use custom licenses with conditions (Llama's community license, for example). Datasets may be research-only. Read the model card's license line (LLMs 2 lesson 12) before building a product on it.

## Safety in the app itself

- **Guard the input:** block prompt-injection attempts and abuse where you can (LLMs 9 lesson 09); limit rates (lesson 05).
- **Guard the output:** remove personal data, check format, refuse clearly out-of-scope requests.
- **Bias:** measure results per group (does it reject more applicants from one group?), not just overall.
- **A human in the loop** for decisions that matter to people.

## Your quest

1. `risk_tier(use)`: `use` is a set of tags. Return `"prohibited"` if it shares any tag with `PROHIBITED`, else `"high"` if it shares any with `HIGH`, else `"transparency"` if with `TRANSPARENCY`, else `"minimal"`.
2. `disclose(answer)`: prefix `"[AI-generated] "` unless the answer already starts with it.
3. `selection_rates(decisions)`: `decisions` is a list of `(group, accepted)` pairs. Return a dict group → share accepted.
4. `four_fifths_ok(decisions)`: the "four-fifths rule" used in US hiring audits: `True` if every group's rate is at least 0.8 × the highest group's rate.

**Remember:** know your risk tier, tell people it's AI, measure per group, keep a human in the loop.

## Review

<details><summary>Why should LLM-judged evals not run on every push?</summary>They cost money and need secrets; run them on a schedule or by hand.</details>
