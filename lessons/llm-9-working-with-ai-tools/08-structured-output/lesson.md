---
title: Structured output: JSON you can trust
xp: 55
---
# Make the next step able to read the answer

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

## 🎯 Your quest

1. `validate(obj, schema)`: return a list of error strings (empty = valid). Support: `type` (`"object"`, `"string"`, `"number"`, `"integer"`, `"boolean"`, `"array"`), `required` (list of keys), `properties` (validate each present key with its sub-schema), `enum` (allowed values). Booleans are **not** numbers or integers.
2. `first_valid(replies, schema, max_tries=3)`: `replies` are raw strings; try `json.loads` on each of the first `max_tries`; return the first parsed object with no errors, or `None`.

**Remember:** a format you can't check is a guess.

## Review

<details><summary>Where should the question go in a long prompt?</summary>At the end, after the documents.</details>
