---
title: Tiny GPT 2: the model
xp: 75
---
# LLMs 8 in sixty lines of PyTorch

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

## Your quest

Write both `forward` methods. The check tests the output shapes, that the first loss is near **ln(vocab)** (LLMs 8 checkpoint: a fresh model guesses uniformly), and that the model is really causal: changing a later token must not change earlier logits.

**Remember:** attention = scores, mask, softmax, mix; GPT = embed, blocks, norm, head.

## Review

<details><summary>In a language-model batch, how is y related to x?</summary>y is x shifted one position to the left: the next token at every position.</details>
