---
title: Automation: headless runs on a schedule
minutes: 45
xp: 55
hint: headless_args: args = [...the first nine items...], then if budget is not None: append "--max-budget-usd" and str(budget)
hint: headless_args: args.append("--allowedTools"), then for tool in allowed: args.append(tool)
hint: field_matches: for part in field.split(","): and check "*", then "*/" steps with value % step == 0, then ranges, then a plain number
hint: Ranges: ends = part.split("-"), low = int(ends[0]), high = int(ends[1]), then if low <= value and value <= high: return True
hint: cron_due: fields = expr.split(), values = [minute, hour, day, month, weekday], then for i in range(5): if not field_matches(fields[i], values[i]): return False
---
# The agent loop, started by a clock

⏱️ About 45 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `str(5)` | "string of 5" | `"5"`. A command line is made of texts only. |
| `if budget is not None:` | "if a budget was given" | `None` means "nothing". `is not None` is true when there is a value. |
| `args.append(x)` | | adds one more item at the end |
| `field.split(",")` | "split at commas" | `"0,30"` → `["0", "30"]`. Without a comma: `["0"]`, one part. |
| `part.startswith("*/")` | | true for `"*/15"` |
| `int(part[2:])` | "int of part from 2" | `"*/15"`[2:] is `"15"`, `int` turns the text into the number 15 |
| `value % step` | "value modulo step" | the **remainder** after dividing: `45 % 15` is 0 (45 = 3 × 15), `50 % 15` is 5 (50 = 3 × 15 + 5). Remainder 0 means "divides evenly". |
| `elif` | "else if" | only checked when the `if` above was false |
| `low <= value and value <= high` | "low at most value, and value at most high" | true when value is in the range, **both ends included** |
| `for i in range(5):` | | `i` = 0, 1, 2, 3, 4: lets you walk two lists side by side with `fields[i]` and `values[i]` |

### 👀 Worked example: does `"1-5,10"` match 10?

1. `"1-5,10".split(",")` → `["1-5", "10"]`.
2. `part` = `"1-5"`: not `*`, doesn't start with `*/`, has a `-` → `ends` = `["1", "5"]`, `low` = 1, `high` = 5. Is 1 ≤ 10 and 10 ≤ 5? No (10 > 5). Next part.
3. `part` = `"10"`: no `*`, no `*/`, no `-` → the last `elif`: `int("10") == 10` → return `True`.

And the whole cron line `"30 7 * * 1-5"` on Tuesday 07:30 (minute 30, hour 7, day 4, month 11, weekday 2):

| i | fields[i] | values[i] | match? |
|---|---|---|---|
| 0 | `30` | 30 | yes |
| 1 | `7` | 7 | yes |
| 2 | `*` | 4 | yes |
| 3 | `*` | 11 | yes |
| 4 | `1-5` | 2 | yes |

No field said no, so the loop ends and `return True` runs. On Saturday (weekday 6), row 4 says no → `return False` right away.

## 🎯 Your quest

1. `headless_args(prompt, allowed, max_turns, budget=None)`: return the argument list `["claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns), "--permission-mode", "dontAsk", "--allowedTools", *allowed]`, and add `"--max-budget-usd", str(budget)` before `--allowedTools` when a budget is given.
2. `field_matches(field, value)`: one cron field: `*`, a number, `a-b` ranges, `*/n` steps, and comma lists of those.
3. `cron_due(expr, minute, hour, day, month, weekday)`: all five fields match (weekday 0 = Sunday).

**Part 1:** `headless_args`. Replace `return ["claude", prompt]` with:

1. `args = ["claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns), "--permission-mode", "dontAsk"]`
2. `if budget is not None:`
3. `    args.append("--max-budget-usd")`
4. `    args.append(str(budget))`
5. `args.append("--allowedTools")`
6. `for tool in allowed:`
7. `    args.append(tool)`
8. `return args`

**Part 2:** `field_matches`. Replace `return True` with:

1. `for part in field.split(","):`
2. `    if part == "*":`
3. `        return True`
4. `    if part.startswith("*/"):`
5. `        step = int(part[2:])`
6. `        if value % step == 0:`
7. `            return True`
8. `    elif "-" in part:`
9. `        ends = part.split("-")`
10. `        low = int(ends[0])`
11. `        high = int(ends[1])`
12. `        if low <= value and value <= high:`
13. `            return True`
14. `    elif int(part) == value:`
15. `        return True`
16. `return False`

**Part 3:** `cron_due`. Replace `return True` with:

1. `fields = expr.split()`
2. `values = [minute, hour, day, month, weekday]`
3. `for i in range(5):`
4. `    if not field_matches(fields[i], values[i]):`
5. `        return False`
6. `return True`

**Remember:** trigger + limits + narrow permissions + a check.

## Review

<details><summary>The three legs of the lethal trifecta?</summary>Untrusted input, private data, a way to send data out.</details>
