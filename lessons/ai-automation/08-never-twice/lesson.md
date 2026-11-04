---
title: Never do the same work twice
xp: 25
---
# Safe to run again

⏱️ About 10 minutes · one function

> **Warm-up:** your "reply to new emails" script crashes halfway and you run it again. What happens to the emails it already answered?

**In one sentence:** remember **which items are done**, skip them on the next run, and mark an item done only **after** it succeeded.

## 🪜 Plain words

Every item needs a stable **ID** (an email's message ID, a file name). Keep the done IDs in a **set** (`done = set()`), because `id in done` is fast and a set never holds duplicates.

The order matters:

1. Is it in `done`? Skip it.
2. Do the work.
3. Only now: `done.add(id)`.

If step 2 crashes, the item isn't marked, so the next run tries it again. A job you can safely run twice is called **idempotent** (say "eye-dem-POH-tent"). That's the most useful property an automation can have.

## 🎯 Your quest

Write `process_new(items, done, handle)`:

- `items` is a list of `(id, data)` pairs, `done` is a set of IDs (change it in place), `handle(data)` does the work.
- Skip IDs already in `done`, call `handle(data)` for the others, then add the ID to `done`.
- Return how many items you handled this run.
- If `handle` raises, let the error go up (don't catch it), and that item must **not** be in `done`.

<details><summary>💡 Hint</summary>
<pre>count = 0
for item_id, data in items:
    if item_id in done:
        continue
    handle(data)
    done.add(item_id)
    count += 1
return count</pre>
</details>

## 🖥️ On your computer

Save `done` between runs: `json.dump(sorted(done), f)` and load it with `set(json.load(f))`.

**Remember:** check, work, then mark.

## Review

<details><summary>Lesson 7: how do you spot a changed file?</summary>Its name is in both snapshots but the modification time differs.</details>
