---
title: Error workflows: know when it broke
minutes: 25
xp: 25
hint: First line: name = data["workflow"]["name"]. Then the trigger case: if "execution" not in data:
hint: Under it: return "❌ " + name + " failed at its trigger: " + data["trigger"]["error"]["message"]
hint: Then: ex = data["execution"] and text = "❌ " + name + " failed at " + ex["lastNodeExecuted"] + ": " + ex["error"]["message"]
hint: Last: if "url" in ex: text = text + "\n" + ex["url"], and then return text
---
# A workflow that watches the others

⏱️ About 25 minutes · one function, eight lines

> **Warm-up:** your morning-summary workflow stopped working 9 days ago because LM Studio wasn't running. How could you have found out on day 1?

**In one sentence:** make one **error workflow** that starts with an **Error Trigger** node and sends you a message, then pick it in every other workflow's settings.

## 🪜 Set it up

1. New workflow: **Error Trigger** → a Telegram, email or ntfy node. Name it "Error Handler" and save it.
2. In each real workflow: **Options → Settings → Error workflow** → "Error Handler".
3. It only fires for **automatic** runs (schedule, webhook…), not when you click "Execute" yourself.

## 🪜 What the Error Trigger gives you

```json
{
  "execution": {"id": "231", "url": "https://n8n.example.com/execution/231",
                "lastNodeExecuted": "Ollama Chat Model",
                "error": {"message": "connect ECONNREFUSED"}},
  "workflow": {"id": "1", "name": "Morning summary"}
}
```

`id` and `url` are only there if the execution was saved. If the **trigger node itself** failed, there's a `trigger` object with `error.message` instead of `execution`.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `data["workflow"]["name"]` | "data's workflow's name" | two lookups: the `workflow` dictionary, then its `name` |
| `"execution" in data` | "execution is in data" | true when the dictionary has that **key**. Use it before reading something that might be missing. |
| `"execution" not in data` | "execution is not in data" | the opposite |
| `"❌ " + name + " failed"` | | glues texts together |
| `"\n"` | "newline" | a line break inside a text |
| `text = text + "more"` | | adds more text to the end of what's in the box |

### 👀 Worked example: a parcel message

```python
def parcel_text(p):
    who = p["to"]["name"]
    if "delivery" not in p:
        return "📦 " + who + ": not sent yet"
    d = p["delivery"]
    text = "📦 " + who + ": at " + d["place"]
    if "photo" in d:
        text = text + "\n" + d["photo"]
    return text
```

- `{"to": {"name": "Ana"}}`: no `"delivery"` key → `"📦 Ana: not sent yet"`.
- `{"to": {"name": "Ana"}, "delivery": {"place": "door"}}`: `text` = `"📦 Ana: at door"`. No `"photo"`, so that's it.
- With `"photo": "pic.jpg"` too: a line break and `pic.jpg` are added on a second line.

## 🎯 Your quest

Write `error_alert(data)`. Replace the starter's line with:

1. `name = data["workflow"]["name"]`
2. The trigger case (no `execution`):
   - `if "execution" not in data:`
   - `    return "❌ " + name + " failed at its trigger: " + data["trigger"]["error"]["message"]`
3. The normal case:
   - `ex = data["execution"]`
   - `text = "❌ " + name + " failed at " + ex["lastNodeExecuted"] + ": " + ex["error"]["message"]`
   - `if "url" in ex:`
   - `    text = text + "\n" + ex["url"]`
   - `return text`

It gives `"❌ Morning summary failed at Ollama Chat Model: connect ECONNREFUSED"` and, on the next line, the URL.

**Remember:** one error workflow, selected everywhere, tells you on day 1.

## Review

<details><summary>Lesson 8: what's the first thing to do when a small model won't give clean JSON?</summary>Force the format (Structured Output Parser or a JSON schema), then still extract and validate in code.</details>
<details><summary>Why check "url" in ex before reading ex["url"]?</summary>The url is only there when the execution was saved. Reading a missing key would crash the error workflow itself.</details>
