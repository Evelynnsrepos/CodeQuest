---
title: Your map of the AI courses
minutes: 15
xp: 30
hint: plan: total_minutes = lessons * minutes_per_lesson, then return math.ceil(total_minutes / minutes_per_day)
hint: PICK: write a course name between the quotes, for example PICK = "LLMs 1: How an LLM works"
---
# Where to go from here

⏱️ About 15 minutes · one function and one choice

> **Warm-up:** which of the last eleven lessons did you find most interesting? That's a good hint for where to go next.

**In one sentence:** you've seen every big idea once; the full courses go deep, level by level.

## 🗺️ The map

| Level | Courses | You'll be able to |
|---|---|---|
| **Start here** | this crash course | explain how AI works in plain words |
| **Level 1 · Understand and use AI** | LLMs 1, 2, 3 | build each piece of an LLM in Python, run models on your PC, give them tools and RAG |
| **Level 2 · Train your own** | LLMs 4, 5, 6, 7, AI beyond LLMs | train a model from scratch, fine-tune with QLoRA, evaluate and publish your own model; know the other kinds of AI |
| **Level 3 · Advanced and pro** | LLMs 8, LLMs 9, AI engineer 1, 2 and 3 | understand frontier models; use PyTorch, real RAG and evals; ship AI apps like an AI engineer |

**Side tracks** you can take any time: **Math for AI** (Math 1–6, from zero, recommended before Level 2), **Python** basics, **AI automation**, and **Data cleaning with Python**.

A good rhythm: one lesson a day, one course a month.

## 🔢 How many days? Step by step

14 lessons, 20 minutes each, and you have 30 minutes a day:

1. Total minutes: 14 × 20 = 280.
2. Days: 280 ÷ 30 = 9.33.
3. Round **up** (lesson 02): a third of a day is still a day you need. → **10 days**.

## 🐍 Python you need

All of these you've already used. Here they are again:

| You write | Say it | What it does |
|---|---|---|
| `a * b` | "a times b" | multiply |
| `a / b` | "a divided by b" | divide (gives a decimal) |
| `math.ceil(9.33)` | "ceiling of 9.33" | rounds **up**: `10` |
| `minutes_per_lesson=20` in the `def` line | "default 20" | if the caller doesn't say, each lesson is 20 minutes (lesson 08) |
| `PICK = "LLMs 1"` | "PICK becomes the text LLMs 1" | puts a string into a box. The quotes are needed. |

### 👀 Worked example: how many boxes?

```python
def boxes_needed(books, per_box):
    return math.ceil(books / per_box)
```

`boxes_needed(25, 10)`: 25 ÷ 10 = 2.5, rounded up = `3` boxes (the half-full box still counts).

## 🎯 Your quest

1. `plan(minutes_per_day, lessons, minutes_per_lesson=20)`: how many **days** to finish, rounded up:
   - `total_minutes = lessons * minutes_per_lesson`
   - `return math.ceil(total_minutes / minutes_per_day)`
2. `PICK`: write the name of the course you'll do next between the quotes.

**Remember:** levels in order, math alongside, one lesson a day.
