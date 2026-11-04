---
title: How to read math without panicking
xp: 20
---
# Math is just very short code

> **Warm-up:** you'll see things like `A = πr²` in this course. You don't need to understand it yet. Just notice: which parts look like letters, which like numbers, which like signs?

**In one sentence:** a formula is a recipe written in a very short secret code, and these courses teach you the code one sign at a time.

## How these math courses work

They're made for someone who has **never really used math**, and they're made to be easy to follow if focus is hard (ADHD-friendly):

- **One idea per lesson.** Stop after any section and come back later; nothing breaks.
- **No formula on the first try.** Every lesson goes in the same steps:
  1. 🪜 **Plain words**: the idea as a normal story, no symbols at all.
  2. 🪜 **With numbers**: the same idea with real numbers, still in words.
  3. 🔣 **The signs**: each new sign, one at a time: how to say it, what it means, how to type it in Python.
  4. 🔬 **Take the formula apart**: the full formula, then **every single sign explained again**, piece by piece, next to the numbers from the example. Every time. Even signs you've seen before.
  5. 🗣️ **Say it out loud**: the formula as a sentence.
  6. 🤖 **Where AI uses it**: why you're learning this.
  7. 🎯 **Your quest**: one small bit of code.
- **Remember** lines are the one thing to keep.
- Not getting a formula at first is **normal and expected**. You're supposed to get it by the end of the lesson, not at the start.

## 🪜 Plain words

A recipe says: "to get the price, take the number of apples and multiply by what one apple costs, then add the bag fee."

## 🪜 With numbers

3 apples, 2 euros each, 1 euro bag fee: 3 times 2 is 6, plus 1 is 7 euros.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| a letter like `x` | "x" | a **variable**: a box with a number in it, like a Python variable | `x = 3` |
| `=` | "equals" / "is" | both sides have the same value | `==` to compare |
| `3x` | "three x" | 3 times x. **Math hides the multiplication sign** when a number touches a letter | `3 * x` |
| `+` | "plus" | add | `+` |

## 🔬 Take the formula apart

The apple recipe as a formula:

<div class="formula"><span class="k1">p</span> = <span class="k2">2</span><span class="k3">a</span> <span class="k4">+ 1</span></div>

| Piece | Say it | Means | In our example |
|---|---|---|---|
| <span class="k1">p</span> | "p" | a box for the **price** (the answer) | 7 |
| `=` | "equals" | "is always the same as" | |
| <span class="k2">2</span> | "two" | the cost of one apple | 2 |
| <span class="k3">a</span> | "a" | a box for the number of **apples** | 3 |
| <span class="k2">2</span><span class="k3">a</span> | "two a" | 2 **times** a (the times sign is hidden!) | 2 · 3 = 6 |
| <span class="k4">+ 1</span> | "plus one" | add the bag fee | + 1 |

So `p = 2a + 1` → `7 = 2·3 + 1` ✓

## 🔀 What if the formula were different?

<div class="wrong"><b>p = 2 + a + 1</b> (forgot that "2a" means times): 3 apples would cost 2 + 3 + 1 = 6 euros. Too cheap, and 100 apples would cost only 103.</div>
<div class="wrong"><b>p = 2(a + 1)</b> (brackets in the wrong place): now the bag is charged like an apple: 2 · 4 = 8 euros.</div>
<div class="right"><b>p = 2a + 1</b>: 2 · 3 + 1 = 7 euros ✓</div>

The other formula from the warm-up, `A = πr²` (area of a circle):

| Piece | Say it | Means |
|---|---|---|
| `A` | "A" | a box for the area (the answer) |
| `=` | "equals" | is always the same as |
| `π` | "pie" | a fixed number, 3.14159…, written as a Greek letter |
| `r` | "r" | a box for the radius |
| `r²` | "r squared" | r times r (the little 2 means "times itself", lesson 7) |
| `πr²` | "pie r squared" | π times r times r (hidden times signs!) |

## 🗣️ Say it out loud

`p = 2a + 1` → "p equals two a plus one" → "the price is two times the apples, plus one."

## 🤖 Where AI uses it

Every AI model is a formula like this, just bigger. One "neuron" is `y = w·x + b`: "multiply the input by a weight, add a bias". Same shape as the apple recipe!

## 🎯 Your quest

A formula becomes a Python **function**: give it the boxes, get the answer.

1. `f(x) = 3x + 2` → write `f(x)` (remember the hidden times sign: `3 * x`)
2. `average(a, b) = (a + b) / 2`
3. `area(r) = πr²` (use `math.pi`, and `r ** 2` for r squared)

**Remember:** a number touching a letter means "times".

## Review

<details><summary>How do you write 5ab in Python?</summary>5 * a * b (two hidden times signs).</details>
<details><summary>What is a variable?</summary>A box (a name) that holds a number.</details>
