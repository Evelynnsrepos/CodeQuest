---
title: Dry runs and logs
minutes: 30
xp: 25
hint: Inside the loop, take the two parts out: name = action["tool"] and args = action["args"]
hint: Build the "key=value" texts: parts = [], then for key in args: and inside it parts.append(key + "=" + repr(args[key]))
hint: if dry_run: prefix = "DRY", else: prefix = "RAN" and on the next line tools[name](**args)
hint: Last line in the loop: log.append(prefix + " " + name + "(" + ", ".join(parts) + ")")
---
# Show what you would do, then do it

⏱️ About 30 minutes · one function, built up in three parts

> **Warm-up:** you wrote a script that renames 300 photos. How do you check it's right **before** it renames anything?

**In one sentence:** a **dry run** goes through every step but only **writes down** the actions, and a **log** says what happened so you can check later.

## 🪜 Plain words

- Default to dry run. You have to say "yes, really" (`dry_run=False`) to change anything. A forgotten setting then does nothing, instead of something bad.
- Write one log line per action, the same in both modes, with a prefix in front: `DRY` (only pretended) or `RAN` (really done):

```
DRY rename(old='a.jpg', new='b.jpg')
RAN rename(old='a.jpg', new='b.jpg')
```

- Show text **with its quotes** (`'a.jpg'`), so you can tell the text `'5'` from the number `5`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `def execute(actions, tools, dry_run=True):` | "dry run is true unless you say otherwise" | an input with a **default**: if the caller doesn't give `dry_run`, it is `True` |
| `True`, `False` | "true", "false" | Python's yes and no. No quotes. |
| `if dry_run:` | "if dry run" | true when `dry_run` is `True` |
| `for key in args:` | "for each key in args" | goes through a dictionary's keys, in order |
| `repr(x)` | "repr of x" | `x` as Python would write it: `repr("a.jpg")` is `'a.jpg'` (with quotes), `repr(5)` is `5` |
| `key + "=" + repr(args[key])` | | glues `old`, `=`, `'a.jpg'` into `old='a.jpg'` |
| `", ".join(parts)` | "comma-space join parts" | `old='a.jpg', new='b.jpg'`. An empty list gives `""`. |
| `tools[name]` | "tools at name" | the function stored under that name |
| `f(**args)` | "f with args unpacked" | the two stars unpack a dictionary into named inputs: with `args = {"old": "a.jpg", "new": "b.jpg"}`, `rename(**args)` is the same as `rename(old="a.jpg", new="b.jpg")` |

### 👀 Worked example: a pretend shopping list

Same shape: build a text for each item, only really "buy" when told to.

```python
def shop(items, really=False):
    log = []
    for item in items:
        name = item["what"]
        details = item["details"]
        parts = []
        for key in details:
            parts.append(key + "=" + repr(details[key]))
        if really:
            prefix = "BOUGHT"
        else:
            prefix = "WOULD BUY"
        log.append(prefix + " " + name + "(" + ", ".join(parts) + ")")
    return log

print(shop([{"what": "milk", "details": {"litres": 2, "brand": "Oat"}}]))
```

For the one item:

1. `name` = `"milk"`, `details` = `{"litres": 2, "brand": "Oat"}`.
2. Inner loop: `key` = `"litres"` → `parts` gets `litres=2`. `key` = `"brand"` → `parts` gets `brand='Oat'` (the text keeps its quotes).
3. `really` is `False` (the default), so the `else` runs: `prefix` = `"WOULD BUY"`.
4. `", ".join(parts)` = `litres=2, brand='Oat'`.
5. The log line: `WOULD BUY milk(litres=2, brand='Oat')`.

Your quest is this, plus one extra line: in the real mode, call the tool.

## 🎯 Your quest

Write `execute(actions, tools, dry_run=True)`. Each action is `{"tool": name, "args": {...}}`, and `tools` maps names to functions. Replace the starter's function body with:

1. `log = []`
2. `for action in actions:`
3. `    name = action["tool"]`
4. `    args = action["args"]`
5. `    parts = []`
6. `    for key in args:`
7. `        parts.append(key + "=" + repr(args[key]))`
8. `    if dry_run:`
9. `        prefix = "DRY"`
10. `    else:`
11. `        prefix = "RAN"`
12. `        tools[name](**args)`
13. `    log.append(prefix + " " + name + "(" + ", ".join(parts) + ")")`
14. `return log`

Line 12 is the only line that really changes something, and it only runs when `dry_run` is `False`.

## 🖥️ On your computer

Write the lines to a file too, so you can read them next week:

```python
import logging
logging.basicConfig(filename="automation.log", level=logging.INFO)
for line in execute(actions, tools):
    logging.info(line)
```

**Remember:** dry run by default, one log line per action.

## Review

<details><summary>Lesson 9: is "send an email" safe to run without asking?</summary>No, you can't unsend it. It goes in the ask-first queue.</details>
<details><summary>What does repr("5") give, and why use it in a log?</summary>'5' with quotes, so you can see it's text and not the number 5.</details>
