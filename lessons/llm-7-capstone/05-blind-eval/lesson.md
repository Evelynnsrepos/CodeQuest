---
title: Blind A/B evaluation against the base model
xp: 50
---
# Did fine-tuning actually help?

> **Warm-up:** if you know which answer came from your tuned model, can you judge fairly?

You can't. So hide it. For each held-out **test** prompt (never trained on), generate one answer from the base model and one from your tuned model (same quant, same temperature, same system prompt). Then shuffle which one is shown as **A** and which as **B**, and judge without knowing. Only after judging do you unblind.

Judging can be you, a friend, or a bigger model ("LLM as judge", which has known biases: it prefers longer answers and the answer shown first, so randomizing A/B matters even more).

Turn judgments into a number:

- **win rate** = (tuned wins + ½ × ties) ÷ n
- **95% confidence interval** (normal approximation, LLMs 4 lesson 11): `p ± 1.96 × sqrt(p(1−p)/n)`

If the interval includes 0.5, you haven't shown a difference yet: get more test prompts. With very few prompts the interval can even run past 0 or 1, which is the formula telling you n is far too small.

## Your quest

1. `make_pairs(base, tuned, seed)`: `base` and `tuned` are equal-length lists of answers. Use `random.Random(seed)`; for each index call `rng.random() < 0.5` once: if true, tuned is **A**, else tuned is **B**. Return a list of dicts `{"A": ..., "B": ..., "tuned": "A" or "B"}`.
2. `score(pairs, judgments)`: `judgments` is a list of `"A"`, `"B"` or `"tie"`. Return `(win_rate, low, high)` with the formula above, each rounded to 3 decimals.

## Review

<details><summary>In a training log, eval_loss keeps rising after step 400. Which checkpoint do you keep?</summary>The one with the lowest eval_loss, around step 400; later ones are overfitting.</details>
<details><summary>Why use the test split here, not the validation split?</summary>Validation was used to choose the checkpoint, so it's no longer an unbiased measure.</details>
