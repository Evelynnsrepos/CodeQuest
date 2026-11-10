---
title: Never do the same work twice
minutes: 20
xp: 25
hint: Start a counter: count = 0, then loop: for item_id, data in items:
hint: Inside the loop, first: if item_id in done: and under it continue
hint: Then three lines inside the loop: handle(data), done.add(item_id), count = count + 1
hint: After the loop: return count
---
# Safe to run again

⏱️ About 20 minutes · one function, seven lines

> **Warm-up:** your "reply to new emails" script crashes halfway and you run it again. What happens to the emails it already answered?

**In one sentence:** remember **which items are done**, skip them on the next run, and mark an item done only **after** it succeeded.

## 🪜 Plain words

Every item needs a stable **ID**: a name that never changes, like an email's message ID or a file name. Keep the done IDs in a **set**. A set is like a list, but it never holds the same thing twice, and asking "is this in it?" is very fast.

The order matters:

1. Is the ID in `done`? Skip it.
2. Do the work.
3. Only now: add the ID to `done`.

If step 2 crashes, step 3 never happens, so the item isn't marked. The next run tries it again. A job you can safely run twice is called **idempotent** (say "eye-dem-POH-tent"). That's the most useful property an automation can have.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `{"mail-1", "mail-2"}` | "a set of mail-1 and mail-2" | a **set**: curly brackets, but only values (no `key: value` pairs). `set()` is an empty set. |
| `("mail-2", "hello")` | "a pair" | a **tuple**: values in round brackets that belong together, here an ID and its data |
| `for item_id, data in items:` | "for each ID and data in items" | each item is a pair. Python unpacks it: the first value goes into `item_id`, the second into `data`. |
| `if item_id in done:` | "if the ID is in done" | true when the set holds that ID |
| `continue` | "continue" | skip the rest of this round, go to the next item |
| `done.add(item_id)` | "done add the ID" | puts the ID into the set. It changes the set you were given, so the caller sees it too. |
| `count = count + 1` | "count becomes count plus one" | adds one to the counter |

### 👀 Worked example: a guest list

Only greet people who haven't been greeted yet, and count the new greetings:

```python
def greet_new(people, greeted):
    count = 0
    for name, age in people:
        if name in greeted:
            continue
        print("Hello", name)
        greeted.add(name)
        count = count + 1
    return count

greeted = {"Ana"}
print(greet_new([("Ana", 30), ("Ben", 25)], greeted))
```

Round by round:

1. Start: `count` = 0, `greeted` = `{"Ana"}`.
2. `name` = `"Ana"`, `age` = 30. `"Ana" in greeted` is true → `continue`, skip.
3. `name` = `"Ben"`, `age` = 25. Not in `greeted`. Prints `Hello Ben`, adds `"Ben"` to `greeted`, `count` becomes 1.
4. Returns `1`. Running it again returns `0`: both are greeted now.

Notice the order: greet first, **then** add to the set.

## 🎯 Your quest

Write `process_new(items, done, handle)`. `handle(data)` does the work for one item. If `handle` crashes, don't catch it: let the error go up, and that item must **not** be in `done`. The order below does that by itself.

Replace the starter's function body with:

1. `count = 0`
2. `for item_id, data in items:`
3. `    if item_id in done:`
4. `        continue`
5. `    handle(data)`
6. `    done.add(item_id)`
7. `    count = count + 1`
8. `return count`

## 🖥️ On your computer

Save `done` between runs in a file:

```python
import json

with open("done.json", "w") as f:
    json.dump(sorted(done), f)       # save at the end

with open("done.json") as f:
    done = set(json.load(f))         # load at the start
```

**Remember:** check, work, then mark.

## Review

<details><summary>Lesson 7: how do you spot a changed file?</summary>Its name is in both snapshots but the modification time differs.</details>
<details><summary>Why mark an item done only after the work?</summary>If the work crashes, the item stays unmarked, so the next run tries it again.</details>
