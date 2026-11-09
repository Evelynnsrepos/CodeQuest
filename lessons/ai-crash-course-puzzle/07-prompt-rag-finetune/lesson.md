---
title: Prompt, RAG or fine-tune?
minutes: 20
xp: 25
hint: In choose, the order is the rule: prompt works → "prompt", missing facts → "rag", wrong style → "fine-tune".
hint: The handbook changes every month: that's missing knowledge (rag). Brand voice and exact format: behaviour (fine-tune).
distractor: "answer questions about the 200-page handbook that changes monthly": "fine-tune",
distractor: "summarize meeting notes; a good prompt already works": "rag",
---
# Three ways to make a model do your job

⏱️ About 20 minutes · 🧩 6 gaps, 2 decoys

> **Warm-up:** a new colleague keeps getting things wrong. Would you explain better, hand them the handbook, or send them on a course?

**In one sentence:** try a better **prompt** first; if the model is missing **knowledge**, give it documents (**RAG**); if it's missing **behaviour** (style, format), **fine-tune** it.

## 💡 The idea

| Way | What it is | Like… | Good for |
|---|---|---|---|
| **Prompt** | write clearer instructions and examples | explaining better | most jobs, start here, it's free |
| **RAG** (Retrieval-Augmented Generation) | search your documents, paste the best pieces into the prompt | handing over the handbook | facts the model doesn't know or that change |
| **Fine-tune** | train the model a bit more on your examples | sending them on a course | a fixed style, format or skill |

The common mistake is fine-tuning to teach **facts**. It's slow and the facts go out of date. Facts → RAG.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `if prompt_works:` | "if prompt works" | `prompt_works` is `True` or `False`; the line under it runs only for `True` |
| `return "rag"` | "give back rag" | gives back the text and **stops** the function, so later ifs don't run |
| `CASES = { ... }` | a dictionary | each line: a situation (key), colon, the answer (value), then a comma |

Because `return` stops the function, the **order** of the ifs is the rule: first question asked first.

### 👀 Worked example

```python
def drink(thirsty, cold):
    if thirsty:
        return "water"
    if cold:
        return "tea"
    return "nothing"
```

`drink(True, True)` gives `"water"`: the first if was true, so it stopped there and never asked about cold.

## 🧩 Your puzzle

1. `choose`: under each `if`, the matching answer: prompt works → `"prompt"`, needs facts → `"rag"`, needs style → `"fine-tune"`.
2. `CASES`: for each situation pick the block with the right answer. Ask: *is something missing, and is it knowledge or behaviour?* Two decoys give a situation the wrong answer.

Run it: `rag` and your three cases.

**Remember:** prompt first, facts → RAG, behaviour → fine-tune.
