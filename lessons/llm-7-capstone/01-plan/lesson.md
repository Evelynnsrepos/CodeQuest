---
title: Pick a goal and a base model
minutes: 40
xp: 40
hint: PROJECT: write your own texts between the quotes. base_model needs a / like "Qwen/Qwen3-4B". success_criteria is a list of at least three texts
hint: pick_base: best = None, for c in candidates: if c["instruct"] and c["license"] in OK_LICENSES and c["params_b"] <= max_params_b:
hint: Inside that if: if best is None or c["params_b"] > best["params_b"]: best = c
hint: After the loop: if best is None: return None, then return best["name"]
---
# The capstone

⏱️ About 40 minutes

> **Warm-up:** what's one thing you'd *actually* use a small custom model for? Pick something where you'd immediately notice a bad answer.

The capstone uses every module once, on one project you care about:

1. Choose a **narrow goal** and a small **instruct** base model (1–4B).
2. Build a dataset of 200–1,000 examples in JSONL and clean it by hand.
3. Fine-tune with QLoRA (Unsloth or TRL), locally or on a rented GPU.
4. Evaluate base vs fine-tuned on 20+ held-out prompts, blind.
5. Merge, convert to GGUF, quantize, load in LM Studio.
6. Give it an MCP tool and use it as a small agent.
7. Write it up on GitHub: what worked, what didn't, what you'd change.

Each lesson here builds a small tool for one step, which you then run on your real data.

**Good goals are narrow and checkable:** "answers in my writing style", "turns my messy notes into a fixed Markdown template", "explains NixOS options like I would", "a German–English tutor persona for a game". "A smarter general assistant" is not a capstone goal: you can't beat the base model at everything with 500 examples.

First check the goal against LLMs 6, lesson 2: if it's really *knowledge*, add RAG instead of (or as well as) fine-tuning.

**Choosing the base model** (LLMs 2, lesson 12): instruct version, a license that allows what you want to do with the result, good at your language, a size that trains in your memory budget and runs fast after quantization, and a chat template with tool calling if you'll use MCP. Families with 1–4B instruct models at the time of writing include Qwen3, Llama 3.2, Gemma 3, SmolLM3 and Phi; new ones appear constantly, so check the Hub.

## 🧩 Part 1: how to fill in PROJECT

Write **your own** plan between the quotes. An example for a different project (don't copy it, make yours):

```python
PROJECT = {
    "goal": "Answer questions about my plant care notes in a short, friendly style.",
    "base_model": "Qwen/Qwen3-4B",
    "why_finetune": "The friendly short style is behaviour, and a system prompt alone keeps drifting.",
    "success_criteria": [
        "Blind judges prefer the tuned answers on at least 65% of 30 held-out prompts.",
        "Answers stay under 120 words on all held-out prompts.",
        "It still calls its search tool correctly in 9 of 10 test prompts.",
    ],
}
```

`success_criteria` is a **list**: square brackets, each criterion in quotes, commas between them.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `c["instruct"]` | | `True` if it's a chat/instruct model |
| `c["license"] in OK_LICENSES` | | true when the license is one of the allowed ones |
| `a and b and c` | | all three must be true |
| `best = None` | | "nothing found yet" |
| `if best is None or c["params_b"] > best["params_b"]:` | | take c if there's no best yet, **or** if c is bigger |
| `return best["name"]` | | only the name, not the whole dictionary |

### 👀 Worked example: the biggest ripe fruit

```python
best = None
for f in [{"name": "apple", "kg": 0.2, "ripe": True},
          {"name": "melon", "kg": 2.0, "ripe": False},
          {"name": "pear", "kg": 0.3, "ripe": True}]:
    if f["ripe"]:
        if best is None or f["kg"] > best["kg"]:
            best = f
print(best["name"])     # pear
```

1. apple: ripe, best is None → best = apple.
2. melon: not ripe, skipped.
3. pear: ripe, 0.3 > 0.2 → best = pear.

## 🎯 Your quest

**Part 1:** fill in `PROJECT` for **your** capstone (see above).

**Part 2:** `pick_base(candidates, max_params_b)`. Replace `return None` with:

1. `    best = None`
2. `    for c in candidates:`
3. `        if c["instruct"] and c["license"] in OK_LICENSES and c["params_b"] <= max_params_b:`
4. `            if best is None or c["params_b"] > best["params_b"]:`
5. `                best = c`
6. `    if best is None:`
7. `        return None`
8. `    return best["name"]`

It picks `Qwen/Qwen3-4B`, and with a 3.5B limit `meta-llama/Llama-3.2-3B-Instruct`.

## Review

<details><summary>RAG or fine-tuning for "make it know my notes"?</summary>RAG: it's changing knowledge, and RAG can cite its sources.</details>
<details><summary>What does a training loss near 0 on a small dataset usually mean?</summary>The model is memorizing the training examples (overfitting).</details>
