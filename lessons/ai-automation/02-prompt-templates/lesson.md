---
title: Prompt templates
minutes: 15
xp: 20
hint: Start with try: and under it (4 more spaces) return template.format_map(fields)
hint: Next, at the same level as try: write except KeyError as e:
hint: Under the except line: raise ValueError("missing field: " + e.args[0])
---
# Write the prompt once, fill it in many times

⏱️ About 15 minutes · one function, four lines

> **Warm-up:** you want the AI to summarize 50 meeting notes. Do you type 50 prompts?

**In one sentence:** an automation keeps the prompt as a **template** with blanks, and your code fills the blanks for every item.

## 🪜 Plain words

A template is text with **blanks** in curly brackets:

`"Summarize this note from {date} in {words} words: {note}"`

`{date}`, `{words}` and `{note}` are blanks. For every note, your code fills them in with that note's values. The prompt is written once, and you can improve it in one place.

The values come in a **dictionary**: a list of "name → value" pairs, like a little phone book. `{"date": "Monday", "words": 30}` says: the name `date` has the value `"Monday"`, the name `words` has the value `30`.

## 🔀 What if it were different?

<div class="wrong"><b>A blank has no value</b>: the template has <code>{date}</code> but the dictionary has no <code>"date"</code>. Python stops with <code>KeyError: 'date'</code>. At 3 a.m. in a batch of 200 notes, that message is confusing.</div>
<div class="right">Catch that error and raise a clear one that says which field is missing: <code>missing field: date</code> ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `{"name": "Eve", "n": 3}` | "a dictionary: name is Eve, n is 3" | a **dictionary**: pairs of `key: value`, separated by commas, in curly brackets |
| `t.format_map(fields)` | "t format map fields" | fills every `{blank}` in the text `t` with the value of the same name from the dictionary `fields` |
| `try:` | "try" | "try the lines below (4 more spaces). If one of them fails, don't stop the program, jump to `except`." |
| `except KeyError as e:` | "except key error as e" | runs only if a `KeyError` happened in the `try` part. The error is put in a box called `e`. |
| `e.args[0]` | "e's first argument" | for a `KeyError`: the missing name, like `"date"` |
| `"a" + "b"` | "a plus b" | glues two pieces of text: `"ab"` |
| `raise ValueError("...")` | "raise a value error" | stops the function with **your own** error message |

### 👀 Worked example 1: filling a template

```python
fields = {"pet": "cat", "food": "fish"}
text = "My {pet} likes {food}."
print(text.format_map(fields))
```

1. `fields` is a dictionary: `pet` → `"cat"`, `food` → `"fish"`.
2. `format_map` finds the blank `{pet}`, looks up `"pet"` in `fields` and finds `"cat"`. Same for `{food}` → `"fish"`.
3. It prints `My cat likes fish.`

### 👀 Worked example 2: catching an error

```python
def get_price(prices, item):
    try:
        return prices[item]
    except KeyError as e:
        raise ValueError("no price for: " + e.args[0])
```

`prices[item]` looks up a name in a dictionary. `get_price({"tea": 2}, "tea")` gives `2`. `get_price({"tea": 2}, "cake")`:

1. `try:` runs `prices["cake"]`. There's no `"cake"`, so Python makes a `KeyError`.
2. Instead of crashing, it jumps to `except KeyError as e:`. Now `e.args[0]` is `"cake"`.
3. `raise ValueError("no price for: " + "cake")`: the error now says `no price for: cake`.

Your quest has exactly this shape.

## 🎯 Your quest

Write `fill(template, fields)`. Inside the function (4 spaces in front of each line, and 8 for the indented ones):

1. `try:`
2. `    return template.format_map(fields)`
3. `except KeyError as e:`
4. `    raise ValueError("missing field: " + e.args[0])`

Check: `fill("Hi {name}!", {"name": "Eve"})` gives `"Hi Eve!"`, and `fill("From {date}", {})` raises `ValueError: missing field: date`.

## 🖥️ On your computer

Keep your templates in `.txt` files next to the script (`open("summary.txt").read()` gives you the text), so you can improve the prompt without touching the code.

**Remember:** one template, many fills, clear errors.

## Review

<details><summary>Lesson 1: 1 minute saved, 10 runs a week, 1 hour to build. Payback?</summary>Saved per week: 1 × 10 = 10 minutes. Build: 1 × 60 = 60 minutes. 60 ÷ 10 = 6 weeks.</details>
<details><summary>What happens to the lines under try: when one of them fails?</summary>Python stops running them and jumps to the matching except line, instead of crashing the whole program.</details>
