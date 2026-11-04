---
title: Saving the game
xp: 25
---
# Don't lose my base!

A survival game without saving is cruel. Saving means turning the game's state into **text** you can write to a file, and loading means turning that text back.

**JSON** is a common text format that looks just like a GDScript Dictionary:

```gdscript
var data := {"health": 80, "items": {"wood": 12}}
var text := JSON.stringify(data)      # '{"health":80,"items":{"wood":12}}'
var back = JSON.parse_string(text)    # a Dictionary again
```

Two catches:

- JSON only knows numbers, text, true/false, lists and dictionaries. A `Vector2` isn't one of them, so save it as two numbers: `{"x": pos.x, "y": pos.y}`, and rebuild it with `Vector2(d.x, d.y)` when loading.
- JSON doesn't separate whole numbers from decimals: every number comes back as a **float**. `80` comes back as `80.0`, so wrap whole numbers in `int()` when loading.

To actually write the file in a real game:

```gdscript
var file := FileAccess.open("user://save.json", FileAccess.WRITE)
file.store_string(text)
# and to read it back:
var text := FileAccess.get_file_as_string("user://save.json")
```

`user://` is a folder Godot gives every game for saves and settings (on Windows it's in `%APPDATA%\Godot\app_userdata\YourGame`). In CodeQuest we skip the file and work with the text directly.

## Your quest

1. `save_text() -> String` returns JSON with `health`, `day`, `items` and `position` (as `{"x": ..., "y": ...}`).
2. `load_text(text: String)` reads it back and sets all four. `health` and `day` must be `int` again, and `position` a `Vector2`.
