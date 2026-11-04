---
title: Triggers: watch a folder
xp: 25
---
# Start when something new shows up

⏱️ About 10 minutes · one function

> **Warm-up:** you drop scanned receipts into a folder. How does your script know which ones are new since last time?

**In one sentence:** a folder trigger compares a **snapshot** from last time with a snapshot from now and handles only what's new or changed.

## 🪜 Plain words

Every file has a **modification time** ("mtime"): a number for when it last changed. A snapshot is a dictionary `{filename: mtime}`.

- In `now` but not in `before` → **new**.
- In both, but the mtime is different → **changed**.
- In `before` but not in `now` → deleted (we ignore those here).

Clocks only give a schedule (LLMs 9, lesson 10, covers cron). A trigger like this reacts to **events** instead, and costs nothing when nothing happened.

## 🎯 Your quest

Write `changed_files(before, now)` that returns a **sorted** list of names that are new or changed.

- `changed_files({"a.jpg": 1}, {"a.jpg": 1, "b.jpg": 5})` → `["b.jpg"]`
- `changed_files({"a.jpg": 1}, {"a.jpg": 2})` → `["a.jpg"]`

<details><summary>💡 Hint</summary><code>sorted(name for name, t in now.items() if before.get(name) != t)</code>. <code>before.get(name)</code> is <code>None</code> for new files, and <code>None != t</code> is true.</details>

## 🖥️ On your computer

Take a snapshot: `{p.name: p.stat().st_mtime for p in pathlib.Path("inbox").iterdir()}`. Save it with `json.dump` at the end of each run and load it at the start of the next. Run the script every few minutes with a systemd timer (NixOS: `systemd.timers` in your config) or Windows Task Scheduler.

**Remember:** snapshot, compare, handle only the difference.

## Review

<details><summary>Lesson 6: in a router, who decides, and who acts?</summary>The model decides the label; your code calls the handler.</details>
