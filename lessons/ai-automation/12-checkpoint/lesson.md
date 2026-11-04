---
title: Checkpoint: your inbox helper
xp: 60
---
# Put the pieces together

⏱️ About 20 minutes · one bigger function, built from small steps

> **Warm-up:** which lessons do you need for "every 10 minutes, sort my new emails, archive spam by itself, and draft replies I approve"?

**In one sentence:** a real automation is the small pieces from this course in one loop: skip done items, label with the model, gate risky actions, mark done.

## 🎯 Your quest

Write `inbox_helper(emails, llm, done)`. Each email is a dict `{"id": ..., "text": ...}`. `done` is a set of IDs (change it in place).

Do it in this order for each email. Tick each step off as it works, the checks test them one by one:

1. **Skip** emails whose ID is in `done` (lesson 8).
2. **Label** it: ask `llm` with a prompt containing the text and `"spam, reply, other"`, clean the reply, fallback `"other"` (lesson 3).
3. **Plan** one action: spam → `{"tool": "archive", "id": id}`, reply → `{"tool": "send_reply", "id": id}`, other → no action.
4. **Gate** (lesson 9): `archive` may run alone, everything else needs approval.
5. **Mark** the email done (lesson 8).

Return a dict `{"run_now": [...], "ask_first": [...], "skipped": n}` with the actions in email order and `n` the number of emails skipped because they were done.

<details><summary>💡 Hint 1: the shape</summary>
<pre>result = {"run_now": [], "ask_first": [], "skipped": 0}
for email in emails:
    ...
return result</pre>
</details>
<details><summary>💡 Hint 2: label to action</summary><code>tool = {"spam": "archive", "reply": "send_reply"}.get(label)</code>. When <code>tool</code> is <code>None</code> there's no action.</details>
<details><summary>💡 Hint 3: gate</summary><code>result["run_now" if tool == "archive" else "ask_first"].append({"tool": tool, "id": email["id"]})</code></details>

## 🖥️ Make it real

On your computer, add the pieces you already know: the LM Studio `llm` from lesson 3, a snapshot or `done.json` saved between runs (lessons 7 and 8), `execute(..., dry_run=True)` for the `run_now` list until you trust it (lesson 10), and a budget if you use a cloud model (lesson 11). Then start it with a timer (LLMs 9, lesson 10, has cron). Read real mail with Python's `imaplib`. Use an app password, never your main password, and keep it out of the code (AI engineer 3, lesson 01).

**Remember:** skip, label, plan, gate, mark. Small pieces, one loop.

## Review

<details><summary>Lesson 1: why round the payback up?</summary>A payback of 4.1 weeks is only reached in week 5.</details>
<details><summary>Lesson 5: why split one big prompt into a pipeline?</summary>So each small step can be tested, and you know which one failed.</details>
<details><summary>Lesson 11: 4,000 characters at $3 per million input tokens, no reply. Cost?</summary>4,000 ÷ 4 = 1,000 tokens. 1,000 ÷ 1,000,000 × 3 = $0.003.</details>
