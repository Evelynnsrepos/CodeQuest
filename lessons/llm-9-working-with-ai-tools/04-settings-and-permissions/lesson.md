---
title: Settings layers and permission rules
xp: 60
---
# Who wins when two files disagree?

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

## 🎯 Your quest

1. `matches(rule, tool, command)`: `rule` like `"Bash(git *)"` or `"Read"` (bare tool name = every call of that tool). Inside the brackets: a trailing `" *"` or `":*"` means "this prefix, then either nothing or a space and anything"; a trailing `"*"` without a space means plain prefix; otherwise exact match.
2. `decide(tool, command, rules)`: `rules` is a dict with lists under `"deny"`, `"ask"`, `"allow"` (any may be missing). Return `"deny"`, `"ask"` or `"allow"`; no match → `"ask"`.
3. `effective(key, layers)`: `layers` is a dict with any of `"managed"`, `"cli"`, `"local"`, `"project"`, `"user"`, each a dict of settings. Return the value from the highest layer that has `key` (or `None`).

**Remember:** values: highest layer wins. Permissions: deny, then ask, then allow.

## Review

<details><summary>Which file is your personal, uncommitted project memory?</summary>CLAUDE.local.md.</details>
