---
title: Publish it with a model card
minutes: 35
xp: 40
hint: make_card: bodies is a list of six texts in SECTIONS order; the first is info["base_model"] + "\n\nLicense: " + info["license"]
hint: Then parts = ["# " + info["name"]], for i in range(len(SECTIONS)): parts.append(SECTIONS[i] + "\n\n" + bodies[i])
hint: make_card ends: return "\n\n".join(parts) + "\n"
hint: missing_sections: lines = markdown.splitlines(), missing = [], for s in SECTIONS: if s not in lines: missing.append(s), return missing
---
# Write it up so someone else can trust it

⏱️ About 35 minutes

> **Warm-up:** you find a fine-tune on Hugging Face with no description. What do you not know about it?

Everything that matters: what it was trained on, for what, how well it works, and where it fails. A **model card** answers those (you read them in LLMs 2, lesson 12; now you write one). Put it as `README.md` in your GitHub repo and, if you upload the GGUF, in the Hugging Face repo too.

Sections a good card has:

| Section | What goes in it |
|---|---|
| `## Base model` | exact model name and its license (your fine-tune inherits it) |
| `## Training data` | where the data came from, how many examples, how you cleaned it |
| `## Training` | method (QLoRA), rank, alpha, learning rate, epochs, max length, hardware, time |
| `## Evaluation` | blind win rate with its interval, tool-call accuracy base vs tuned |
| `## Limitations` | what it does badly, what it must not be used for |
| `## How to run` | GGUF file + quant, LM Studio / llama.cpp settings, chat template |

Also commit your scripts, your config and a small sample of the data (not private data!) so the run is reproducible.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"\n\n"` | | an empty line: in Markdown, a new paragraph |
| `"# " + info["name"]` | | the title line |
| `SECTIONS[i]`, `bodies[i]` | | the heading and text with the same position |
| `"\n\n".join(parts)` | | puts an empty line between all the parts |
| `markdown.splitlines()` | | a list with one entry per line |
| `s not in lines` | | true if no line is exactly that heading |

### 👀 Worked example: a two-section card

```python
parts = ["# demo"]
heads = ["## A", "## B"]
texts = ["first", "second"]
for i in range(len(heads)):
    parts.append(heads[i] + "\n\n" + texts[i])
print("\n\n".join(parts))
```

prints:

```
# demo

## A

first

## B

second
```

## 🎯 Your quest

`make_card(info)`: replace `return ""` with:

1. `    bodies = [`
2. `        info["base_model"] + "\n\nLicense: " + info["license"],`
3. `        info["data"],`
4. `        info["training"],`
5. `        info["evaluation"],`
6. `        info["limitations"],`
7. `        info["how_to_run"],`
8. `    ]`
9. `    parts = ["# " + info["name"]]`
10. `    for i in range(len(SECTIONS)):`
11. `        parts.append(SECTIONS[i] + "\n\n" + bodies[i])`
12. `    return "\n\n".join(parts) + "\n"`

`missing_sections(markdown)`: replace `return []` with:

1. `    lines = markdown.splitlines()`
2. `    missing = []`
3. `    for s in SECTIONS:`
4. `        if s not in lines:`
5. `            missing.append(s)`
6. `    return missing`

It prints the card and `missing: []`.

## Review

<details><summary>Your tuned model's tool-call accuracy fell from 0.95 to 0.70. What's the fix?</summary>Mix tool-calling examples (in the right chat template) back into the training data and retrain.</details>
<details><summary>Why must the card name the base model's license?</summary>The fine-tune is a derivative, so the base license's terms still apply to it.</details>
