---
title: Expressions: {{ $json.name }}
minutes: 40
xp: 30
hint: follow: for key in path.split("."): and inside it value = value[key]. After the loop: return value
hint: value_of, the node form: if expr.startswith("$('"): then end = expr.index("')") and name = expr[3:end]
hint: Still in the if: path = expr[end + len("').item.json."):] and return str(follow(nodes[name], path))
hint: After the if (4 spaces): return str(follow(item, expr[len("$json."):]))
---
# Fill fields from the data

⏱️ About 40 minutes · two small functions (the third one is given)

> **Warm-up:** you want the Telegram text to say "New mail from anna@x.de". How does the Telegram node know the address of *this* item?

**In one sentence:** any node field can hold an **expression** in double curly braces, and `$json` means "the current item's json".

## 🪜 Plain words

- `New mail from {{ $json.from }}` → `New mail from anna@x.de`
- Dots go deeper: `{{ $json.sender.name }}` reads `{"sender": {"name": "Anna"}}`: first the box `sender`, then the box `name` inside it.
- `{{ $('Read Email').item.json.subject }}` reads from an **earlier** node by its name (`Read Email`), for the matching item. Use it when a node in between (like an AI node) replaced `$json` with its own output.

This is the same idea as lesson 2 of AI automation 1 (`{name}` templates), with n8n's way of writing it.

In this lesson you build a tiny copy of how n8n fills these in. The `render` function at the bottom of the starter is **given**: it finds each `{{ ... }}`, hands what's inside (like `$json.sender.name`) to your `value_of`, and puts the answer in its place. You write the two helpers.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"a.b.c".split(".")` | "split at the dots" | cuts the text at every dot: `["a", "b", "c"]` |
| `value = value[key]` | "value becomes value at key" | goes one box deeper and keeps the inner box |
| `s.startswith("$('")` | "s starts with dollar, bracket, quote" | true if the text begins with exactly those characters |
| `s.index("')")` | "index of quote-bracket" | the **position** where `')` first appears. Positions count from 0. |
| `s[3:9]` | "s from 3 up to 9" | a **slice**: the characters from position 3 up to, but not including, position 9 |
| `s[6:]` | "s from 6 to the end" | everything from position 6 on |
| `len("$json.")` | "length of dollar json dot" | `6`: how many characters that text has. Using `len(...)` saves you counting by hand. |
| `str(x)` | "string of x" | turns any value into text: `str(3)` is `"3"`, `str(True)` is `"True"` |

### 👀 Worked example 1: following a path

```python
def follow(value, path):
    for key in path.split("."):
        value = value[key]
    return value

data = {"pet": {"name": "Momo", "age": 3}}
print(follow(data, "pet.name"))
```

1. `"pet.name".split(".")` is `["pet", "name"]`.
2. `key` = `"pet"`: `value` becomes `data["pet"]`, which is `{"name": "Momo", "age": 3}`.
3. `key` = `"name"`: `value` becomes that dictionary's `["name"]`, which is `"Momo"`.
4. Returns `"Momo"`.

This is exactly your first function. Type it as it is.

### 👀 Worked example 2: cutting text with positions

Take `expr = "$('Read Email').item.json.subject"`. Number the characters from 0:

| position | 0 | 1 | 2 | 3 … 12 | 13 | 14 | 15 … |
|---|---|---|---|---|---|---|---|
| character | `$` | `(` | `'` | `Read Email` | `'` | `)` | `.item.json.subject` |

1. `expr.startswith("$('")` → true: it's the node form.
2. `end = expr.index("')")` → **13**, where `')` starts.
3. `name = expr[3:end]` = `expr[3:13]` → `"Read Email"`. Position 3 is the first letter after `$('`.
4. After the name comes `').item.json.` (13 characters). So the path starts at `end + len("').item.json.")` = 13 + 13 = 26: `expr[26:]` → `"subject"`.

For the simple form, `expr = "$json.sender.name"`: `expr[len("$json."):]` = `expr[6:]` → `"sender.name"`.

## 🎯 Your quest

**Part 1:** `follow(value, path)`. Replace `return value` with worked example 1:

1. `for key in path.split("."):`
2. `    value = value[key]`
3. `return value`

**Part 2:** `value_of(expr, item, nodes)`. `nodes` is a dictionary: node name → that node's json. Replace `return ""` with:

1. `if expr.startswith("$('"):`
2. `    end = expr.index("')")`
3. `    name = expr[3:end]`
4. `    path = expr[end + len("').item.json."):]`
5. `    return str(follow(nodes[name], path))`
6. `return str(follow(item, expr[len("$json."):]))`

Don't change `render`. When both parts work, the example at the bottom prints `Anna <anna@x.de>: Hi there`.

<details><summary>Curious how render works?</summary><code>re</code> is Python's search-pattern toolbox. <code>re.sub(pattern, fill, text)</code> finds every piece of <code>text</code> that matches the pattern and replaces it with what <code>fill</code> returns. The pattern <code>\{\{\s*(.*?)\s*\}\}</code> means: two <code>{</code>, maybe spaces, then <b>remember</b> anything (that's the bracket part), maybe spaces, two <code>}</code>. <code>match.group(1)</code> is the remembered part. You'll meet patterns again in Data cleaning.</details>

**Remember:** `{{ }}` = "fill in from the data", `$json` = this item.

## Review

<details><summary>Lesson 2: a node gets 4 items. How often does a "Send message" node run?</summary>4 times, once per item.</details>
<details><summary>What is "hello"[1:3]?</summary>"el": positions 1 and 2 (h is position 0, and 3 is not included).</details>
