---
title: Routers: send each item to the right place
xp: 25
---
# One question, many paths

⏱️ About 10 minutes · one function

> **Warm-up:** your inbox gets bills, newsletters and messages from friends. Should one prompt handle all three?

**In one sentence:** a **router** asks the model one short question (which kind is this?) and then your code sends the item to the handler for that kind.

## 🪜 Plain words

This is lesson 3's `label_for` plus a dictionary of functions:

```python
handlers = {"bill": save_to_bills, "newsletter": archive, "other": ask_me}
```

`handlers.get(label, handlers["other"])` picks the handler for the label, and falls back to `"other"` for anything unexpected. The model only decides **where** something goes. The handlers are plain, testable code (or their own small prompts).

## 🎯 Your quest

Write `route(text, llm, handlers)`:

1. The allowed labels are the keys of `handlers`: `list(handlers)`.
2. Ask `llm` with a prompt containing the text and the labels joined with `", "`.
3. Clean the reply like lesson 3 (strip, lower, strip dots).
4. Call the matching handler with `text` (or `handlers["other"]` if no match) and return what it returns.

<details><summary>💡 Hint</summary><code>handler = handlers.get(reply, handlers["other"])</code> then <code>return handler(text)</code></details>

## 🖥️ On your computer

Routers save money: a small fast local model does the routing, and only the hard path calls a big model.

**Remember:** the model picks the path, code walks it.

## Review

<details><summary>Lesson 5: how do you get a function's name in Python?</summary><code>step.__name__</code></details>
