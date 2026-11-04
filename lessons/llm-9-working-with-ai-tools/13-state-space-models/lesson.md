---
title: Mamba and state space models
xp: 60
---
# A running note instead of looking back at everything

> **Warm-up:** attention lets every token look at every earlier token. For a 1-million-token context, how much does the model have to keep around?

**In one sentence:** a state space model keeps one fixed-size state and updates it once per token, so memory stays constant and cost grows linearly, at the price of weaker exact recall.

## 🪜 Plain words

Attention keeps a **KV cache** that grows with every token (LLMs 2). An SSM keeps a **state** h, like a running note:

- new state = (fade the old note) + (write in the new token)
- output = read from the note

Old information fades unless it's important. **Mamba** makes the fade and the writing depend on the input ("selective"), so it can choose what to keep. Recalling one exact detail from 50,000 tokens ago is hard for a fixed-size note, so **hybrids** (Jamba, Nemotron-H, Qwen3-Next) mix a few attention layers with many SSM layers. It's the RNN idea (AI beyond LLMs) made trainable in parallel.

## 🪜 With numbers

Single-number state, a = 0.5 (fade), b = 1 (write), c = 2 (read), inputs 1, 0, 0, 1:

| t | x | h = 0.5·h + 1·x | y = 2·h |
|---|---|---|---|
| 1 | 1 | 1 | 2 |
| 2 | 0 | 0.5 | 1 |
| 3 | 0 | 0.25 | 0.5 |
| 4 | 1 | 1.125 | 2.25 |

Memory: a layer with 8 KV heads of size 128 stores 2 · 8 · 128 = 2,048 numbers **per token**. A Mamba layer with an 8,192 × 16 state stores 131,072 numbers **total**. Break-even at 131,072 / 2,048 = **64 tokens**; at 32,768 tokens the KV cache is 512× bigger.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `hₜ` | "h t" | the state after token t | `h` |
| `Ā` | "A bar" | how the old state fades (bar = discretized) | `a` |
| `B̄` | "B bar" | how the new input is written in | `b` |
| `C` | "C" | how the output is read out | `c` |
| `xₜ`, `yₜ` | "x t", "y t" | input, output at step t | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">hₜ</span> = <span class="k2">Ā</span> <span class="k3">hₜ₋₁</span> + <span class="k4">B̄</span> <span class="k5">xₜ</span>, &nbsp;&nbsp; <span class="k6">yₜ</span> = C <span class="k1">hₜ</span></div>

| Piece | Means | t = 4 |
|---|---|---|
| <span class="k3">hₜ₋₁</span> | yesterday's note | 0.25 |
| <span class="k2">Ā</span> · | fade it | 0.125 |
| <span class="k4">B̄</span> <span class="k5">xₜ</span> | write the new token | 1 |
| <span class="k1">hₜ</span> | new note | 1.125 |
| <span class="k6">yₜ</span> = C hₜ | read it | 2.25 |

## 🔀 What if it were different?

<div class="wrong"><b>|a| > 1</b> (a = 1.5): the note grows every step and explodes (the RNN problem, Math 2 lesson 14).</div>
<div class="wrong"><b>a = 0</b>: the note forgets everything each step; the model only sees the current token.</div>
<div class="wrong"><b>"SSMs beat attention at everything"</b>: they are cheaper for long context, but weaker at copying exact details from far back; that's why hybrids exist.</div>
<div class="right">h = a·h + b·x, y = c·h: 2, 1, 0.5, 2.25 ✓</div>

## 🎯 Your quest

1. `ssm_scan(xs, a, b, c)`: start with h = 0, return the list of outputs y.
2. `kv_numbers(tokens, kv_heads, d_head)`: 2 · kv_heads · d_head · tokens (one layer).
3. `break_even_tokens(d_inner, d_state, kv_heads, d_head)`: the token count where KV numbers reach the SSM state size (d_inner · d_state), rounded up.

**Remember:** SSM = fixed-size running note: constant memory, fuzzy long recall.

## Review

<details><summary>What does the MoE balancing loss equal when perfectly balanced?</summary>α (E · Σ fP = 1).</details>
