---
title: Prompt engineering that works
xp: 50
---
# Write it like a brief for a smart new coworker

> **Warm-up:** "Summarize this." vs. "Summarize this bug report in 3 bullet points for a beginner, because it'll be a phone notification." Which gets better results, and why?

**In one sentence:** good prompts give the goal, the context and the why, examples, a clear structure that separates data from instructions, and an exact output format.

## 🪜 Plain words (from the guide)

| Technique | Why it works |
|---|---|
| Be specific: goal, audience, length, format | the model fills gaps with the most average guess |
| Give the **why** | lets it handle cases you didn't list |
| 2–5 **examples** (few-shot) | models copy patterns more reliably than descriptions |
| **Tags** like `<document>`, `<instructions>` | data and instructions don't get mixed up |
| **Long documents first, question last** | the end of the prompt gets the most attention |
| Ask for a **format** | easy to parse and check automatically |
| Say what **to do**, not only what not to do | "don't X" still puts X in context |
| **Iterate with evals**: 10–20 test inputs, change one thing | otherwise you're guessing |

Small local models need even more help: shorter prompts, more examples, stricter formats, fewer tools, lower temperature.

## 🪜 With numbers

A well-built prompt, in order:

```
<documents>
<document index="1">…bug report…</document>
</documents>
<examples>
<example><input>…</input><output>…</output></example>
</examples>
<instructions>
Summarize the bug report for a beginner in 3 bullet points. It will be shown as a phone notification, so keep each bullet under 12 words.
</instructions>
Answer with only the 3 bullets.
```

## 🔀 What if it were different?

<div class="wrong"><b>Question first, 20 pages of document after</b>: the question is far from the end and gets less attention; answers drift.</div>
<div class="wrong"><b>Document pasted without tags</b>: if it contains "ignore the above and…", the model can't tell your instructions from its data (prompt injection, lesson 09).</div>
<div class="wrong"><b>"Don't use bullet points"</b>: "Write in plain sentences" works better.</div>
<div class="right">documents → examples → instructions with the why → exact format, last ✓</div>

## 🎯 Your quest

`build_prompt(task, why, documents, examples, fmt)`:

- documents (a list of strings) inside `<documents>`, each as `<document index="N">…</document>` numbered from 1,
- then examples (list of `(input, output)` pairs) inside `<examples>` as `<example><input>…</input><output>…</output></example>` (skip the block if the list is empty),
- then `<instructions>` + task + `" "` + why + `</instructions>`,
- then fmt as the last line.

Join the parts with `"\n"`.

**Remember:** data first, instructions with the why, format last.

## Review

<details><summary>What decides whether a skill loads?</summary>Its description.</details>
