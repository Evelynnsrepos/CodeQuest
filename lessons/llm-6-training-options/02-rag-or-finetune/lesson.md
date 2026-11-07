---
title: RAG or fine-tuning?
minutes: 30
xp: 35
hint: First check: if goal["prompt_works"]: return "prompt"
hint: Then: if goal["needs_facts"] and goal["needs_behaviour"]: return "both"
hint: Then if needs_facts → "rag", if needs_behaviour → "finetune", and the last line (no if) return "prompt"
---
# Knowledge vs behaviour

⏱️ About 30 minutes

> **Warm-up:** "I want the model to know my notes." Fine-tune it on the notes, or put the relevant notes in the prompt? Why?

The rule of thumb that holds up remarkably well:

> **RAG for knowledge. Fine-tuning for behaviour.**

**Knowledge** (facts, documents, your notes, a product manual, anything that changes): use **RAG**. Fine-tuning on facts works poorly: the model picks up the *style* of the documents much faster than it reliably memorizes their *content*, it can't cite sources, it hallucinates confidently when it half-remembers, and every update means retraining. RAG can be updated by editing a file, can quote its source, and lets you check what the model saw.

**Behaviour** (format, style, tone, a persona, always answering in strict JSON, a narrow skill, shorter answers, a language it handles poorly): **fine-tuning** shines. These are patterns the model applies *everywhere*, hard to describe in a prompt but easy to show with a few hundred examples. Fine-tuning can also make a small model as good as a bigger one on *one narrow task*, which saves VRAM and speed.

Before either: **try prompting**. A good system prompt with 3–5 examples ("few-shot") often solves behaviour problems with zero training.

Combinations are normal: a fine-tuned model that's good at *using* retrieved documents, or at calling your tools reliably, with RAG feeding it the facts.

Most people who think they need training actually need RAG or a better prompt.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `goal["prompt_works"]` | "goal at prompt works" | `True` or `False`, read from the dictionary |
| `if goal["prompt_works"]:` | | runs the next line when that value is `True` |
| `a and b` | | true only if **both** are true |
| `return "prompt"` | | ends the function. The `if`s below it are never reached. |

The **order** of the `if`s matters: the first one that's true wins.

### 👀 Worked example: what to wear

```python
def outfit(day):
    if day["raining"]:
        return "raincoat"
    if day["cold"] and day["windy"]:
        return "coat and scarf"
    if day["cold"]:
        return "coat"
    return "t-shirt"

print(outfit({"raining": False, "cold": True, "windy": True}))   # coat and scarf
```

1. Raining? No, go on.
2. Cold **and** windy? Yes → `"coat and scarf"`. The function stops here, so the plain "cold" check never runs.

If the "cold" check came first, it would always win and "coat and scarf" could never happen. Same in your quest: "both" must come before "rag".

## 🎯 Your quest

Write `decide(goal)`. Replace `return ""` with:

1. `    if goal["prompt_works"]:`
2. `        return "prompt"`
3. `    if goal["needs_facts"] and goal["needs_behaviour"]:`
4. `        return "both"`
5. `    if goal["needs_facts"]:`
6. `        return "rag"`
7. `    if goal["needs_behaviour"]:`
8. `        return "finetune"`
9. `    return "prompt"`

The four goals print `rag`, `prompt`, `finetune` and `both`.

## Review

<details><summary>In which order should you try prompting, RAG and fine-tuning?</summary>Prompting first, then RAG, then (Q)LoRA fine-tuning.</details>
<details><summary>Which methods change the model's weights?</summary>Pretraining, full fine-tuning, LoRA, QLoRA and DPO. Prompting and RAG don't.</details>
