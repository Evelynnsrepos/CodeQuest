---
title: Many files, one bad apple
minutes: 20
xp: 25
hint: Start with two empty dictionaries: results = {} and on the next line errors = {}
hint: Loop: for name, text in files.items(): and inside it first skip empty files: if text.strip() == "": then continue
hint: Then try: results[name] = handle(text), and except Exception as e: errors[name] = str(e)
hint: After the loop (back at 4 spaces): return results, errors
---
# A batch that keeps going

⏱️ About 20 minutes · one function

> **Warm-up:** your script summarizes 200 notes overnight. Note 37 is broken and the script crashes. How many summaries do you have in the morning?

**In one sentence:** a batch job handles each item on its own, **writes down** the ones that fail, and keeps going.

## 🪜 Plain words

- **Loop** over the files: do the same work once for every file.
- Put the work for **one** file inside `try:`. If it fails, `except` catches the error, writes it down, and the loop goes on with the next file.
- **Skip** empty files (nothing in them, or only spaces). Sending them to a model wastes time and money.

At the end you have two piles: **results** and **errors**. In the morning you look at the errors pile instead of starting from zero.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `results = {}` | "results becomes an empty dictionary" | a new, empty dictionary (name → value pairs) |
| `for name, text in files.items():` | "for each name and text in files' items" | goes through the dictionary one pair at a time. Each time, the key goes into `name` and the value into `text`. The lines under it (4 more spaces) run once per pair. |
| `text.strip() == ""` | "text stripped equals empty" | true when the text is empty or only spaces. `""` is an empty text. |
| `continue` | "continue" | skip the rest of the loop for **this** item and go on with the next one |
| `results[name] = x` | "results at name becomes x" | puts the pair `name → x` into the dictionary |
| `try:` / `except Exception as e:` | "try / except any error as e" | if a line in `try` fails, jump to `except` instead of crashing. `Exception` means "any kind of error". |
| `str(e)` | "string of e" | the error's message as text, like `"can't read this file"` |
| `return a, b` | "return a and b" | gives back **two** things at once, as a pair |

### 👀 Worked example: same shape, other work

This divides 100 by each number. Dividing by 0 fails, so it goes on the errors pile:

```python
def divide_all(numbers):
    answers = {}
    problems = {}
    for name, n in numbers.items():
        if n == 1:
            continue
        try:
            answers[name] = 100 / n
        except Exception as e:
            problems[name] = str(e)
    return answers, problems
```

`divide_all({"a": 4, "b": 0, "c": 1})`, one round of the loop at a time:

1. `name` = `"a"`, `n` = 4. Not 1. `100 / 4` works: `answers` is now `{"a": 25.0}`.
2. `name` = `"b"`, `n` = 0. `100 / 0` fails with the message `"division by zero"`. Python jumps to `except`: `problems` is now `{"b": "division by zero"}`. The loop **keeps going**.
3. `name` = `"c"`, `n` = 1. The `if` is true, `continue` skips it.
4. After the loop: it returns `({"a": 25.0}, {"b": "division by zero"})`.

## 🎯 Your quest

Press **Run** first: the starter crashes on `b.md`, just like the warm-up. Now fix it.

Write `run_batch(files, handle)`. `handle(text)` does the work for one file (in real life: a model call). Replace the starter's function body with:

1. `results = {}`
2. `errors = {}`
3. `for name, text in files.items():`
4. `    if text.strip() == "":`
5. `        continue`
6. `    try:`
7. `        results[name] = handle(text)`
8. `    except Exception as e:`
9. `        errors[name] = str(e)`
10. `return results, errors` (back at 4 spaces, after the loop)

The spaces in front show which line belongs inside what. Count them carefully: 4 inside the function, 8 inside the loop, 12 inside `if`, `try` and `except`.

## 🖥️ On your computer

Read a real folder of notes into a dictionary:

```python
import pathlib

files = {}
for p in pathlib.Path("notes").glob("*.md"):
    files[p.name] = p.read_text()
```

`glob("*.md")` finds every file ending in `.md`.

**Remember:** one item per `try`, keep a pile of errors, never let one file stop the rest.

## Review

<details><summary>Lesson 3: why does the prompt list the allowed answers?</summary>So the model knows the exact words you can check for in code.</details>
<details><summary>What does continue do inside a loop?</summary>It skips the rest of the loop for this item and goes straight to the next one.</details>
