---
title: Checkpoint: a safe nightly agent
xp: 90
---
# Put the safety pieces together

> **Warm-up:** an agent should review new GitHub issues every night and suggest labels. List every safety piece from this course that it needs.

You'll write the decision core of a nightly automation: is it due, which tool calls may run, and is the model's answer usable.

## 🪜 The plan

1. **Due?** cron `0 2 * * *` (02:00 every day), lesson 10.
2. **Least privilege + trifecta:** only the tools it needs; issues are untrusted, so no outbound tool unless you approve (lesson 09).
3. **Permissions:** every tool call goes through deny → ask → allow (lesson 04). In a headless run, "ask" means **deny** (`dontAsk`).
4. **Output check:** the answer must match the schema (lesson 08), otherwise skip that issue.

## 🔀 What if it were different?

<div class="wrong"><b>"ask" treated as allow in a nightly run</b>: everything not explicitly denied runs unattended.</div>
<div class="wrong"><b>Label from an unvalidated reply</b>: one malformed answer and the script crashes, or applies a label like "ignore previous instructions".</div>
<div class="right">due → filtered tools → deny/ask/allow with ask = deny → validated output ✓</div>

## 🎯 Your quest

Your earlier functions are given: `cron_due`, `decide`, `validate`.

`nightly(now, calls, replies, rules, schema)`:

- `now` is `(minute, hour, day, month, weekday)`. If `cron_due("0 2 * * *", *now)` is false, return `None`.
- `calls` is a list of `(tool, command)` pairs the agent wants. Return a dict with:
  - `"ran"`: the calls whose decision is `"allow"`,
  - `"blocked"`: all the others (`"ask"` counts as blocked, as in `dontAsk`),
  - `"labels"`: for each reply string in `replies`, `json.loads` it and keep the `"label"` value if `validate` gives no errors; skip broken or invalid replies.

You've finished LLMs 9. Next: try the guide's learning checklist on your own machine.

## Review

<details><summary>Hook exit code that blocks?</summary>2, with the reason on stderr.</details>
<details><summary>Where does auto memory live?</summary>~/.claude/projects/&lt;project&gt;/memory/, with a MEMORY.md index.</details>
<details><summary>Speculative decoding speed-up formula?</summary>(1 − α^(k+1)) / (1 − α), divided by (1 + k·c).</details>
