---
title: Dataset formats: JSONL and chat messages
minutes: 50
xp: 40
hint: alpaca_to_chat: if system is not None: messages.append({"role": "system", "content": system})
hint: Then user = record["instruction"], and if record.get("input", "") != "": user = user + "\n\n" + record["input"]
hint: Then append the user message and {"role": "assistant", "content": record["output"]}
hint: to_jsonl: lines = [], for r in records: lines.append(json.dumps(r)), return "\n".join(lines)
hint: validate_line: try: data = json.loads(line) and except ValueError: return "not valid JSON". Then one if per rule, each returning a short text
---
# What a fine-tuning dataset looks like

⏱️ About 50 minutes

> **Warm-up:** to teach a model your writing style, what would one training example look like? What goes in, and what should come out?

A supervised fine-tuning (**SFT**) dataset is a list of example conversations. It's almost always stored as **JSONL** ("JSON Lines"): one complete JSON object **per line**, nothing else. That makes huge files easy to stream, split and append to.

Two shapes you'll meet:

**Instruction format** (from Stanford's Alpaca dataset): flat fields.

```json
{"instruction": "Summarize the text.", "input": "LoRA freezes the base model and ...", "output": "LoRA trains small matrices ..."}
```

**Chat / messages format**: the same `messages` list you send to LM Studio. This is what modern tools (TRL, Unsloth, Axolotl) prefer, because the tool can apply the model's own chat template.

```json
{"messages": [{"role": "system", "content": "You write like Evelynn."},
              {"role": "user", "content": "Explain the KV cache."},
              {"role": "assistant", "content": "ok so basically ..."}]}
```

(You'll also see **ShareGPT** format, `{"conversations": [{"from": "human", "value": ...}]}`, which tools can convert.)

What makes a dataset good matters far more than its size:

- **Quality over quantity.** 300 clean, consistent examples beat 30,000 sloppy ones. Read every example; your model will copy mistakes faithfully.
- **Consistency.** If half your answers start with "Sure!" and half don't, the model learns a coin flip.
- **Coverage.** Include the variety of requests it will really see, including short ones and edge cases.
- **Hold out** 10% (or at least 20 prompts) for validation and evaluation before you start (LLMs 5, lesson 8).
- **Deduplicate**, and keep private data out unless the model will stay private.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `if system is not None:` | | true when a system text was given. `None` means "nothing". |
| `record.get("input", "")` | | the input, or `""` if the record has none |
| `"\n\n"` | "two newlines" | an empty line between instruction and input |
| `json.dumps(r)` | | the dictionary as **one line** of JSON text |
| `"\n".join(lines)` | | glues the lines with a newline between them |
| `try:` … `except ValueError:` | | try something; if it fails with that error, run the `except` part instead of crashing |
| `isinstance(x, dict)`, `isinstance(x, list)`, `isinstance(x, str)` | | "is x a dictionary / list / text?" |
| `x not in ["a", "b"]` | | true when x is none of them |
| `messages[-1]` | "the last message" | `-1` counts from the end |

### 👀 Worked example: one record, step by step

`{"instruction": "Say hi in German.", "input": "", "output": "Hallo!"}` with system `"You are concise."`:

1. System given → messages = `[{"role": "system", "content": "You are concise."}]`.
2. user = `"Say hi in German."`. The input is `""`, so nothing is added.
3. Add `{"role": "user", "content": "Say hi in German."}` and `{"role": "assistant", "content": "Hallo!"}`.

With input `"Hund"` and instruction `"Translate."`, step 2 gives `"Translate.\n\nHund"`.

**Checking a line.** `validate_line` is a list of checks, each one returning a short error the moment something is wrong. Only a line that passes **all** of them reaches the last `return None`:

```python
def check_age(text):
    try:
        age = int(text)
    except ValueError:
        return "not a number"
    if age < 0:
        return "negative"
    return None

print(check_age("abc"), check_age("-3"), check_age("12"))   # not a number negative None
```

## 🎯 Your quest

**Part 1:** `alpaca_to_chat(record, system=None)`. Between `messages = []` and `return {"messages": messages}`, add:

1. `    if system is not None:`
2. `        messages.append({"role": "system", "content": system})`
3. `    user = record["instruction"]`
4. `    if record.get("input", "") != "":`
5. `        user = user + "\n\n" + record["input"]`
6. `    messages.append({"role": "user", "content": user})`
7. `    messages.append({"role": "assistant", "content": record["output"]})`

**Part 2:** `to_jsonl(records)`. Replace `return ""` with:

1. `    lines = []`
2. `    for r in records:`
3. `        lines.append(json.dumps(r))`
4. `    return "\n".join(lines)`

**Part 3:** `validate_line(line)`. Above `return None`, add:

1. `    try:`
2. `        data = json.loads(line)`
3. `    except ValueError:`
4. `        return "not valid JSON"`
5. `    if not isinstance(data, dict):`
6. `        return "needs a messages list with at least 2 messages"`
7. `    messages = data.get("messages")`
8. `    if not isinstance(messages, list) or len(messages) < 2:`
9. `        return "needs a messages list with at least 2 messages"`
10. `    for m in messages:`
11. `        if m.get("role") not in ["system", "user", "assistant"]:`
12. `            return "unknown role"`
13. `        content = m.get("content")`
14. `        if not isinstance(content, str) or content == "":`
15. `            return "empty content"`
16. `    if messages[-1]["role"] != "assistant":`
17. `        return "last message must be from the assistant"`

The last two test lines print an error each; the two good lines print `None`.

## Review

<details><summary>Rule of thumb: RAG or fine-tuning?</summary>RAG for knowledge, fine-tuning for behaviour (style, format, narrow skills).</details>
<details><summary>Why is fine-tuning a poor way to add facts?</summary>The model learns style faster than content, can't cite sources, hallucinates half-remembered facts and needs retraining for every update.</details>
