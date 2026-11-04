---
title: Automation: headless runs on a schedule
xp: 55
---
# The agent loop, started by a clock

> **Warm-up:** you want a summary of yesterday's notes every weekday at 7:30. What starts the agent, and what stops it running forever?

**In one sentence:** automation runs the agent from a trigger (cron, a git push, a file change) in **headless** mode, with limits, narrow permissions and a computer-checkable result.

## 🪜 Plain words

**Headless Claude Code:** `claude -p "prompt"` runs once and exits. Useful flags (checked against the CLI docs):

| Flag | What it does |
|---|---|
| `--output-format json` | machine-readable result (`text`, `json`, `stream-json`) |
| `--max-turns 10` | stop after 10 agent turns |
| `--allowedTools "Read" "Bash(git log *)"` | these run without asking |
| `--permission-mode dontAsk` | anything not pre-allowed is **denied** instead of waiting for you |
| `--max-budget-usd 0.50` | stop when estimated spend reaches this |

**Cron** schedules with 5 fields: `minute hour day-of-month month day-of-week`. `30 7 * * 1-5` = 7:30, Monday to Friday. `*/15 * * * *` = every 15 minutes.

**Patterns, simplest first:** single call → fixed chain → router → parallel → evaluator loop → full agent. Most automations should stay at the first two.

## 🪜 With numbers

```
30 7 * * 1-5  claude -p "Summarize yesterday's notes in notes/" --output-format json --max-turns 5 --allowedTools Read Glob --permission-mode dontAsk
```

Tuesday 07:30 → runs. Saturday 07:30 → no (6 isn't in 1-5). Tuesday 07:31 → no.

## 🔀 What if it were different?

<div class="wrong"><b>No --max-turns</b>: a confused agent loops until the money or the night runs out.</div>
<div class="wrong"><b>Default permission mode in cron</b>: the run stops at the first prompt and waits forever for a human who's asleep. Use <code>dontAsk</code> plus exact allow rules.</div>
<div class="wrong"><b><code>* 7 * * 1-5</code></b> instead of <code>30 7 …</code>: runs 60 times every morning.</div>
<div class="right">a specific schedule, -p with JSON output, turn and budget limits, only the tools it needs ✓</div>

## 🎯 Your quest

1. `headless_args(prompt, allowed, max_turns, budget=None)`: return the argument list `["claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns), "--permission-mode", "dontAsk", "--allowedTools", *allowed]`, and add `"--max-budget-usd", str(budget)` before `--allowedTools` when a budget is given.
2. `field_matches(field, value)`: one cron field: `*`, a number, `a-b` ranges, `*/n` steps, and comma lists of those.
3. `cron_due(expr, minute, hour, day, month, weekday)`: all five fields match (weekday 0 = Sunday).

**Remember:** trigger + limits + narrow permissions + a check.

## Review

<details><summary>The three legs of the lethal trifecta?</summary>Untrusted input, private data, a way to send data out.</details>
