---
title: Items: how data flows
minutes: 20
xp: 25
hint: to_items: items = [], then for row in rows: and inside it items.append({"json": row}), then return items
hint: run_node: new_items = [], then for item in items: and inside it result = fn(item["json"])
hint: Still inside run_node's loop: new_items.append({"json": result}). After the loop: return new_items
---
# Every node gets a list

⏱️ About 20 minutes · two small functions

> **Warm-up:** a node reads 3 emails, and the next node is "Send Telegram message". How many messages get sent?

**In one sentence:** in n8n, data moves between nodes as a **list of items**, each item is `{"json": {...}}`, and most nodes run **once per item**.

## 🪜 Plain words

What the email node passes on looks like this:

```json
[
  {"json": {"from": "anna@x.de", "subject": "Hi"}},
  {"json": {"from": "shop@y.com", "subject": "Your order"}},
  {"json": {"from": "boss@work.com", "subject": "Thursday"}}
]
```

Files travel next to `json` under a `binary` key. So the Telegram node sends **3** messages, one per item. That's usually what you want, and the reason for surprise bills when a node gets 500 items you didn't expect.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `[]` | "an empty list" | a list with nothing in it yet |
| `for row in rows:` | "for each row in rows" | goes through the list one value at a time |
| `{"json": row}` | "a dictionary: json is row" | wraps the row into a new dictionary under the key `"json"`. That's one n8n item. |
| `items.append(x)` | "items append x" | adds `x` to the end of the list |
| `item["json"]` | "item at json" | takes the row back out of an item |
| `fn(x)` | "fn of x" | runs the function you were given with `x` |

### 👀 Worked example: wrapping presents

Same shape as both quest functions: start empty, loop, append, return.

```python
def wrap_all(gifts):
    boxes = []
    for gift in gifts:
        boxes.append({"inside": gift})
    return boxes

print(wrap_all(["book", "socks"]))
```

1. `boxes` = `[]`.
2. `gift` = `"book"` → `boxes` = `[{"inside": "book"}]`.
3. `gift` = `"socks"` → `boxes` = `[{"inside": "book"}, {"inside": "socks"}]`.
4. Returns that list.

And unwrapping, changing, wrapping again:

```python
def shout_all(boxes):
    new_boxes = []
    for box in boxes:
        result = box["inside"].upper()
        new_boxes.append({"inside": result})
    return new_boxes
```

`box["inside"]` takes the gift out, `.upper()` makes it uppercase, and it goes into a new box. `run_node` is this, but instead of `.upper()` it calls `fn`.

## 🎯 Your quest

**Part 1:** `to_items(rows)`. Replace `return rows` with:

1. `items = []`
2. `for row in rows:`
3. `    items.append({"json": row})`
4. `return items`

**Part 2:** `run_node(items, fn)` simulates a node that runs once per item. Replace `return items` with:

1. `new_items = []`
2. `for item in items:`
3. `    result = fn(item["json"])`
4. `    new_items.append({"json": result})`
5. `return new_items`

## 🖥️ In n8n

Click any node after a run and switch the output view between **Table**, **JSON** and **Schema**. The JSON view shows exactly these lists.

**Remember:** a list of `{"json": ...}`, one run per item.

## Review

<details><summary>Lesson 1: n8n runs in Docker and LM Studio on your desktop. Which host?</summary><code>host.docker.internal</code></details>
