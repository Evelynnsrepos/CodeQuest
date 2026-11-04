---
title: The roadmap, and where boot.dev fits
xp: 15
---
# The gate to training

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

## Your quest

`ROADMAP` lists the courses in order. Write `next_course(done)`: given a set of finished course names, return the first course in `ROADMAP` that isn't finished, or `"all done"`. Then put the courses you've *actually* finished into `my_done` and run it.

## Review

<details><summary>Will a 14B model at Q4_K_M with 8k context fit in 11 GB?</summary>No: about 8.9 GB of weights + 1.3 GB KV cache + 1 GB overhead ≈ 11.2 GB.</details>
<details><summary>Name the three parts of an MCP server entry for a stdio server.</summary>command, args and (optionally) env.</details>
