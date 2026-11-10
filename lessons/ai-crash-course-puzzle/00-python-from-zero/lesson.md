---
title: How the puzzle works (and your first Python)
minutes: 15
xp: 15
hint: The gap under def double needs the block that multiplies: return x * 2
hint: The gap under def greet needs the block with "Hello, " (comma and space inside the quotes) + name
distractor: return x + 2
distractor: return "Hello, " + "name"
---
# Code like Lego

⏱️ About 15 minutes · 🧩 2 gaps to fill

> **Warm-up:** have you ever built something from Lego with the instructions open next to you? That's exactly how this course works.

**In one sentence:** you never type code here; you read how it works, then snap ready-made **blocks** of code into the right **gaps**.

## 🧩 How a puzzle works

Open the **Puzzle** tab (on a phone) or look to the right (on a computer). You'll see:

1. **The program.** Most lines are already written for you.
2. **Gaps** with a **?** in them. One gap is glowing: that's where the next block goes.
3. **The tray** under the program, full of blocks.

What you do:

- **Tap a block** → it jumps into the glowing gap. (On a computer you can also drag it.)
- **Tap a filled gap** → the block jumps back to the tray. Changed your mind? No problem.
- **Tap an empty gap** → it starts glowing, so the next block goes there.
- **▶ Run** shows what your program prints. **Submit** checks it and gives you XP.

⚠️ The tray has **decoy blocks**: they look almost right but are wrong. Not every block gets used! Reading carefully is the whole skill.

The spaces at the start of a line (the **indentation**) are done for you. You only pick the right block.

## 🐍 The Python in this puzzle

A **function** is a little machine: you put something in, it gives something back.

```python
def triple(x):
    return x * 3
```

Read it piece by piece:

| Piece | Say it | What it does |
|---|---|---|
| `def` | "define" | "I'm making a new function" |
| `triple` | the name | what the machine is called |
| `(x)` | "taking x" | the box for what goes **in** |
| `:` | colon | "the inside of the function starts on the next line" |
| `return` | "give back" | what comes **out** |
| `x * 3` | "x times 3" | in Python, `*` means **times** (multiply) |

So `triple(5)` puts 5 into the box `x`, works out 5 × 3, and gives back `15`.

Text works too. Text goes in quotes, and `+` glues two texts together:

```python
def shout(word):
    return word + "!"
```

`shout("Hi")` gives back `"Hi!"`. Careful: `"word"` **with** quotes would be the letters w-o-r-d, not the box called `word`.

<div class="quiz" data-answer="1" data-why="+ adds 2 to the number. * multiplies it by 2. For 21 that's 23 versus 42."><p><b>Predict first:</b> which block doubles a number?</p><button>return x + 2</button><button>return x * 2</button></div>

## 🧩 Your puzzle

1. Under `def double(x):` the gap needs the block that gives back **x times 2**.
2. Under `def greet(name):` the gap needs the block that gives back `"Hello, "` glued to the **box** `name` (no quotes around name!).

Then press **▶ Run**. You should see `42` and `Hello, Ada`. Then **Submit**.

**Remember:** read every block, decoys look almost right.
