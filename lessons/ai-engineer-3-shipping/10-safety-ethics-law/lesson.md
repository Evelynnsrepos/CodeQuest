---
title: Safety, ethics and the law
minutes: 45
xp: 60
hint: risk_tier: use & PROHIBITED is the set of shared tags. if len(use & PROHIBITED) > 0: return "prohibited", then the same for HIGH and TRANSPARENCY, else "minimal"
hint: disclose: tag = "[AI-generated] ", if answer.startswith(tag): return answer, else return tag + answer
hint: selection_rates: count totals[group] and accepted[group] in one loop over for group, ok in decisions:, then rates[group] = accepted[group] / totals[group]
hint: four_fifths_ok: top = max(rates.values()), then return False if any rates[group] < 0.8 * top, else True
---
# Build things you'd be fine explaining in public

⏱️ About 45 minutes

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

## 🔬 The four-fifths rule, step by step

1. **Selection rate** of a group = accepted ÷ everyone in that group. 50 accepted out of 100 → 50 ÷ 100 = **0.5** (50%).
2. Find the **highest** rate of all groups. Call it *top*.
3. **Four fifths** is 4 ÷ 5 = **0.8**. The limit is 0.8 × *top*.
4. Every group must be at or above that limit. A group below it is a warning sign that the system treats it unfairly.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `use & PROHIBITED` | "use and prohibited" | the tags that are in **both** sets: `{"chatbot", "hiring"} & HIGH` is `{"hiring"}` |
| `len(...) > 0` | | at least one shared tag |
| `answer.startswith(tag)` | | the tag is already there, so don't add it twice |
| `for group, ok in decisions:` | | each pair `("A", True)` is unpacked: `group` = `"A"`, `ok` = `True` |
| `totals.get(group, 0) + 1` | | the count so far (0 the first time) plus one |
| `if ok:` | | only for accepted ones |
| `max(rates.values())` | | the highest of all the rates |

### 👀 Worked example: two groups

`A`: 50 accepted, 50 not. `B`: 30 accepted, 70 not.

1. Rates: A = 50 ÷ 100 = **0.5**, B = 30 ÷ 100 = **0.3**.
2. *top* = 0.5. Limit = 0.8 × 0.5 = **0.4**.
3. A: 0.5 ≥ 0.4, fine. B: 0.3 < 0.4 → **False**: this hiring tool needs a closer look.

`risk_tier({"chatbot", "hiring"})`: no prohibited tag, but `hiring` is in HIGH → `"high"` (the stricter tier wins, because it's checked first).

## 🎯 Your quest

1. `risk_tier(use)`: `use` is a set of tags. Return `"prohibited"` if it shares any tag with `PROHIBITED`, else `"high"` if it shares any with `HIGH`, else `"transparency"` if with `TRANSPARENCY`, else `"minimal"`.
2. `disclose(answer)`: prefix `"[AI-generated] "` unless the answer already starts with it.
3. `selection_rates(decisions)`: `decisions` is a list of `(group, accepted)` pairs. Return a dict group → share accepted.
4. `four_fifths_ok(decisions)`: the "four-fifths rule" used in US hiring audits: `True` if every group's rate is at least 0.8 × the highest group's rate.

**Part 1:** `risk_tier`. Replace `return "minimal"` with:

1. `if len(use & PROHIBITED) > 0:`
2. `    return "prohibited"`
3. `if len(use & HIGH) > 0:`
4. `    return "high"`
5. `if len(use & TRANSPARENCY) > 0:`
6. `    return "transparency"`
7. `return "minimal"`

**Part 2:** `disclose`. Replace `return answer` with:

1. `tag = "[AI-generated] "`
2. `if answer.startswith(tag):`
3. `    return answer`
4. `return tag + answer`

**Part 3:** `selection_rates`. Replace `return {}` with:

1. `totals = {}`
2. `accepted = {}`
3. `for group, ok in decisions:`
4. `    totals[group] = totals.get(group, 0) + 1`
5. `    accepted[group] = accepted.get(group, 0)`
6. `    if ok:`
7. `        accepted[group] = accepted[group] + 1`
8. `rates = {}`
9. `for group in totals:`
10. `    rates[group] = accepted[group] / totals[group]`
11. `return rates`

**Part 4:** `four_fifths_ok`. Replace `return True` with:

1. `rates = selection_rates(decisions)`
2. `top = max(rates.values())`
3. `for group in rates:`
4. `    if rates[group] < 0.8 * top:`
5. `        return False`
6. `return True`

**Remember:** know your risk tier, tell people it's AI, measure per group, keep a human in the loop.

## Review

<details><summary>Why should LLM-judged evals not run on every push?</summary>They cost money and need secrets; run them on a schedule or by hand.</details>
