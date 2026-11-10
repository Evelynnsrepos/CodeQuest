---
title: How Claude Code remembers: CLAUDE.md and auto memory
minutes: 50
xp: 50
hint: load_order, folders: folders = [""] and folder = "". Then for part in cwd.split("/"): if part != "": folder = folder + "/" + part and folders.append(folder)
hint: load_order, files: for folder in folders: for name in [...]: path = folder + "/" + name, and if path in existing and path not in out: out.append(path)
hint: imports: pieces = text.split("`"). The pieces at 0, 2, 4, ... are outside backticks: for i in range(0, len(pieces), 2):
hint: imports: for word in pieces[i].split(): if word.startswith("@"): out.append(word[1:])
hint: index_loaded: size = size + len(line) + 1, then if size > 25000: break, then out.append(line)
---
# Memory is just files loaded at the start

⏱️ About 50 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"/home/eve".split("/")` | "split at the slashes" | `["", "home", "eve"]`. The first piece is empty, because the text starts with `/`. |
| `if part != "":` | "if part is not empty" | `!=` means "is not equal to" |
| `folder = folder + "/" + part` | | glues texts together: `""` → `"/home"` → `"/home/eve"` |
| `if a in s and b not in out:` | | both must be true. `not in` is true when the list does **not** hold it. |
| `text.split()` | "split" (nothing in the brackets) | cuts at every space or new line: `"a b\nc".split()` is `["a", "b", "c"]` |
| `range(0, 7, 2)` | "range from 0 to 7, step 2" | `0, 2, 4, 6`: every second number, stopping before 7 |
| `word.startswith("@")` | "word starts with at" | true for `"@notes.md"` |
| `word[1:]` | "word from 1 to the end" | drops the first character: `"@notes.md"` → `"notes.md"` |
| `lines[:200]` | "lines up to 200" | the first 200 items (all of them if there are fewer) |
| `break` | "break" | leaves the loop right away |

### 👀 Worked example 1: every folder on the way down

```python
folders = [""]
folder = ""
for part in "/home/eve/CodeQuest".split("/"):
    if part != "":
        folder = folder + "/" + part
        folders.append(folder)
print(folders)
```

1. The pieces are `""`, `"home"`, `"eve"`, `"CodeQuest"`.
2. `""` is empty: skipped.
3. `"home"`: `folder` = `"/home"`. `"eve"`: `"/home/eve"`. `"CodeQuest"`: `"/home/eve/CodeQuest"`.
4. `folders` = `["", "/home", "/home/eve", "/home/eve/CodeQuest"]`. The `""` stands for `/` itself: `"" + "/" + "CLAUDE.md"` is `"/CLAUDE.md"`.

### 👀 Worked example 2: skipping text inside backticks

```python
text = "Read @a.md not `@b.md` and @c.md"
pieces = text.split("`")
print(pieces)
```

`pieces` = `` ["Read @a.md not ", "@b.md", " and @c.md"] ``. Cutting at each backtick puts everything **inside** backticks at positions 1, 3, 5, ... So `range(0, len(pieces), 2)` visits only 0 and 2, the outside parts. In those, the words starting with `@` are `@a.md` and `@c.md`, so the answer is `["a.md", "c.md"]`.

Splitting into words also handles emails: `"a@b.com"` is one word that starts with `a`, not `@`, so it's not an import.

## 🎯 Your quest

1. `load_order(cwd, existing, home)`: `cwd` like `"/home/eve/CodeQuest/lessons"`, `existing` a set of file paths that exist, `home` like `"/home/eve"`. Return the paths that load at launch, in order: `home + "/.claude/CLAUDE.md"` first (if it exists), then for each folder from `/` down to `cwd`: `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` (each only if it exists). (Skip the managed file and don't list the user file twice.)
2. `imports(text)`: list of `@paths` in a CLAUDE.md, ignoring any inside backticks. A path is `@` followed by non-space characters, at the start of the text or after whitespace.
3. `index_loaded(lines)`: the lines of a `MEMORY.md` that load: at most 200 lines and at most 25,000 characters in total (count each line plus 1 for its newline; stop before the line that would go over).

**Part 1:** `load_order`. Replace `return []` with:

1. `out = []`
2. `user = home + "/.claude/CLAUDE.md"`
3. `if user in existing:`
4. `    out.append(user)`
5. `folders = [""]`
6. `folder = ""`
7. `for part in cwd.split("/"):`
8. `    if part != "":`
9. `        folder = folder + "/" + part`
10. `        folders.append(folder)`
11. `for folder in folders:`
12. `    for name in ["CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"]:`
13. `        path = folder + "/" + name`
14. `        if path in existing and path not in out:`
15. `            out.append(path)`
16. `return out`

Line 14's `path not in out` is what stops the user file from showing up twice when `cwd` is your home folder.

**Part 2:** `imports`. Replace `return []` with:

1. `out = []`
2. `` pieces = text.split("`") ``
3. `for i in range(0, len(pieces), 2):`
4. `    for word in pieces[i].split():`
5. `        if word.startswith("@"):`
6. `            out.append(word[1:])`
7. `return out`

**Part 3:** `index_loaded`. Replace `return lines` with:

1. `out = []`
2. `size = 0`
3. `for line in lines[:200]:`
4. `    size = size + len(line) + 1`
5. `    if size > 25000:`
6. `        break`
7. `    out.append(line)`
8. `return out`

**Remember:** memory = files loaded at the start; rules in CLAUDE.md, guarantees in hooks and permissions.

## Review

<details><summary>What does the model actually receive on each request?</summary>System prompt, tools, memory files and the whole history, re-sent every time.</details>
