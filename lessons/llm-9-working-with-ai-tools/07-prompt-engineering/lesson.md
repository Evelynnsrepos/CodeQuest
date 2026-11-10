---
title: Prompt engineering that works
minutes: 30
xp: 50
hint: Start with parts = ["<documents>"] and i = 1
hint: for doc in documents: parts.append('<document index="' + str(i) + '">' + doc + "</document>") and then i = i + 1
hint: if len(examples) > 0: then for inp, out in examples: and append the <example>... text built with +
hint: End: append the instructions, then fmt, then return "\n".join(parts)
---
# Write it like a brief for a smart new coworker

⏱️ About 30 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `parts = ["<documents>"]` | | a list that starts with one line |
| `parts.append(x)` | "parts append x" | adds `x` as the next line |
| `str(i)` | "string of i" | the number as text: `str(2)` is `"2"`. You can't glue a number to text with `+` without it. |
| `'<document index="' + str(i) + '">'` | | single quotes `'...'` around text that holds double quotes `"`. Result: `<document index="2">` |
| `i = i + 1` | | counts up: 1, 2, 3, ... |
| `if len(examples) > 0:` | "if there is at least one example" | skips the block when the list is empty |
| `for inp, out in examples:` | "for each input and output" | each item is a pair; Python unpacks it into two names |
| `"\n".join(parts)` | "new-line join parts" | one text, one part per line |

### 👀 Worked example: a shopping note

```python
def note(items, pairs):
    parts = ["<items>"]
    i = 1
    for item in items:
        parts.append('<item n="' + str(i) + '">' + item + "</item>")
        i = i + 1
    parts.append("</items>")
    for a, b in pairs:
        parts.append(a + " -> " + b)
    return "\n".join(parts)

print(note(["milk", "eggs"], [("old", "new")]))
```

1. `parts` = `["<items>"]`, `i` = 1.
2. `"milk"`: appends `<item n="1">milk</item>`, `i` becomes 2. `"eggs"`: `<item n="2">eggs</item>`, `i` becomes 3.
3. Appends `</items>`.
4. The pair `("old", "new")`: `a` = `"old"`, `b` = `"new"` → appends `old -> new`.
5. Prints four lines:

```
<items>
<item n="1">milk</item>
<item n="2">eggs</item>
</items>
old -> new
```

## 🎯 Your quest

`build_prompt(task, why, documents, examples, fmt)`:

- documents (a list of strings) inside `<documents>`, each as `<document index="N">…</document>` numbered from 1,
- then examples (list of `(input, output)` pairs) inside `<examples>` as `<example><input>…</input><output>…</output></example>` (skip the block if the list is empty),
- then `<instructions>` + task + `" "` + why + `</instructions>`,
- then fmt as the last line.

Join the parts with `"\n"`.

Replace `return task` with:

1. `parts = ["<documents>"]`
2. `i = 1`
3. `for doc in documents:`
4. `    parts.append('<document index="' + str(i) + '">' + doc + "</document>")`
5. `    i = i + 1`
6. `parts.append("</documents>")`
7. `if len(examples) > 0:`
8. `    parts.append("<examples>")`
9. `    for inp, out in examples:`
10. `        parts.append("<example><input>" + inp + "</input><output>" + out + "</output></example>")`
11. `    parts.append("</examples>")`
12. `parts.append("<instructions>" + task + " " + why + "</instructions>")`
13. `parts.append(fmt)`
14. `return "\n".join(parts)`

**Remember:** data first, instructions with the why, format last.

## Review

<details><summary>What decides whether a skill loads?</summary>Its description.</details>
