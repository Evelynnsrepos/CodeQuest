---
title: Skills: instructions that load when needed
minutes: 40
xp: 45
hint: parse_skill: lines = text.split("\n") and end = lines.index("---", 1) finds the closing ---
hint: parse_skill: for line in lines[1:end]: if ":" in line: pieces = line.split(":", 1) and out[pieces[0].strip()] = pieces[1].strip()
hint: parse_skill: out["body"] = "\n".join(lines[end + 1:])
hint: pick_skill: a best-so-far loop. Count n with for w in words(skills[name]): if w in task_words: n = n + 1, then if n > best_n: keep it
---
# The description decides

⏱️ About 40 minutes

> **Warm-up:** you have 30 how-to guides for your projects. Pasting all of them into every prompt would waste the context. How could the agent load just the right one?

**In one sentence:** a skill is a folder with a `SKILL.md`; only its short **description** sits in context all the time, and the full instructions load when the task matches.

## 🪜 Plain words

- Locations: `~/.claude/skills/<name>/SKILL.md` (yours, every project) or `.claude/skills/<name>/SKILL.md` (this project). Plugins can ship skills too.
- The file starts with **frontmatter** between `---` lines: `name` (defaults to the folder name) and `description` (recommended). Then the instructions in Markdown, plus optional scripts next to it.
- Claude sees every skill's **description** and loads the body when a task fits. You can also run one yourself as `/name`.
- Old `.claude/commands/<name>.md` slash commands now work the same way as skills.
- Descriptions are cut off at about 1,536 characters in the listing: **put the key use case first.**

**Subagents** are related: a second agent with its own context and system prompt (in `.claude/agents/`) that the main agent hands a task to. **Plugins** bundle skills, hooks, agents and MCP servers into one install.

## 🪜 With numbers

```markdown
---
name: new-lesson
description: Add a CodeQuest lesson. Use when asked to create or change a lesson folder (lesson.md, starter.py, solution.py, check.py).
---
1. Copy the folder layout from an existing lesson...
```

Task "add a lesson about entropy" shares the words *add* and *lesson* with that description → this skill is the one to load.

## 🔀 What if it were different?

<div class="wrong"><b>description: "Helpful stuff"</b>: matches nothing in particular, so it's never picked (or picked for everything).</div>
<div class="wrong"><b>Frontmatter not on the first line</b> (a blank line above the <code>---</code>): Claude Code doesn't read it at all.</div>
<div class="wrong"><b>Putting a 400-line procedure in CLAUDE.md</b>: it costs context in every session. A skill loads only when needed.</div>
<div class="right">a specific description that says WHEN, key use case first ✓</div>

## 🐍 Python you need

`words(s)` is **given** in the starter: it gives back the set of lower-case words in `s`, so `words("Add a Lesson!")` is `{"add", "a", "lesson"}`.

| You write | Say it | What it does |
|---|---|---|
| `text.split("\n")` | "split at new lines" | a list with one item per line |
| `lines.index("---", 1)` | "index of dashes, starting at 1" | the position of the first `"---"` line, looking from position 1 on (so it skips the opening one at 0) |
| `lines[1:end]` | "lines from 1 up to end" | the lines between the two `---` |
| `line.split(":", 1)` | "split at the first colon" | the `1` means "only cut once": `"description: a: b"` → `["description", " a: b"]` |
| `out[key] = value` | "out at key becomes value" | stores a value in the dictionary |
| `"\n".join(lines)` | "new-line join lines" | glues the lines back into one text |
| `for name in skills:` | | goes through the dictionary's keys; `skills[name]` is the description |
| `if n > best_n:` | | the **best-so-far** pattern: keep a new one only if it beats the old best. `>` (not `>=`) keeps the first on a tie. |

### 👀 Worked example 1: frontmatter

```python
text = "---\nname: tea\nnote: hot: yes\n---\nBoil water"
lines = text.split("\n")
end = lines.index("---", 1)
print(lines, end)
```

1. `lines` = `["---", "name: tea", "note: hot: yes", "---", "Boil water"]`.
2. `end` = **3**: the closing `---`.
3. `lines[1:3]` = `["name: tea", "note: hot: yes"]`.
4. `"note: hot: yes".split(":", 1)` = `["note", " hot: yes"]`. After `.strip()`: key `"note"`, value `"hot: yes"`. Only the first colon cut it.
5. `lines[4:]` = `["Boil water"]`, joined: `"Boil water"`, the body.

### 👀 Worked example 2: most shared words

```python
foods = {"soup": "hot tomato soup", "salad": "cold green salad"}
want = words("a hot soup please")
best = None
best_n = 0
for name in foods:
    n = 0
    for w in words(foods[name]):
        if w in want:
            n = n + 1
    if n > best_n:
        best = name
        best_n = n
print(best)
```

1. `want` = `{"a", "hot", "soup", "please"}`.
2. `"soup"`: its words `hot`, `tomato`, `soup`: `hot` and `soup` are wanted → `n` = 2. 2 > 0 → `best` = `"soup"`, `best_n` = 2.
3. `"salad"`: `cold`, `green`, `salad`: none wanted → `n` = 0. 0 > 2? No.
4. Prints `soup`. If nothing shared a word, `best` would still be `None`.

## 🎯 Your quest

1. `parse_skill(text)`: return a dict of frontmatter fields (`key: value` lines between the first two `---` lines) plus `"body"` (everything after). If the text doesn't start with `---`, return `{"body": text}`.
2. `pick_skill(skills, task)`: `skills` maps names to descriptions. Return the name whose description shares the most words with the task (lower-case, split on non-letters); `None` if no word is shared. Ties: the first in the dict.

**Part 1:** `parse_skill`. Replace `return {}` with:

1. `if not text.startswith("---"):`
2. `    return {"body": text}`
3. `lines = text.split("\n")`
4. `end = lines.index("---", 1)`
5. `out = {}`
6. `for line in lines[1:end]:`
7. `    if ":" in line:`
8. `        pieces = line.split(":", 1)`
9. `        out[pieces[0].strip()] = pieces[1].strip()`
10. `out["body"] = "\n".join(lines[end + 1:])`
11. `return out`

**Part 2:** `pick_skill`. Replace `return None` with:

1. `best = None`
2. `best_n = 0`
3. `task_words = words(task)`
4. `for name in skills:`
5. `    n = 0`
6. `    for w in words(skills[name]):`
7. `        if w in task_words:`
8. `            n = n + 1`
9. `    if n > best_n:`
10. `        best = name`
11. `        best_n = n`
12. `return best`

**Remember:** skills = know-how on demand; the description is the trigger.

## Review

<details><summary>Which exit code blocks a PreToolUse hook?</summary>2.</details>
