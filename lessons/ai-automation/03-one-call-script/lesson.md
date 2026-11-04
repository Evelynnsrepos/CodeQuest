---
title: A one-call script
xp: 25
---
# Ask, then clean up the answer

⏱️ About 10 minutes · one function

> **Warm-up:** you ask a model "is this email work, private or spam?" It answers `"Work."`. Is that equal to `"work"` in Python?

**In one sentence:** the simplest automation is one model call with a tight question, plus code that **cleans** the reply and has a fallback.

## 🪜 Plain words

In these lessons `llm` is a **function you pass in**: `llm(prompt)` returns the model's text. In the browser it's a fake model, so the checks are repeatable. On your computer it would call LM Studio or Ollama (see below). Passing it in is also how real code gets tested.

Models add things you didn't ask for: spaces, capital letters, a full stop, sometimes a whole sentence. So:

1. Tell the model the **exact** allowed answers.
2. Clean the reply: `.strip()` removes spaces and newlines at the ends, `.lower()` makes it lowercase, `.strip(".")` removes dots at the ends.
3. If it's still not an allowed answer, use a **fallback** like `"other"` instead of crashing.

## 🎯 Your quest

Write `label_for(text, llm, labels)`:

1. Build a prompt that contains the text and the allowed labels joined with `", "`, for example: `"Answer with one word from: work, private, spam.\n\n" + text`
2. Call `llm(prompt)` once.
3. Clean the reply (strip, lower, strip dots).
4. Return it if it's in `labels`, otherwise `"other"`.

<details><summary>💡 Hint</summary><code>reply = llm(prompt).strip().lower().strip(".")</code> then <code>return reply if reply in labels else "other"</code></details>

## 🖥️ On your computer

A real `llm` for LM Studio's local server (start it in LM Studio's Developer tab), using only the standard library:

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

<details><summary>Lesson 2: what does template.format(**fields) do when a field is missing?</summary>It raises KeyError with the missing name.</details>
