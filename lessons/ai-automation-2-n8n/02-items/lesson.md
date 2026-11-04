---
title: Items: how data flows
xp: 25
---
# Every node gets a list

⏱️ About 10 minutes · two small functions

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

## 🎯 Your quest

1. `to_items(rows)`: turn a list of dicts into n8n items: `[{"json": row} for row in rows]`.
2. `run_node(items, fn)`: simulate a node that runs once per item: call `fn(item["json"])` for each item and return the results as new items.

<details><summary>💡 Hint</summary><code>return [{"json": fn(item["json"])} for item in items]</code></details>

## 🖥️ In n8n

Click any node after a run and switch the output view between **Table**, **JSON** and **Schema**. The JSON view shows exactly these lists.

**Remember:** a list of `{"json": ...}`, one run per item.

## Review

<details><summary>Lesson 1: n8n runs in Docker and LM Studio on your desktop. Which host?</summary><code>host.docker.internal</code></details>
