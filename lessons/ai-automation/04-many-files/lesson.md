---
title: Many files, one bad apple
xp: 25
---
# A batch that keeps going

⏱️ About 10 minutes · one function

> **Warm-up:** your script summarizes 200 notes overnight. Note 37 is broken and the script crashes. How many summaries do you have in the morning?

**In one sentence:** a batch job handles each item on its own, **writes down** the ones that fail, and keeps going.

## 🪜 Plain words

- Loop over the items. A dictionary `{filename: text}` gives you both with `for name, text in files.items():`.
- Put the work for **one** item inside `try:`. If it fails, `except Exception as e:` catches the error so the loop continues. Save `str(e)` so you can see later what went wrong.
- **Skip** empty files (only spaces or nothing): `text.strip() == ""`. Sending them to a model wastes time and money.

At the end you have two piles: results and errors. Look at the errors pile in the morning instead of starting from zero.

## 🎯 Your quest

Press **Run** first: the starter crashes on `b.md`, just like the warm-up. Now fix it.


Write `run_batch(files, handle)`. `handle(text)` does the work for one file (in real life: a model call).

- Return a pair `(results, errors)`, two dictionaries keyed by filename.
- `results[name] = handle(text)` when it works.
- `errors[name] = str(e)` when `handle` raises.
- Empty or whitespace-only files go in neither.

<details><summary>💡 Hint</summary>
<pre>results, errors = {}, {}
for name, text in files.items():
    if not text.strip():
        continue
    try:
        results[name] = handle(text)
    except Exception as e:
        errors[name] = str(e)
return results, errors</pre>
</details>

## 🖥️ On your computer

Read a real folder with `pathlib`: `files = {p.name: p.read_text() for p in pathlib.Path("notes").glob("*.md")}`.

**Remember:** one item per `try`, keep a pile of errors, never let one file stop the rest.

## Review

<details><summary>Lesson 3: why does the prompt list the allowed answers?</summary>So the model knows the exact words you can check for in code.</details>
