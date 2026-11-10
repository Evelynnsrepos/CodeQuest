---
title: Settings layers and permission rules
minutes: 45
xp: 60
hint: matches: if "(" not in rule: return rule == tool. Then i = rule.index("("), name = rule[:i], pattern = rule[i + 1:-1]
hint: matches: if pattern.endswith(" *") or pattern.endswith(":*"): prefix = pattern[:-2] and return command == prefix or command.startswith(prefix + " ")
hint: decide: for outcome in ["deny", "ask", "allow"]: then for rule in rules.get(outcome, []): then if matches(rule, tool, command): return outcome
hint: effective: for name in [...]: settings = layers.get(name, {}), then if key in settings: return settings[key]
---
# Who wins when two files disagree?

⏱️ About 45 minutes

> **Warm-up:** your user settings allow `Bash(git push *)`. The project's settings deny it. Can Claude push?

**In one sentence:** Claude Code reads settings from several layers where the most specific wins for single values, but permission rules from all layers are combined and checked in a fixed order: deny, then ask, then allow.

## 🪜 Plain words

**Settings layers** (highest first): **managed** (your organization) → **command line** (`--settings`, one session) → **project local** `.claude/settings.local.json` → **shared project** `.claude/settings.json` → **user** `~/.claude/settings.json`. For a single value like `model`, the highest layer that sets it wins. Lists like `permissions.allow` are **merged** from all layers.

**Permission rules** look like `Tool(pattern)`:

- `Bash(npm run test *)`: any command starting with `npm run test ` (the space matters!)
- `Bash(ls *)` matches `ls -la` and `ls`, but **not** `lsof`. `Bash(ls*)` (no space) matches `lsof` too.
- `Bash(git diff:*)` is an older way to write `Bash(git diff *)`; both work.
- `Read(./.env)` for files.

**Check order:** deny rules first, then ask rules, then allow rules. The **first** match decides. A deny can never be "carved out" by a more specific allow. No match → the mode's default (normally: ask you).

**Modes:** `default` (asks), `acceptEdits` (file edits OK), `plan` (read only), `auto` (a classifier decides), `dontAsk` (everything that would ask is denied), `bypassPermissions` (no prompts: only in a throwaway container or VM).

## 🪜 With numbers

Rules: deny `Bash(git push *)`, allow `Bash(git *)`.

- `git status` → no deny match, no ask match, allow `git *` matches → **allow**
- `git push origin main` → deny matches first → **deny** (even though allow also matches)
- `npm install` → nothing matches → **ask**

## 🔀 What if it were different?

<div class="wrong"><b>"The most specific rule wins"</b>: allow <code>Bash(aws s3 ls)</code> would beat deny <code>Bash(aws *)</code>. It doesn't: deny is checked first, always.</div>
<div class="wrong"><b>Bash(rm*) meant as "the rm command"</b>: also matches <code>rmdir</code> and <code>rmmod</code>. Write <code>Bash(rm *)</code>.</div>
<div class="wrong"><b>Unknown commands silently allowed</b>: the safe default is ask.</div>
<div class="right">deny → ask → allow → default "ask" ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"(" not in rule` | "bracket not in rule" | true when the text has no `(` anywhere |
| `rule.index("(")` | "index of the bracket" | the **position** of the first `(`. Positions count from 0. |
| `rule[:i]` | "rule up to i" | the characters before position `i` |
| `rule[i + 1:-1]` | "rule from i plus 1 to minus 1" | from just after the `(` up to, but not including, the **last** character (the `)`). `-1` counts from the end. |
| `s.endswith(" *")` | "s ends with space star" | true for `"git *"` |
| `pattern[:-2]` | "pattern without the last two" | `"git *"` → `"git"` |
| `s.startswith(prefix + " ")` | | true for `"git status"` when prefix is `"git"` |
| `a or b` | "a or b" | true when at least one of them is true |
| `rules.get("deny", [])` | "rules get deny, or an empty list" | the value under `"deny"`, or `[]` if there is none. An empty list makes the loop run 0 times. |

### 👀 Worked example: taking `"Bash(git *)"` apart

```python
rule = "Bash(git *)"
i = rule.index("(")
print(i, rule[:i], rule[i + 1:-1])
```

| position | 0–3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| character | `Bash` | `(` | `g` | `i` | `t` | ` ` | `*` | `)` |

1. `i` = **4**, where the `(` is.
2. `rule[:4]` = `"Bash"`: the tool name.
3. `rule[5:-1]` = positions 5 to 9 = `"git *"`: the pattern.
4. It ends with `" *"`, so `prefix` = `"git"`. Then `"git status"` matches (it starts with `"git "`), `"git"` matches (equal), but `"gitk"` does not (no space after `git`).

And `decide` with `rules = {"deny": ["Bash(git push *)"], "allow": ["Bash(git *)"]}` and the command `"git push origin main"`:

1. `outcome` = `"deny"`: the one rule matches → return `"deny"`. Done; allow is never looked at.
2. For `"git status"`: deny doesn't match, `rules.get("ask", [])` is `[]` (nothing to check), allow matches → `"allow"`.

## 🎯 Your quest

1. `matches(rule, tool, command)`: `rule` like `"Bash(git *)"` or `"Read"` (bare tool name = every call of that tool). Inside the brackets: a trailing `" *"` or `":*"` means "this prefix, then either nothing or a space and anything"; a trailing `"*"` without a space means plain prefix; otherwise exact match.
2. `decide(tool, command, rules)`: `rules` is a dict with lists under `"deny"`, `"ask"`, `"allow"` (any may be missing). Return `"deny"`, `"ask"` or `"allow"`; no match → `"ask"`.
3. `effective(key, layers)`: `layers` is a dict with any of `"managed"`, `"cli"`, `"local"`, `"project"`, `"user"`, each a dict of settings. Return the value from the highest layer that has `key` (or `None`).

**Part 1:** `matches`. Replace `return False` with:

1. `if "(" not in rule:`
2. `    return rule == tool`
3. `i = rule.index("(")`
4. `name = rule[:i]`
5. `pattern = rule[i + 1:-1]`
6. `if name != tool:`
7. `    return False`
8. `if pattern.endswith(" *") or pattern.endswith(":*"):`
9. `    prefix = pattern[:-2]`
10. `    return command == prefix or command.startswith(prefix + " ")`
11. `if pattern.endswith("*"):`
12. `    return command.startswith(pattern[:-1])`
13. `return command == pattern`

**Part 2:** `decide`. Replace `return "allow"` with:

1. `for outcome in ["deny", "ask", "allow"]:`
2. `    for rule in rules.get(outcome, []):`
3. `        if matches(rule, tool, command):`
4. `            return outcome`
5. `return "ask"`

**Part 3:** `effective`. Replace `return None` with:

1. `for name in ["managed", "cli", "local", "project", "user"]:`
2. `    settings = layers.get(name, {})`
3. `    if key in settings:`
4. `        return settings[key]`
5. `return None`

The list in line 1 is the order from highest to lowest, so the first layer that has the key wins.

**Remember:** values: highest layer wins. Permissions: deny, then ask, then allow.

## Review

<details><summary>Which file is your personal, uncommitted project memory?</summary>CLAUDE.local.md.</details>
