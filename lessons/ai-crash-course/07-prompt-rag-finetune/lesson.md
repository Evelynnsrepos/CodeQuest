---
title: Prompt, RAG or fine-tune?
xp: 25
hint: choose, first two lines: if prompt_works: and under it return "prompt"
hint: Then the same for needs_facts (return "rag") and needs_style (return "fine-tune"), and a last return "prompt" at 4 spaces.
hint: In CASES, write the answer between the empty quotes: "rag", "fine-tune" or "prompt".
---
# Three ways to make a model do your thing

⏱️ About 20 minutes · one function and three answers

> **Warm-up:** you want a chatbot that answers questions about your company's handbook. What would you try first?

**In one sentence:** try a better **prompt** first, add **RAG** when the model is missing knowledge, and **fine-tune** only when you need a different behaviour.

## 💡 The idea in plain words

| | What it changes | Good for | Cost |
|---|---|---|---|
| **Prompting** | only the instructions and examples you send | most tasks; always try first | minutes |
| **RAG** (retrieval-augmented generation) | your code finds relevant documents (with embeddings, lesson 04) and pastes them into the prompt at question time | facts the model doesn't know, facts that change, answers with sources | a few hours to build |
| **Fine-tuning** | the model's weights, by training it on your examples (lesson 06) | a consistent style or format, a narrow skill, a smaller cheaper model | data + GPU time; retrain to update |

The rule of thumb: **prompt first; add RAG for knowledge; fine-tune for behaviour.**

A common mistake is fine-tuning to teach facts: the model learns the *style* of your documents but still makes up details, and you must retrain whenever the facts change. With RAG you just update the documents.

<div class="quiz" data-answer="1" data-why="Facts that change belong in RAG: update the documents, no retraining."><p><b>Predict first:</b> your bot must know this week’s prices, which change every day. What do you use?</p><button>fine-tuning</button><button>RAG</button><button>a longer prompt with no data</button></div>

**Go deeper:** LLMs 3 (RAG and tools), LLMs 6 (fine-tuning and its alternatives), AI engineer 2 (real RAG).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `True`, `False` | "true", "false" | the two yes/no values (called **booleans**). Capital first letter! |
| `if ready:` | "if ready" | runs the indented lines when `ready` holds `True` |
| `return "rag"` | "give back the text rag" | hands back a string and **stops the function** immediately. Lines below it don't run. |
| several ifs in a row | | checked top to bottom. The **first** one that's true wins, because its `return` stops the function. |

### 👀 Worked example: what to wear

```python
def outfit(raining, cold):
    if raining:
        return "raincoat"
    if cold:
        return "jumper"
    return "t-shirt"
```

Try each case in your head, top to bottom:

| raining | cold | first true if | gives back |
|---|---|---|---|
| True | True | `if raining` | `"raincoat"` (the cold check never runs) |
| False | True | `if cold` | `"jumper"` |
| False | False | none | `"t-shirt"` (the last line) |

The **order** is the rule: rain matters more than cold. In `choose`, the order is the rule of thumb: prompt first, then RAG, then fine-tuning.

### Filling in a dictionary of texts

`CASES` is a dictionary (lesson 01): each key is a scenario, each value is your answer. You only change the empty `""` into a word between the quotes:

```python
CASES = {
    "some scenario": "rag",
}
```

## 🎯 Your quest

1. `choose(prompt_works, needs_facts, needs_style)`: each input is `True` or `False`. Like `outfit`:
   - `if prompt_works:` → `return "prompt"`
   - `if needs_facts:` → `return "rag"`
   - `if needs_style:` → `return "fine-tune"`
   - last line: `return "prompt"` (nothing specific is missing: keep improving the prompt)
2. In `CASES`, replace each `""` with `"prompt"`, `"rag"` or `"fine-tune"`. Ask for each scenario: does a prompt already work? Is knowledge missing? Is behaviour/style missing?

**Remember:** prompt first, RAG for knowledge, fine-tune for behaviour.
