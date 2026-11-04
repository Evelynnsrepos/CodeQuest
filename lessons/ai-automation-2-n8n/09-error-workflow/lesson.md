---
title: Error workflows: know when it broke
xp: 25
---
# A workflow that watches the others

⏱️ About 10 minutes · one function

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

## 🎯 Your quest

Write `error_alert(data)` that returns the message text:

- normal error: `"❌ Morning summary failed at Ollama Chat Model: connect ECONNREFUSED"`, plus a new line with the `url` if there is one
- trigger error (no `execution`, but `trigger`): `"❌ Morning summary failed at its trigger: <trigger error message>"`

<details><summary>💡 Hint</summary>Use <code>.get()</code> for things that might be missing: <code>ex = data.get("execution")</code>, <code>url = ex.get("url")</code>. Add <code>"\n" + url</code> only <code>if url</code>.</details>

**Remember:** one error workflow, selected everywhere, tells you on day 1.

## Review

<details><summary>Lesson 8: what's the first thing to do when a small model won't give clean JSON?</summary>Force the format (Structured Output Parser or a JSON schema), then still extract and validate in code.</details>
