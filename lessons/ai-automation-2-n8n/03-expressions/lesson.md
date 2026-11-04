---
title: Expressions: {{ $json.name }}
xp: 30
---
# Fill fields from the data

⏱️ About 12 minutes · one function

> **Warm-up:** you want the Telegram text to say "New mail from anna@x.de". How does the Telegram node know the address of *this* item?

**In one sentence:** any node field can hold an **expression** in double curly braces, and `$json` means "the current item's json".

## 🪜 Plain words

- `New mail from {{ $json.from }}` → `New mail from anna@x.de`
- Dots go deeper: `{{ $json.sender.name }}` reads `{"sender": {"name": "Anna"}}`.
- `{{ $('Read Email').item.json.subject }}` reads from an **earlier** node by its name, for the matching item. Use it when a node in between (like an AI node) replaced `$json` with its own output.

This is the same idea as lesson 2 of AI automation 1 (`{name}` templates), with n8n's syntax.

## 🎯 Your quest

Write `render(text, item, nodes)`: replace every `{{ ... }}` in `text`:

- `$json.a.b` → follow the keys `a`, `b` in `item`
- `$('Name').item.json.a` → follow `a` in `nodes["Name"]`
- spaces inside the braces don't matter
- the value is turned into text with `str()`

Use `re.sub` with a function. The pattern `r"\{\{\s*(.*?)\s*\}\}"` finds each expression and captures what's inside.

<details><summary>💡 Hint 1: follow a path</summary><code>for key in "a.b".split("."): value = value[key]</code></details>
<details><summary>💡 Hint 2: the node form</summary><code>m = re.match(r"\$\('(.+?)'\)\.item\.json\.(.+)", expr)</code> gives the node name in <code>m.group(1)</code> and the path in <code>m.group(2)</code>. Otherwise the expression starts with <code>"$json."</code>.</details>

**Remember:** `{{ }}` = "fill in from the data", `$json` = this item.

## Review

<details><summary>Lesson 2: a node gets 4 items. How often does a "Send message" node run?</summary>4 times, once per item.</details>
