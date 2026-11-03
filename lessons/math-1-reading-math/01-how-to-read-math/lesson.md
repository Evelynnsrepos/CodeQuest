---
title: How to read math without panicking
xp: 20
---
# Math is just very short code

> **Warm-up:** look at `A = πr²`. Before reading on, try saying it out loud in normal words. Which part feels unclear?

**In one sentence:** a formula is a tiny program written in a very compressed language, and you can read it piece by piece like code.

## How these math courses work

These courses are built to be easy to follow if focus is hard (ADHD-friendly):

- **One idea per lesson.** If a lesson feels long, stop after any section and come back later; nothing breaks.
- Every lesson has the same parts in the same order, so you always know where you are:
  - 🔣 **New symbols**: a table with each symbol, how to *say* it, what it means, and the Python for it.
  - 🗣️ **Say it out loud**: every formula translated into a normal sentence.
  - 🧮 **Worked example**: real numbers, every step written down.
  - 🤖 **Where AI uses it**: why you're learning this.
  - 🎯 **Your quest**: one small piece of code.
- **Remember** lines are the one thing to keep if you forget everything else.
- Re-reading is normal. Mathematicians read formulas slowly, many times.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `x`, `r`, `n` | "x", "r", "n" | a **variable**: a name for a number, like a Python variable | `x = 3` |
| `π` | "pie" | a **constant**: a fixed number, 3.14159… | `math.pi` |
| `=` | "equals" / "is" | both sides have the same value (a fact, not an assignment) | `==` to compare, `=` to define |
| `3x` | "three x" | **multiplication with no sign**: 3 times x | `3 * x` |
| `r²` | "r squared" | r times r | `r ** 2` |

## The idea

Math writing leaves things out to stay short:

- **No multiplication sign.** `2πr` means `2 * math.pi * r`. Two letters side by side (`ab`) means `a * b`, never a two-letter variable.
- **One letter per variable.** Math uses `r` where code would write `radius`. That's why it feels cryptic; the meaning is in the surrounding text.
- **`=` states a fact.** `A = πr²` means "A is always π times r squared", so in Python it becomes a function: give it `r`, get `A`.

## 🗣️ Say it out loud

`A = πr²` → "The area A equals pi times r squared." → "To get the area, square the radius and multiply by pi."

## 🧮 Worked example

`f(x) = 3x + 2` with `x = 4`:

1. Replace `x` with 4: `3·4 + 2`
2. Multiply first: `12 + 2`
3. Add: `14`

## 🤖 Where AI uses it

Every model is a formula. A single neuron (LLMs 1) is `y = w·x + b`: "y equals w times x plus b".

## 🎯 Your quest

Turn each formula into a Python function:

1. `f(x) = 3x + 2`
2. `average(a, b) = (a + b) / 2`
3. `area(r) = πr²` (use `math.pi`)

**Remember:** letters next to each other are multiplied, and `=` in a formula means "is always".

## Review

<details><summary>How do you write 5ab in Python?</summary>5 * a * b</details>
<details><summary>What does the = in a formula mean?</summary>Both sides always have the same value. In code it usually becomes a function.</details>
