---
title: Prompt templates
xp: 20
---
# Write the prompt once, fill it in many times

⏱️ About 10 minutes · one function

> **Warm-up:** you want the AI to summarize 50 meeting notes. Do you type 50 prompts?

**In one sentence:** an automation keeps the prompt as a **template** with blanks, and your code fills the blanks for every item.

## 🪜 Plain words

Python strings have a `format` method. `{name}` in the text is a blank, and you fill it by name:

```python
template = "Summarize this note from {date} in {words} words:\n{note}"
prompt = template.format(date="Monday", words=30, note="We agreed to ...")
```

If you have the values in a dictionary, `**` unpacks it into names: `template.format(**fields)`.

## 🔀 What if it were different?

<div class="wrong"><b>A blank has no value</b>: <code>"{date}".format()</code> raises <code>KeyError: 'date'</code>. At 3 a.m. in a batch of 200 notes, that message is confusing.</div>
<div class="right">Catch it and raise a clear error that names the missing field ✓</div>

A `KeyError` carries the missing key: `except KeyError as e:` then `e.args[0]` is `"date"`.

## 🎯 Your quest

Write `fill(template, fields)`:

- return `template.format(**fields)`
- if a field is missing, raise `ValueError("missing field: date")` (with the real field name)

<details><summary>💡 Hint</summary>
<pre>try:
    return template.format(**fields)
except KeyError as e:
    raise ValueError(f"missing field: {e.args[0]}")</pre>
</details>

## 🖥️ On your computer

Keep your templates in `.txt` files next to the script (`open("summary.txt").read()`), so you can improve the prompt without touching the code.

**Remember:** one template, many fills, clear errors.

## Review

<details><summary>Lesson 1: 1 minute saved, 10 runs a week, 1 hour to build. Payback?</summary>60 ÷ 10 = 6 weeks.</details>
