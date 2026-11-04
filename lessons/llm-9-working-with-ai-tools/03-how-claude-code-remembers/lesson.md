---
title: How Claude Code remembers: CLAUDE.md and auto memory
xp: 50
---
# Memory is just files loaded at the start

> **Warm-up:** you start Claude Code in `~/My-repos/CodeQuest/lessons`. Which instruction files does it read before you type anything?

**In one sentence:** Claude Code has no memory of its own; it loads CLAUDE.md files (that **you** write) and an auto-memory index (that **Claude** writes) into the context at the start of every session.

## 🪜 Plain words

**CLAUDE.md files** (you write them; checked against the Claude Code docs, Nov 2026):

| Scope | File | Who it's for |
|---|---|---|
| Managed (organization) | `/etc/claude-code/CLAUDE.md` on Linux, `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows | everyone on the machine |
| User | `~/.claude/CLAUDE.md` | you, in every project |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | everyone using the repo (commit it) |
| Local | `./CLAUDE.local.md` | only you, this project (add to `.gitignore`) |

- Files in the folder you start in **and every folder above it** load at launch, ordered from the top of the disk down to your folder. Within one folder, `CLAUDE.local.md` comes after `CLAUDE.md`. So the most specific instructions are read **last**.
- They are **added together**, not overriding each other. Contradictions confuse Claude, so keep them consistent.
- CLAUDE.md files in **subfolders** load later, only when Claude works with files in that subfolder.
- `@path/to/file` inside a CLAUDE.md **imports** that file (up to 4 hops deep). Inside backticks it's just text.
- If a repo has only an `AGENTS.md` (the file other agents use), Claude Code reads that instead.
- Aim for under 200 lines per file; longer files cost context and get followed less reliably.

**Auto memory** (Claude writes it): `~/.claude/projects/<project>/memory/` with a `MEMORY.md` **index** (one line per memory) plus topic files. Only the first **200 lines or 25 KB** of `MEMORY.md` load at session start. `/memory` opens and toggles all of this; `/context` shows what actually loaded.

Sessions themselves are saved as JSON lines under `~/.claude/projects/`, and `claude --continue` / `--resume` reloads one.

## 🪜 With numbers

Started in `/home/eve/CodeQuest/lessons` with files in `/home/eve/CodeQuest/CLAUDE.md`, `/home/eve/CodeQuest/CLAUDE.local.md` and `/home/eve/CodeQuest/lessons/CLAUDE.md`, plus `~/.claude/CLAUDE.md`. Load order:

1. `~/.claude/CLAUDE.md` (user)
2. `/home/eve/CodeQuest/CLAUDE.md`
3. `/home/eve/CodeQuest/CLAUDE.local.md`
4. `/home/eve/CodeQuest/lessons/CLAUDE.md` (read last, wins in practice)

## 🔀 What if you got it wrong?

<div class="wrong"><b>Secrets in CLAUDE.md</b>: it's committed and sent to the model every request. Use environment variables.</div>
<div class="wrong"><b>"Never push to main" only in CLAUDE.md</b>: instructions are context, not enforcement. Use a deny rule or a hook for guarantees.</div>
<div class="wrong"><b>A 600-line MEMORY.md</b>: everything after line 200 is silently not loaded.</div>
<div class="right">short CLAUDE.md for rules, personal bits in CLAUDE.local.md, hooks/permissions for guarantees ✓</div>

## 🎯 Your quest

1. `load_order(cwd, existing, home)`: `cwd` like `"/home/eve/CodeQuest/lessons"`, `existing` a set of file paths that exist, `home` like `"/home/eve"`. Return the paths that load at launch, in order: `home + "/.claude/CLAUDE.md"` first (if it exists), then for each folder from `/` down to `cwd`: `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` (each only if it exists). (Skip the managed file and don't list the user file twice.)
2. `imports(text)`: list of `@paths` in a CLAUDE.md, ignoring any inside backticks. A path is `@` followed by non-space characters, at the start of the text or after whitespace.
3. `index_loaded(lines)`: the lines of a `MEMORY.md` that load: at most 200 lines and at most 25,000 characters in total (count each line plus 1 for its newline; stop before the line that would go over).

**Remember:** memory = files loaded at the start; rules in CLAUDE.md, guarantees in hooks and permissions.

## Review

<details><summary>What does the model actually receive on each request?</summary>System prompt, tools, memory files and the whole history, re-sent every time.</details>
