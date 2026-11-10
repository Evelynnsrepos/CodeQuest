---
title: Your map of the AI courses
minutes: 15
xp: 30
hint: plan: total_minutes = lessons * minutes_per_lesson, then return math.ceil(total_minutes / minutes_per_day).
hint: For PICK, any of the PICK blocks is right. Choose the one you want to do next.
distractor: return total_minutes / minutes_per_day
distractor: PICK = "Math 1: Reading math"
distractor: PICK = "AI automation 1: Scripts"
distractor: PICK = "AI crash course"
---
# Where to go from here

⏱️ About 15 minutes · 🧩 3 gaps, one of them is your choice

> **Warm-up:** which of the last eleven lessons did you find most interesting? That's a good hint for where to go next.

**In one sentence:** you've seen every big idea once; the full courses go deep, level by level.

## 🗺️ The map

| Level | Courses | You'll be able to |
|---|---|---|
| **Start here** | the AI crash course (typing edition) | the same ideas again, now writing the code yourself |
| **Level 1 · Understand and use AI** | LLMs 1, 2, 3 | build each piece of an LLM in Python, run models on your PC, give them tools and RAG |
| **Level 2 · Train your own** | LLMs 4, 5, 6, 7, AI beyond LLMs | train a model from scratch, fine-tune it, evaluate and publish it |
| **Level 3 · Advanced and pro** | LLMs 8, 9, AI engineer 1, 2, 3 | understand frontier models and ship AI apps |

**Side tracks** any time: **Math for AI** (Math 1–6, from zero), **Python**, **AI automation**, **Data cleaning**.

A good next step after this puzzle course: do the normal **AI crash course**. It's the same 12 ideas, so you already know what every line means; now you get to type them yourself.

## 🔢 How many days? Step by step

14 lessons, 20 minutes each, 30 minutes a day:

1. Total minutes: 14 × 20 = **280**.
2. Days: 280 ÷ 30 = **9.33**.
3. Round **up** (like tokens in lesson 02): a third of a day is still a day → **10 days**.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `a * b` | "a times b" | multiply |
| `a / b` | "a divided by b" | divide, gives a decimal like 9.33 |
| `math.ceil(9.33)` | "ceiling of 9.33" | rounds **up**: 10 |
| `PICK = "..."` | "PICK becomes …" | puts a text into the box `PICK` |

## 🧩 Your puzzle

1. Total minutes: lessons × minutes per lesson.
2. Days: total ÷ minutes per day, rounded **up** (decoy: without `math.ceil` you'd get 9.33 days).
3. **Your choice:** put the course you'll do next into the PICK gap. Every PICK block is a right answer, the others stay in the tray.

Run it: `10 days; next: …` with your pick.

**Remember:** one lesson a day adds up fast.
