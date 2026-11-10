---
title: Multi-head attention
minutes: 50
xp: 50
hint: split_heads: w = len(rows[0]) // n_heads, heads = [], for h in range(n_heads): head = [], for row in rows: head.append(row[h * w:(h + 1) * w])
hint: split_heads continued: heads.append(head) after the inner loop, and return heads at the end
hint: multi_head: Qs = split_heads(Q, n_heads), the same for Ks and Vs, then outputs.append(causal_attention(Qs[h], Ks[h], Vs[h])) for each h
hint: Joining: for i in range(len(Q)): row = [], for h in range(n_heads): row = row + outputs[h][i], then result.append(row)
---
# Many heads look at different things

⏱️ About 50 minutes

> **Warm-up:** one attention head produces one set of weights per token. Can a single set of weights track both "which noun does *it* refer to" and "which word came right before me"?

Not well. So a transformer layer runs **several heads in parallel**. With model width `d = 4096` and `h = 32` heads (Llama 3 8B), each head works on `d / h = 128` numbers:

1. Compute Q, K, V for every position as usual (each a `d`-wide row).
2. **Split** each row into `h` slices of `d/h` numbers. Slice number `i` of every row belongs to head `i`.
3. Run causal attention **per head** on its slices.
4. **Concatenate** the heads' outputs back into one `d`-wide row per position, then multiply by an output matrix `W_O` (skipped here).

It costs the same as one big head (the slices add up to `d`), but each head gets its own softmax, so each can attend somewhere different. Interpretability research found heads that do specific jobs, such as **induction heads**, which copy patterns ("A B … A → B") and are a big part of in-context learning.

**Causal** means position `i` only attends to positions `0..i`: a model that predicts the next token must not peek at it. In real code this is a **mask** that sets future scores to −∞ before the softmax.

Modern variant: **grouped-query attention (GQA)** lets several query heads share one K/V head (Llama 3 8B: 32 query heads, 8 K/V heads), which shrinks the KV cache 4×. You met its effect in LLMs 2's VRAM math.

## 🔬 Take it apart: cutting a row into heads

With 4 numbers per row and 2 heads, each head gets a slice of width w = 4 // 2 = **2**:

- head 0 gets positions 0–1: `row[0:2]`
- head 1 gets positions 2–3: `row[2:4]`

In general head h gets `row[h * w:(h + 1) * w]`: for h = 1, that's `row[2:4]`.

Row `[1, 0, 0, 1]` → head 0 sees `[1, 0]`, head 1 sees `[0, 1]`. Each head runs its own attention on its own slices, then the results are glued back side by side: `[head 0's 2 numbers] + [head 1's 2 numbers]` = 4 numbers again.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(rows[0]) // n_heads` | | slice width, a whole number |
| `row[h * w:(h + 1) * w]` | | the slice for head h |
| `heads.append(head)` | | one list of slices per head |
| `causal_attention(Qs[h], Ks[h], Vs[h])` | (given) | one head's attention, from LLMs 5 lesson 12 |
| `outputs[h][i]` | | head h's output row for position i |
| `row = row + outputs[h][i]` | | glue lists end to end |

### 👀 Worked example: splitting three rows

`Q = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0]]`, 2 heads:

1. h = 0: slices `[0:2]` of each row → `[[1, 0], [0, 1], [1, 1]]`
2. h = 1: slices `[2:4]` → `[[0, 1], [1, 0], [0, 0]]`

That's exactly the first line the program prints.

## 🎯 Your quest

`split_heads(rows, n_heads)`: replace `return []` with:

1. `    w = len(rows[0]) // n_heads`
2. `    heads = []`
3. `    for h in range(n_heads):`
4. `        head = []`
5. `        for row in rows:`
6. `            head.append(row[h * w:(h + 1) * w])`
7. `        heads.append(head)`
8. `    return heads`

`multi_head(Q, K, V, n_heads)`: replace `return []` with:

1. `    Qs = split_heads(Q, n_heads)`
2. `    Ks = split_heads(K, n_heads)`
3. `    Vs = split_heads(V, n_heads)`
4. `    outputs = []`
5. `    for h in range(n_heads):`
6. `        outputs.append(causal_attention(Qs[h], Ks[h], Vs[h]))`
7. `    result = []`
8. `    for i in range(len(Q)):`
9. `        row = []`
10. `        for h in range(n_heads):`
11. `            row = row + outputs[h][i]`
12. `        result.append(row)`
13. `    return result`

Position 0 sees only itself, so its output is V[0] = `[1.0, 2.0, 3.0, 4.0]`.

## Review

<details><summary>Why divide attention scores by √d?</summary>Dot products grow with vector length; without scaling the softmax saturates and gradients vanish.</details>
<details><summary>What is a harness?</summary>The program around a model that builds prompts, runs tools, loops, manages context and asks for permissions.</details>
