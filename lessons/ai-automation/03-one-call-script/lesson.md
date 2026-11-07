---
title: A one-call script
minutes: 20
xp: 25
hint: First line: prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text
hint: Second line: reply = llm(prompt).strip().lower().strip(".")
hint: Then: if reply in labels: and under it return reply. After that, at the same level as the if: return "other"
---
# Ask, then clean up the answer

⏱️ About 20 minutes · one function, five lines

> **Warm-up:** you ask a model "is this email work, private or spam?" It answers `"Work."`. Is that the same text as `"work"`?

**In one sentence:** the simplest automation is one model call with a tight question, plus code that **cleans** the reply and has a fallback.

## 🪜 Plain words

In these lessons `llm` is a **function you get as an input**: `llm(prompt)` sends the prompt to a model and gives back the model's text. In the browser it's a fake model, so the checks always give the same result. On your computer it would call LM Studio or Ollama (see the end of the lesson). Getting the model as an input is also how real code gets tested.

Models add things you didn't ask for: spaces, capital letters, a full stop, sometimes a whole sentence. For a computer, `"Work."` and `"work"` are **different** texts. So:

1. Tell the model the **exact** allowed answers.
2. **Clean** the reply: remove spaces and line breaks at the ends, make it lowercase, remove dots at the ends.
3. If it's still not an allowed answer, use a **fallback** like `"other"` instead of crashing.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `["work", "spam"]` | "a list: work, spam" | a **list**: several values in a row, in square brackets |
| `", ".join(labels)` | "comma-space join labels" | glues the list's texts together with `", "` between them: `"work, spam"` |
| `"a" + "b"` | "a plus b" | glues two texts: `"ab"` |
| `"\n"` | "newline" | a line break inside a text. `"\n\n"` is an empty line. |
| `llm(prompt)` | "llm of prompt" | calls the model function and gives back its text |
| `s.strip()` | "s strip" | removes spaces and line breaks at the start and end: `"  Spam.\n"` → `"Spam."` |
| `s.lower()` | "s lower" | all lowercase: `"Spam."` → `"spam."` |
| `s.strip(".")` | "s strip dot" | removes dots at the start and end: `"spam."` → `"spam"` |
| `a.strip().lower()` | | the dots in a row mean "then": strip, **then** lowercase the result |
| `if reply in labels:` | "if reply is in labels" | true when the list `labels` holds exactly that text |

### 👀 Worked example 1: cleaning step by step

```python
reply = "  Spam.\n"
reply = reply.strip()      # "Spam."
reply = reply.lower()      # "spam."
reply = reply.strip(".")   # "spam"
```

Each line takes the text in the box `reply`, changes it, and puts the result back in the box. Writing `"  Spam.\n".strip().lower().strip(".")` does the same three steps in one line.

### 👀 Worked example 2: same shape, a different question

```python
def mood_of(text, llm, moods):
    prompt = "Answer with one word from: " + ", ".join(moods) + ".\n\n" + text
    reply = llm(prompt).strip().lower().strip(".")
    if reply in moods:
        return reply
    return "unknown"
```

`mood_of("I love this!", llm, ["happy", "sad"])`, line by line:

1. `", ".join(moods)` is `"happy, sad"`, so `prompt` is `"Answer with one word from: happy, sad.` + empty line + `I love this!"`.
2. Say the model answers `" Happy!\n"`. Cleaning gives `"happy!"`. The `!` isn't a dot, so it stays.
3. `if "happy!" in ["happy", "sad"]`: no, it's not exactly one of them.
4. So the `return reply` line is skipped and the function returns `"unknown"`.

If the model had said `"Happy."`, cleaning gives `"happy"`, the `if` is true, and it returns `"happy"`.

## 🎯 Your quest

Write `label_for(text, llm, labels)`. It's worked example 2 with `"other"` as the fallback. Inside the function:

1. `prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text`
2. `reply = llm(prompt).strip().lower().strip(".")`
3. `if reply in labels:`
4. `    return reply`
5. `return "other"`

Delete the starter's `return llm(text)` line.

## 🖥️ On your computer

A real `llm` for LM Studio's local server (start it in LM Studio's Developer tab), using only Python's built-in tools. You don't have to understand every line yet, just copy it:

```python
import json, urllib.request

def llm(prompt):
    body = json.dumps({"model": "local-model", "temperature": 0,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("http://localhost:1234/v1/chat/completions", body,
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["choices"][0]["message"]["content"]
```

`temperature 0` makes answers as repeatable as possible, which is what automations want. For retries and timeouts in depth, see AI engineer 2, lesson 08.

**Remember:** tight question, clean reply, fallback.

## Review

<details><summary>Lesson 2: what does format_map do when a field is missing?</summary>It raises a KeyError with the missing name, which our fill turns into a clear ValueError.</details>
<details><summary>What does "  Work.\n".strip().lower().strip(".") give?</summary>"work": spaces and line break gone, lowercase, dot gone.</details>
