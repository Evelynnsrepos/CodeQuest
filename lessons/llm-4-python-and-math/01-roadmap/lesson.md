---
title: The roadmap, and where boot.dev fits
minutes: 20
xp: 15
hint: Loop over the list in order: for course in ROADMAP:
hint: Inside the loop: if course not in done: and under it return course
hint: After the loop (4 spaces, not 8): return "all done"
hint: my_done is a set: my_done = {"Learn Coding Basics"} if you finished that one, or set() for none
---
# The gate to training

⏱️ About 20 minutes

> **Warm-up:** which parts of the earlier modules felt like "I followed the steps" rather than "I could write this myself"?

Modules 1–3 needed only a little Python. Modules 5–7 (training) are written in Python with PyTorch, and they rest on three kinds of math: **linear algebra** (everything is matrix multiplication), **calculus** (training follows derivatives downhill) and **probability** (a model outputs distributions, and the loss is a probability measure). This module builds all three in plain Python, so that when PyTorch does them for you, you know what it's doing.

Run it in parallel with boot.dev. The courses that matter for AI, in order (names from boot.dev's public roadmap; they change, so check the site):

| # | boot.dev course | Why it matters here |
|---|---|---|
| 1 | Learn Coding Basics (Python) | variables, loops, functions: everything uses them |
| 2 | Learn Linux, Learn Git | model files, servers, repos, your capstone on GitHub |
| 3 | Build a Bookbot | first real program reading files: datasets are files |
| 4 | Learn Object Oriented Programming | PyTorch models are classes (lesson 2 here) |
| 5 | Build an AI Agent (Python) | LLMs 3's agent loop against a real API |
| 6 | Learn Statistics for Programmers | probability and evaluation (lessons 9–11 here) |
| 7 | Learn Retrieval Augmented Generation | RAG done properly |

**New to math?** Do the Math for AI track first (Math 1: Reading math → Math 5: Information theory and optimization). It starts from arithmetic, explains every sign, and builds the same formulas this module uses step by step. This module then works as the fast applied bridge into training.

For math intuition, watch alongside: 3Blue1Brown's *Essence of Linear Algebra* (chapters 1–4 and 9) and *Essence of Calculus* (chapters 1–4), plus Khan Academy for practice problems. This module goes further than "intuition level" on purpose: you'll implement the gradient of softmax + cross-entropy yourself, which is the exact formula every LLM is trained with.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for course in ROADMAP:` | "for each course in the roadmap" | goes through the list **in order**, first to last |
| `if course not in done:` | "if the course is not in done" | true when the set `done` doesn't hold that course |
| `return course` | | stops the function **right now** and gives back that course. The loop doesn't go on. |
| `return "all done"` after the loop | | only reached if the loop finished without returning |
| `{"a", "b"}` | "a set of a and b" | a **set**: a bag of things with no order and no repeats |
| `set()` | "an empty set" | a set with nothing in it. (`{}` would be an empty *dictionary*.) |

### 👀 Worked example: the first unread book

```python
SHELF = ["Momo", "Heidi", "Pippi"]

def next_book(read):
    for book in SHELF:
        if book not in read:
            return book
    return "all read"

print(next_book({"Momo"}))
```

1. `book` = `"Momo"`: it **is** in `read`, so the `if` is false. Next.
2. `book` = `"Heidi"`: not in `read` → `return "Heidi"`. Done, `"Pippi"` is never looked at.
3. With `next_book({"Momo", "Heidi", "Pippi"})`, every `if` is false, the loop ends, and the last line gives `"all read"`.

## 🎯 Your quest

**Part 1:** write `next_course(done)`. Replace `return ""` with:

1. `for course in ROADMAP:`
2. `    if course not in done:`
3. `        return course`
4. `return "all done"`

**Part 2:** change `my_done = set()` to the courses you've really finished, for example `my_done = {"Learn Coding Basics", "Learn Linux"}`. The names must match `ROADMAP` exactly. Nothing finished yet? Leave it as `set()`.

## Review

<details><summary>Will a 14B model at Q4_K_M with 8k context fit in 11 GB?</summary>No: about 8.9 GB of weights + 1.3 GB KV cache + 1 GB overhead ≈ 11.2 GB.</details>
<details><summary>Name the three parts of an MCP server entry for a stdio server.</summary>command, args and (optionally) env.</details>
