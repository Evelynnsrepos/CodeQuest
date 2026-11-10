---
title: Checkpoint: your inbox helper
minutes: 40
xp: 60
hint: Step 1 inside the loop: if email["id"] in done: then result["skipped"] = result["skipped"] + 1 and continue
hint: Step 2: prompt = "Answer with one word from: spam, reply, other.\n\n" + email["text"], then label = llm(prompt).strip().lower().strip(".")
hint: Step 3 and 4: if label == "spam": result["run_now"].append({"tool": "archive", "id": email["id"]}), elif label == "reply": result["ask_first"].append({"tool": "send_reply", "id": email["id"]})
hint: Step 5, last line in the loop (8 spaces): done.add(email["id"])
---
# Put the pieces together

⏱️ About 40 minutes · one bigger function, built from small steps you already know

> **Warm-up:** which lessons do you need for "every 10 minutes, sort my new emails, archive spam by itself, and draft replies I approve"?

**In one sentence:** a real automation is the small pieces from this course in one loop: skip done items, label with the model, gate risky actions, mark done.

## 🐍 Python you need

Everything here is from lessons 3, 8 and 9. One new piece:

| You write | Say it | What it does |
|---|---|---|
| `elif label == "reply":` | "else if label is reply" | checked only when the `if` above it was false. You can chain several. If none is true, nothing happens. |
| `result["run_now"].append(x)` | "result's run-now list, append x" | `result["run_now"]` is a list inside the dictionary. `.append` adds to that list. |
| `result["skipped"] = result["skipped"] + 1` | | adds one to the number stored under `"skipped"` |
| `{"tool": "archive", "id": email["id"]}` | | builds a new small dictionary for one action |

### 👀 Worked example: if, elif, and nothing

```python
def plan(label):
    if label == "spam":
        return "archive"
    elif label == "reply":
        return "send_reply"
    return None
```

- `plan("spam")`: the `if` is true → `"archive"`.
- `plan("reply")`: the `if` is false, the `elif` is true → `"send_reply"`.
- `plan("other")`: both false → `None`, no action. Notice that an unknown label like `"maybe spam"` also lands here, so you don't even need a separate `"other"` fallback for it.

## 🎯 Your quest

Write `inbox_helper(emails, llm, done)`. Each email is a dict `{"id": ..., "text": ...}`. `done` is a set of IDs (change it in place). The checks test the steps one by one, so tick them off as they work.

Return a dict `{"run_now": [...], "ask_first": [...], "skipped": n}` with the actions in email order and `n` the number of emails skipped because they were done. The starter already has the `result = ...` line and the `return result` line. Between them, type:

```
for email in emails:
```

Then, inside the loop (8 spaces), the five steps:

1. **Skip** (lesson 8):
   - `if email["id"] in done:`
   - `    result["skipped"] = result["skipped"] + 1`
   - `    continue`
2. **Label** (lesson 3):
   - `prompt = "Answer with one word from: spam, reply, other.\n\n" + email["text"]`
   - `label = llm(prompt).strip().lower().strip(".")`
3. and 4. **Plan and gate** (lesson 9): spam is archived alone, replies wait for you, anything else gets no action:
   - `if label == "spam":`
   - `    result["run_now"].append({"tool": "archive", "id": email["id"]})`
   - `elif label == "reply":`
   - `    result["ask_first"].append({"tool": "send_reply", "id": email["id"]})`
5. **Mark** (lesson 8), also for emails with no action:
   - `done.add(email["id"])`

## 🖥️ Make it real

On your computer, add the pieces you already know: the LM Studio `llm` from lesson 3, a snapshot or `done.json` saved between runs (lessons 7 and 8), `execute(..., dry_run=True)` for the `run_now` list until you trust it (lesson 10), and a budget if you use a cloud model (lesson 11). Then start it with a timer (LLMs 9, lesson 10, has cron). Read real mail with Python's `imaplib`. Use an app password, never your main password, and keep it out of the code (AI engineer 3, lesson 01).

**Remember:** skip, label, plan, gate, mark. Small pieces, one loop.

## Review

<details><summary>Lesson 1: why round the payback up?</summary>A payback of 4.1 weeks is only reached in week 5.</details>
<details><summary>Lesson 5: why split one big prompt into a pipeline?</summary>So each small step can be tested, and you know which one failed.</details>
<details><summary>Lesson 11: 4,000 characters at $3 per million input tokens, no reply. Cost?</summary>4,000 ÷ 4 = 1,000 tokens. 1,000 ÷ 1,000,000 × 3 = $0.003.</details>
