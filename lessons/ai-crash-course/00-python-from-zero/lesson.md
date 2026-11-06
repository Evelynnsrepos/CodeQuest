---
title: Python from zero: how to read and write code
minutes: 20
xp: 20
hint: Start the line with def, then the name double, then (x) and a colon: def double(x):
hint: The line under def starts with 4 spaces. It gives the answer back with return: return x * 2
hint: For greet, glue two pieces of text together with +: return "Hello, " + name
---
# You don't need to know any code

⏱️ About 20 minutes · two tiny functions

> **Warm-up:** a recipe says "take 2 eggs, beat them, add sugar". A program is the same thing: a list of steps, written very exactly, that a computer follows from top to bottom.

**In one sentence:** in this course you'll write small pieces of Python, and every lesson first shows you every piece you need, with examples, before you write anything yourself.

## 🖥️ How a lesson works

- On the right (or below, on a phone) is the **editor**: a box with code in it. You type there.
- **Run** runs your code and shows what it prints. Nothing bad can happen. Press it as often as you like.
- **Submit** runs your code *and* checks it. It says which parts are done ("2 of 3 parts done").
- **Hint** shows one small hint at a time. After a few hints you can see the whole answer. Using hints is fine: that's how you learn the pattern.
- Lines starting with `#` in the editor are **comments**: notes for you. Python ignores them. In this course they tell you what to write on each line.

## 🐍 The first pieces of Python

Read this table one row at a time. You don't need to remember it: every lesson repeats the pieces it uses.

| You write | Say it | What it does |
|---|---|---|
| `print("hi")` | "print hi" | shows `hi` in the output box |
| `"hi"` | "the text hi" | text goes between quotes. Text is called a **string**. |
| `7`, `2.5` | "seven", "two point five" | numbers. No quotes. A dot, not a comma, for decimals. |
| `+  -  *  /` | "plus, minus, times, divided by" | maths. `*` is times, `/` is divided by. |
| `age = 30` | "age becomes 30" | stores 30 under the name `age`. This is a **variable**: a labelled box. `=` does *not* mean "is equal", it means "put this into the box". |
| `# note` | "comment" | a note for humans. Python skips it. |

### Example 1: variables and print

```python
apples = 3
pears = 4
total = apples + pears
print(total)
```

Line by line:

1. `apples = 3`: put 3 into a box called `apples`.
2. `pears = 4`: put 4 into a box called `pears`.
3. `total = apples + pears`: look inside both boxes (3 and 4), add them (7), put 7 into a new box `total`.
4. `print(total)`: show what's in `total`. The output box shows `7`.

### Example 2: gluing text

`+` between two strings glues them together:

```python
name = "Evelynn"
print("Hi " + name)
```

Output: `Hi Evelynn`. Notice the space inside `"Hi "`: Python only adds exactly what you write.

## 🧰 Functions: your own little machines

A **function** is a machine with a name. You put something in, it gives something back. Almost every quest in this course asks you to finish a function.

```python
def triple(x):
    return x * 3
```

Piece by piece:

| Piece | Say it | What it means |
|---|---|---|
| `def` | "define" | "I'm making a new function" |
| `triple` | the name | you choose it. The quest tells you which name to use. |
| `(x)` | "taking x" | `x` is the **input** (called a *parameter*): a box that gets filled when someone uses the function |
| `:` | colon | "the steps of this function start below" |
| 4 spaces | indentation | every line that belongs to the function starts with 4 spaces. That's how Python knows where the function ends. **The spaces matter.** |
| `return x * 3` | "give back x times 3" | the answer the machine hands back. The function stops here. |

Using (**calling**) the function: write its name and put the input in brackets.

```python
print(triple(5))    # the machine gets 5, gives back 15, print shows 15
print(triple(10))   # shows 30
```

What happens in `triple(5)`: Python fills the box `x` with 5, runs `return x * 3`, so it computes 5 × 3 = 15 and hands back 15. Then `print` shows it.

A function can take **more than one input**, separated by commas:

```python
def add(a, b):
    return a + b

print(add(2, 3))    # a is 2, b is 3, shows 5
```

<div class="wrong"><b>Forgetting the 4 spaces:</b> <code>def triple(x):</code> followed by <code>return x * 3</code> at the start of the line gives <code>IndentationError</code>. Python doesn't know the line belongs to the function.</div>
<div class="wrong"><b>print instead of return:</b> <code>print(x * 3)</code> inside the function shows the number, but hands nothing back. The checker asks the function for its answer and gets nothing (Python calls "nothing" <code>None</code>).</div>
<div class="right"><b>Right:</b> 4 spaces, then <code>return</code> ✓</div>

<div class="quiz" data-answer="1" data-why="x gets 4, and 4 + 1 = 5 is handed back. print then shows 5."><p><b>Predict first:</b> <code>def plus_one(x):</code> / <code>    return x + 1</code>. What does <code>print(plus_one(4))</code> show?</p><button>4</button><button>5</button><button>x + 1</button></div>

## 🎯 Your quest

The editor already has both function lines started. Replace the line `return 0` / `return ""` with the right one.

1. `double(x)`: give back `x` times 2. (Look at `triple` above: it's the same with a 2.)
2. `greet(name)`: give back the text `Hello, ` glued to the name. `greet("Ada")` must give back `"Hello, Ada"`. (Look at Example 2.)

Press **Run** first: the last lines print what your functions give back. Then **Submit**.

**Remember:** `def` makes a function, 4 spaces put lines inside it, `return` hands the answer back.
