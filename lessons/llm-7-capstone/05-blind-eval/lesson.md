---
title: Blind A/B evaluation against the base model
minutes: 45
xp: 50
hint: make_pairs: rng = random.Random(seed), pairs = [], for i in range(len(base)): if rng.random() < 0.5: tuned is A, else: tuned is B
hint: The two appends: {"A": tuned[i], "B": base[i], "tuned": "A"} and {"A": base[i], "B": tuned[i], "tuned": "B"}
hint: score: wins = 0, then for i in range(n): j = judgments[i]; if j == "tie": wins = wins + 0.5, elif j == pairs[i]["tuned"]: wins = wins + 1
hint: score ends: p = wins / n, margin = 1.96 * math.sqrt(p * (1 - p) / n), return (round(p, 3), round(p - margin, 3), round(p + margin, 3))
---
# Did fine-tuning actually help?

⏱️ About 45 minutes

> **Warm-up:** if you know which answer came from your tuned model, can you judge fairly?

You can't. So hide it. For each held-out **test** prompt (never trained on), generate one answer from the base model and one from your tuned model (same quant, same temperature, same system prompt). Then shuffle which one is shown as **A** and which as **B**, and judge without knowing. Only after judging do you unblind.

Judging can be you, a friend, or a bigger model ("LLM as judge", which has known biases: it prefers longer answers and the answer shown first, so randomizing A/B matters even more).

Turn judgments into a number:

- **win rate** = (tuned wins + ½ × ties) ÷ n
- **95% confidence interval** (normal approximation, LLMs 4 lesson 11): `p ± 1.96 × sqrt(p(1−p)/n)`

If the interval includes 0.5, you haven't shown a difference yet: get more test prompts. With very few prompts the interval can even run past 0 or 1, which is the formula telling you n is far too small.

## 🔬 Take the formulas apart

**Win rate** <div class="formula">p = (<span class="k1">wins</span> + <span class="k2">½ × ties</span>) ÷ <span class="k3">n</span></div>
A tie counts as half a win. Judgments A, B, tie, A with tuned on A, A, B, A: win, loss, ½, win → 2.5 ÷ 4 = **0.625**.

**Interval** <div class="formula">p ± <span class="k1">1.96</span> × <span class="k2">√( p(1 − p) / n )</span></div>
- <span class="k2">√(p(1 − p)/n)</span> is the standard error of a win rate (LLMs 4, lesson 11, in its short form for yes/no data). p(1 − p) means p × (1 − p).
- 0.625 × 0.375 = 0.234. ÷ 4 = 0.0586. √ ≈ 0.242. × 1.96 ≈ 0.474.
- So 0.625 − 0.474 = **0.151** to 0.625 + 0.474 = **1.099**. Huge (and above 1, which shows the shortcut is rough with only 4 prompts). You need many more.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `rng = random.Random(seed)` | | your own random number maker, repeatable |
| `rng.random() < 0.5` | | a coin flip: true about half the time |
| `if … elif … :` | "else if" | `elif` is only checked when the `if` was false |
| `wins + 0.5` | | half a point for a tie |
| `round(p, 3)` | | 3 decimals |

### 👀 Worked example: one coin flip

`base[i] = "b1"`, `tuned[i] = "t1"`, flip true → `{"A": "t1", "B": "b1", "tuned": "A"}`. The judge sees only A and B. If they answer "A", that's a win, because `pairs[i]["tuned"]` is "A".

## 🎯 Your quest

`make_pairs(base, tuned, seed)`: replace `return []` with:

1. `    rng = random.Random(seed)`
2. `    pairs = []`
3. `    for i in range(len(base)):`
4. `        if rng.random() < 0.5:`
5. `            pairs.append({"A": tuned[i], "B": base[i], "tuned": "A"})`
6. `        else:`
7. `            pairs.append({"A": base[i], "B": tuned[i], "tuned": "B"})`
8. `    return pairs`

`score(pairs, judgments)`: replace `return (0, 0, 0)` with:

1. `    n = len(pairs)`
2. `    wins = 0`
3. `    for i in range(n):`
4. `        j = judgments[i]`
5. `        if j == "tie":`
6. `            wins = wins + 0.5`
7. `        elif j == pairs[i]["tuned"]:`
8. `            wins = wins + 1`
9. `    p = wins / n`
10. `    margin = 1.96 * math.sqrt(p * (1 - p) / n)`
11. `    return (round(p, 3), round(p - margin, 3), round(p + margin, 3))`

It prints `(0.625, 0.151, 1.099)`.

## Review

<details><summary>In a training log, eval_loss keeps rising after step 400. Which checkpoint do you keep?</summary>The one with the lowest eval_loss, around step 400; later ones are overfitting.</details>
<details><summary>Why use the test split here, not the validation split?</summary>Validation was used to choose the checkpoint, so it's no longer an unbiased measure.</details>
