---
title: Structured output: JSON you can trust
minutes: 50
xp: 55
hint: validate, line 1-3: errors = [], then if "type" in schema and not type_ok(obj, schema["type"]): return [path + ": expected " + schema["type"]]
hint: validate, enum: if "enum" in schema and obj not in schema["enum"]: errors.append(path + ": not one of " + str(schema["enum"]))
hint: validate, the sub-schemas: for key in properties: if key in obj: errors = errors + validate(obj[key], properties[key], path + "." + key)
hint: first_valid: for raw in replies[:max_tries]: then try: obj = json.loads(raw) and except json.JSONDecodeError: continue
hint: first_valid: if validate(obj, schema) == []: return obj. After the loop: return None
---
# Make the next step able to read the answer

⏱️ About 50 minutes

> **Warm-up:** an automation asks a model "is this email spam?" and gets back "Well, it's hard to say, but probably yes!". How does your script use that?

**In one sentence:** ask for JSON that follows a schema, then **validate** it in code and retry (or fail loudly) when it doesn't match.

## 🪜 Plain words

- **JSON schema** describes the shape you want: `{"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}, "reason": {"type": "string"}}}`.
- Many runners can **force** it: OpenAI-style `response_format` with a JSON schema, llama.cpp **grammars** (GBNF) that only allow valid tokens. Small local models especially need this.
- Even then, **validate**. Models (or a truncated reply) can still give you broken JSON. Retry a couple of times with the error message, then give up visibly.

## 🪜 With numbers

Schema: required `spam` (boolean), optional `reason` (string), `label` must be one of `["ham", "spam"]`.

| Reply | Valid? | Why |
|---|---|---|
| `{"spam": true, "reason": "lottery"}` | ✓ | |
| `{"spam": "yes"}` | ✗ | spam must be a boolean |
| `{"reason": "x"}` | ✗ | spam is required |
| `Sure! {"spam": true}` | ✗ | not JSON at all |
| `{"spam": false, "label": "maybe"}` | ✗ | not in the enum |

## 🔀 What if it were different?

<div class="wrong"><b>Trust the reply and do <code>data["spam"]</code></b>: one bad reply crashes the pipeline at 3 a.m., or worse, "yes" is treated as True by accident.</div>
<div class="wrong"><b>Check <code>isinstance(x, int)</code> for numbers</b>: in Python <code>True</code> is an int too. A boolean would pass as a number.</div>
<div class="wrong"><b>Retry forever</b>: a stuck model burns tokens all night. Cap the retries.</div>
<div class="right">parse → validate → retry a few times → fail loudly ✓</div>

## 🐍 Python you need

`type_ok(value, t)` is **given** in the starter: `type_ok(True, "boolean")` is `True`, `type_ok(True, "number")` is `False`. Read it once: the first `if` handles booleans, because in Python `True` also counts as the number 1 and we don't want that.

| You write | Say it | What it does |
|---|---|---|
| `"type" in schema` | "type is in schema" | on a dictionary, `in` checks the **keys** |
| `not type_ok(...)` | "not type OK" | true when the type is wrong |
| `str(["ham", "spam"])` | "string of the list" | the list as text, `"['ham', 'spam']"`, so you can glue it with `+` |
| `isinstance(obj, dict)` | "is obj a dictionary" | true for `{...}` |
| `errors = errors + more` | | adding two lists makes one longer list |
| `validate(obj[key], ...)` inside `validate` | | a function may **call itself** on a smaller piece. Here: check the inside of the object with the inside schema. It stops because the pieces get smaller. |
| `path + "." + key` | | builds names like `$.spam`, so the error says *where* |
| `try:` / `except json.JSONDecodeError:` | "try this, and if it fails with a JSON error, do that" | `json.loads("Sure!")` would crash; `except` catches the crash |
| `continue` | "continue" | skips the rest of this round and goes to the next item |
| `replies[:max_tries]` | | only the first `max_tries` replies |

### 👀 Worked example 1: checking `{"spam": "yes"}`

Schema: `{"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}}}`.

1. `validate(obj, schema)`, `path` = `"$"` (the default: `$` means "the whole thing").
2. Type `"object"`: `obj` is a dictionary → OK.
3. No `"enum"` → skip.
4. Required: `"spam"` is in `obj` → no error.
5. Properties: `key` = `"spam"` is in `obj`, so call `validate("yes", {"type": "boolean"}, "$.spam")`.
6. Inside that call: `"yes"` is not a boolean → it returns `["$.spam: expected boolean"]`.
7. Back outside: `errors = [] + ["$.spam: expected boolean"]`. Returned.

### 👀 Worked example 2: try and except

```python
import json
for raw in ['oops', '{"a": 1}']:
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        print("not JSON:", raw)
        continue
    print("parsed:", obj)
```

1. `'oops'`: `json.loads` fails → the `except` lines run → prints `not JSON: oops` → `continue` jumps to the next item.
2. `'{"a": 1}'`: works → prints `parsed: {'a': 1}`.

## 🎯 Your quest

1. `validate(obj, schema)`: return a list of error strings (empty = valid). Support: `type` (`"object"`, `"string"`, `"number"`, `"integer"`, `"boolean"`, `"array"`), `required` (list of keys), `properties` (validate each present key with its sub-schema), `enum` (allowed values). Booleans are **not** numbers or integers.
2. `first_valid(replies, schema, max_tries=3)`: `replies` are raw strings; try `json.loads` on each of the first `max_tries`; return the first parsed object with no errors, or `None`.

The starter's `validate` already has a third input, `path="$"`. Leave it there.

**Part 1:** `validate`. Replace `return []` with:

1. `errors = []`
2. `if "type" in schema and not type_ok(obj, schema["type"]):`
3. `    return [path + ": expected " + schema["type"]]`
4. `if "enum" in schema and obj not in schema["enum"]:`
5. `    errors.append(path + ": not one of " + str(schema["enum"]))`
6. `if isinstance(obj, dict):`
7. `    for key in schema.get("required", []):`
8. `        if key not in obj:`
9. `            errors.append(path + "." + key + ": required")`
10. `    properties = schema.get("properties", {})`
11. `    for key in properties:`
12. `        if key in obj:`
13. `            errors = errors + validate(obj[key], properties[key], path + "." + key)`
14. `return errors`

**Part 2:** `first_valid`. Replace `return None` with:

1. `for raw in replies[:max_tries]:`
2. `    try:`
3. `        obj = json.loads(raw)`
4. `    except json.JSONDecodeError:`
5. `        continue`
6. `    if validate(obj, schema) == []:`
7. `        return obj`
8. `return None`

**Remember:** a format you can't check is a guess.

## Review

<details><summary>Where should the question go in a long prompt?</summary>At the end, after the documents.</details>
