---
title: Skills: instructions that load when needed
xp: 45
---
# The description decides

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

## 🎯 Your quest

1. `parse_skill(text)`: return a dict of frontmatter fields (`key: value` lines between the first two `---` lines) plus `"body"` (everything after). If the text doesn't start with `---`, return `{"body": text}`.
2. `pick_skill(skills, task)`: `skills` maps names to descriptions. Return the name whose description shares the most words with the task (lower-case, split on non-letters); `None` if no word is shared. Ties: the first in the dict.

**Remember:** skills = know-how on demand; the description is the trigger.

## Review

<details><summary>Which exit code blocks a PreToolUse hook?</summary>2.</details>
