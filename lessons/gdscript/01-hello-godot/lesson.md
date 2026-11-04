---
title: Hello, Godot!
xp: 10
hint: Put print("Hello, Godot!") inside run(), indented with one Tab.
hint: Check the spelling, the comma and the ! exactly.
---
# Your first script

> **Warm-up:** In a game, where do you think the text from print() shows up?

GDScript is the language of the Godot game engine. It looks a lot like Python: blocks are indented, and `print()` writes text to the output.

In these lessons your code goes inside a function called `run()`. CodeQuest calls it for you, just like Godot calls `_ready()` when a scene starts.

```gdscript
func run():
	print("The game begins")
```

Godot indents with **tabs**. On a phone, use the **Tab** key in the bar above the keyboard.

## Your quest

Make `run()` print exactly:

```
Hello, Godot!
```

## Review

<details><summary>What does print() do in Godot?</summary>It writes text to the Output panel (here, the output box).</details>
<details><summary>What does Godot use to indent code inside a function?</summary>Tabs.</details>
