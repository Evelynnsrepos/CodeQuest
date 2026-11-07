---
title: Triggers: watch a folder
minutes: 20
xp: 25
hint: Start with an empty list: found = []
hint: Loop over the new snapshot: for name in now: and inside it if before.get(name) != now[name]: then found.append(name)
hint: After the loop: return sorted(found)
---
# Start when something new shows up

⏱️ About 20 minutes · one function, five lines

> **Warm-up:** you drop scanned receipts into a folder. How does your script know which ones are new since last time?

**In one sentence:** a folder trigger compares a **snapshot** from last time with a snapshot from now and handles only what's new or changed.

## 🪜 Plain words

Every file has a **modification time** ("mtime"): a number that says when it last changed. A bigger number means later. A **snapshot** is a dictionary `{filename: mtime}`: a photo of the folder at one moment.

Compare the old photo (`before`) with the new one (`now`):

- In `now` but not in `before` → **new**.
- In both, but the mtime is different → **changed**.
- In `before` but not in `now` → deleted (we ignore those here).

A clock only gives a schedule ("every day at 8"; LLMs 9, lesson 10, covers that). A trigger like this reacts to **events** instead, and does nothing when nothing happened.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `found = []` | "found becomes an empty list" | a new, empty list |
| `for name in now:` | "for each name in now" | looping over a dictionary gives you its **keys**, one at a time |
| `now[name]` | "now at name" | the value for that key: here, the mtime |
| `before.get(name)` | "before get name" | the value for that key, or `None` if `before` doesn't have it (a new file) |
| `!=` | "is not equal to" | true when the two sides are different. `None != 5` is true. |
| `found.append(name)` | "found append name" | adds `name` to the end of the list |
| `sorted(found)` | "sorted found" | a copy of the list in alphabetical order |

### 👀 Worked example: prices that went up or are new

Same shape: compare two dictionaries, keep the keys whose value is new or different.

```python
def new_prices(last_week, this_week):
    found = []
    for item in this_week:
        if last_week.get(item) != this_week[item]:
            found.append(item)
    return sorted(found)

print(new_prices({"milk": 1, "tea": 3}, {"tea": 4, "milk": 1, "bread": 2}))
```

Round by round through `this_week`:

1. `item` = `"tea"`: `last_week.get("tea")` is 3, `this_week["tea"]` is 4. 3 != 4 is true → add `"tea"`.
2. `item` = `"milk"`: 1 != 1 is false → skip.
3. `item` = `"bread"`: `last_week.get("bread")` is `None` (it wasn't there). `None != 2` is true → add `"bread"`.
4. `found` is `["tea", "bread"]`. `sorted` gives `["bread", "tea"]`.

## 🎯 Your quest

Write `changed_files(before, now)`. It's the worked example with other names. Replace the starter's last line with:

1. `found = []`
2. `for name in now:`
3. `    if before.get(name) != now[name]:`
4. `        found.append(name)`
5. `return sorted(found)`

- `changed_files({"a.jpg": 1}, {"a.jpg": 1, "b.jpg": 5})` → `["b.jpg"]`
- `changed_files({"a.jpg": 1}, {"a.jpg": 2})` → `["a.jpg"]`

## 🖥️ On your computer

Take a real snapshot of a folder called `inbox`:

```python
import pathlib

now = {}
for p in pathlib.Path("inbox").iterdir():
    now[p.name] = p.stat().st_mtime
```

Save it with `json.dump` at the end of each run and load it at the start of the next. Run the script every few minutes with a systemd timer (NixOS: `systemd.timers` in your config) or Windows Task Scheduler.

**Remember:** snapshot, compare, handle only the difference.

## Review

<details><summary>Lesson 6: in a router, who decides, and who acts?</summary>The model decides the label; your code calls the handler.</details>
<details><summary>What does before.get(name) give for a brand new file?</summary>None, because before doesn't have that key. None is different from any mtime, so the file counts as new.</details>
