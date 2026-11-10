---
title: Tiny GPT 2: the model
minutes: 60
xp: 75
hint: Attention: B, T, C = x.shape, then q, k, v = self.qkv(x).split(C, dim=2) and hs = C // self.n_head
hint: Heads: q = q.view(B, T, self.n_head, hs).transpose(1, 2), and the same line for k and v
hint: Then att = q @ k.transpose(-2, -1) / math.sqrt(hs), the masked_fill line, y = att.softmax(dim=-1) @ v, undo the heads, return self.proj(y)
hint: TinyGPT: B, T = idx.shape, positions = torch.arange(T, device=idx.device), x = self.tok(idx) + self.pos(positions)
hint: TinyGPT: loss = None, and only if targets is not None: loss = F.cross_entropy(logits.view(B * T, -1), targets.view(B * T))
---
# LLMs 8 in sixty lines of PyTorch

⏱️ About 60 minutes

> **Warm-up:** name the parts of one transformer block, in order.

The model is the GPT from LLMs 8, written with PyTorch layers. Most of it is given; you write the two `forward` methods, which is where the ideas live.

**CausalSelfAttention.forward(x)**, with `x` of shape `(B, T, C)` (batch, time = tokens, channels = embedding size):

1. `self.qkv(x)` makes Q, K and V in one matrix multiply; `.split(C, dim=2)` cuts them apart.
2. **Heads:** reshape each to `(B, T, n_head, C // n_head)`, then `.transpose(1, 2)` → `(B, n_head, T, head_size)`. Each head now attends on its own.
3. Scores `q @ k.transpose(-2, -1) / √head_size`, shape `(B, n_head, T, T)`.
4. Causal mask: `att.masked_fill(~self.mask[:T, :T], float("-inf"))` (the buffer holds True on and below the diagonal).
5. `softmax(dim=-1)`, `@ v`, then undo the heads: `.transpose(1, 2).contiguous().view(B, T, C)`, and `self.proj`.

**TinyGPT.forward(idx, targets=None)**, with `idx` of shape `(B, T)` (token ids):

1. `x = self.tok(idx) + self.pos(torch.arange(T, device=idx.device))`: token embedding + position embedding.
2. `logits = self.head(self.ln_f(self.blocks(x)))`, shape `(B, T, vocab)`.
3. If `targets` is given: `F.cross_entropy(logits.view(B*T, -1), targets.view(B*T))`, else `None`. Return `(logits, loss)`.

Compare with the NumPy attention of lesson 03: same math, plus heads and batches.

## 🔬 The shapes, step by step

Follow one batch with B = 2 sequences, T = 8 tokens, C = 64 channels and 4 heads:

| Step | Shape | Why |
|---|---|---|
| `x` | (2, 8, 64) | 2 sequences, 8 tokens each, 64 numbers per token |
| `self.qkv(x)` | (2, 8, 192) | 3 × 64: Q, K and V side by side |
| `.split(64, dim=2)` | three times (2, 8, 64) | cut them apart |
| `hs = 64 // 4` | 16 | each head gets 16 of the 64 numbers |
| `.view(2, 8, 4, 16)` | (2, 8, 4, 16) | the 64 numbers regrouped as 4 heads × 16 |
| `.transpose(1, 2)` | (2, 4, 8, 16) | heads before tokens, so each head works on its own |
| `q @ k.transpose(-2, -1)` | (2, 4, 8, 8) | per head, every token's score with every token |
| `/ math.sqrt(16)` | | divide by 4 (√16 = 4, because 4 × 4 = 16) |
| `att.softmax(dim=-1) @ v` | (2, 4, 8, 16) | the mixed values |
| `.transpose(1, 2).contiguous().view(2, 8, 64)` | (2, 8, 64) | glue the heads back together |

**The first loss ≈ ln(vocab)**: a fresh model gives every one of 30 characters about the same chance, 1/30. Cross-entropy is −ln(chance of the right answer) = −ln(1/30) = ln 30 = **3.4**. (`ln` is the natural log, LLMs 4 lesson 10.)

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `B, T, C = x.shape` | | unpacks the three sizes into three names |
| `.view(...)` | | the same numbers in a new shape |
| `.transpose(1, 2)` | | swaps axis 1 and axis 2 |
| `.contiguous()` | | puts the numbers in memory in the new order, which `.view` needs after a transpose |
| `~self.mask[:T, :T]` | "not mask" | `~` flips True and False: True now marks the **future** tokens |
| `.masked_fill(m, float("-inf"))` | | puts −∞ where m is True |
| `torch.arange(T, device=idx.device)` | | 0, 1, ..., T − 1 on the same device as the ids: the positions |
| `self.tok(idx) + self.pos(positions)` | | token embedding plus position embedding |
| `logits.view(B * T, -1)` | | flattens to one row per token; `-1` means "work out this size yourself" |
| `F.cross_entropy(logits, targets)` | | the loss for "how likely was the right next character" |

## 🎯 Your quest

Write both `forward` methods. The check tests the output shapes, that the first loss is near **ln(vocab)** (LLMs 8 checkpoint: a fresh model guesses uniformly), and that the model is really causal: changing a later token must not change earlier logits.

**Part 1:** `CausalSelfAttention.forward`. Replace `return x` with (8 spaces in front of each, since it's inside a class method):

1. `B, T, C = x.shape`
2. `q, k, v = self.qkv(x).split(C, dim=2)`
3. `hs = C // self.n_head`
4. `q = q.view(B, T, self.n_head, hs).transpose(1, 2)`
5. `k = k.view(B, T, self.n_head, hs).transpose(1, 2)`
6. `v = v.view(B, T, self.n_head, hs).transpose(1, 2)`
7. `att = q @ k.transpose(-2, -1) / math.sqrt(hs)`
8. `att = att.masked_fill(~self.mask[:T, :T], float("-inf"))`
9. `y = att.softmax(dim=-1) @ v`
10. `y = y.transpose(1, 2).contiguous().view(B, T, C)`
11. `return self.proj(y)`

**Part 2:** `TinyGPT.forward`. Replace `return None, None` with:

1. `B, T = idx.shape`
2. `positions = torch.arange(T, device=idx.device)`
3. `x = self.tok(idx) + self.pos(positions)`
4. `x = self.blocks(x)`
5. `logits = self.head(self.ln_f(x))`
6. `loss = None`
7. `if targets is not None:`
8. `    loss = F.cross_entropy(logits.view(B * T, -1), targets.view(B * T))`
9. `return logits, loss`

**Remember:** attention = scores, mask, softmax, mix; GPT = embed, blocks, norm, head.

## Review

<details><summary>In a language-model batch, how is y related to x?</summary>y is x shifted one position to the left: the next token at every position.</details>
