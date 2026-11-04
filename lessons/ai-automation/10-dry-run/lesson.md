---
title: Dry runs and logs
xp: 25
---
# Show what you would do, then do it

⏱️ About 10 minutes · one function

> **Warm-up:** you wrote a script that renames 300 photos. How do you check it's right **before** it renames anything?

**In one sentence:** a **dry run** goes through every step but only **prints** the actions, and a **log** says what happened so you can check later.

## 🪜 Plain words

- Default to `dry_run=True`. You have to say "yes, really" (`dry_run=False`) to change anything. A forgotten flag then does nothing instead of something bad.
- Write one log line per action, the same in both modes, with a prefix: `DRY rename(old='a.jpg', new='b.jpg')` or `RAN rename(...)`.
- Format the arguments as `key=value` with `repr(value)`, so text shows its quotes and you can tell `'5'` from `5`.

## 🎯 Your quest

Write `execute(actions, tools, dry_run=True)`:

- `actions` is a list of `{"tool": name, "args": {...}}`, `tools` maps names to functions.
- For each action build the line `f"{prefix} {name}({args_text})"`, where `prefix` is `"DRY"` or `"RAN"` and `args_text` is the `key=repr(value)` pairs joined with `", "`.
- Only when `dry_run` is `False`, call `tools[name](**args)`.
- Return the list of log lines.

<details><summary>💡 Hint</summary><code>args_text = ", ".join(f"{k}={v!r}" for k, v in a["args"].items())</code>. The <code>!r</code> means "use repr".</details>

## 🖥️ On your computer

Write the lines to a file too: `logging.basicConfig(filename="automation.log", level=logging.INFO)` then `logging.info(line)`. When something odd happens next week, the log tells you which run did it.

**Remember:** dry run by default, one log line per action.

## Review

<details><summary>Lesson 9: is "send an email" safe to run without asking?</summary>No, you can't unsend it. It goes in the ask-first queue.</details>
