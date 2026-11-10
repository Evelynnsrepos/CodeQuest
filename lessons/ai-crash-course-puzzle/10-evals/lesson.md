---
title: Evals, is it actually better?
minutes: 30
xp: 30
hint: accuracy: compare preds[i].strip().lower() == gold[i].strip().lower(), count with right = right + 1, then return right / len(gold).
hint: win_interval: p = wins / n, and give back (p - margin, p + margin). is_better: return low > 0.5.
distractor: if preds[i] == gold[i]:
distractor: return low > 0.6
---
# Evals

⏱️ About 30 minutes · 🧩 6 gaps, 2 decoys

> **Warm-up:** a new model won 6 of 10 test questions against the old one. Is it better?

**In one sentence:** an **eval** is a test set with right answers; you count how often the model is right, and you check the result isn't just **luck**.

## 💡 The idea

**Accuracy** = right answers ÷ all questions. Compare fairly: `"Paris"` and `"paris "` mean the same, so ignore capital letters and extra spaces.

**Luck:** flip a coin 10 times and you'll often get 6 heads. So "won 6 of 10" proves nothing. We draw an **interval** (a range) around the score: "the true win rate is probably between here and here". Only if the **whole range** is above 0.5 (50%) is the new model really better.

## 🔢 The maths, step by step

60 wins out of 100 games:

1. Win rate: p = 60 ÷ 100 = **0.6**.
2. How wobbly that is: p × (1 − p) ÷ n = 0.6 × 0.4 ÷ 100 = 0.24 ÷ 100 = **0.0024**.
3. Square root: √0.0024 ≈ **0.049**. (Remember: √ asks "which number times itself gives this?")
4. Times 2: **0.098**. This is the **margin**, how far either side to go. (The 2 makes it about 95% sure.)
5. Interval: 0.6 − 0.098 = **0.502** to 0.6 + 0.098 = **0.698**.
6. Is the low end above 0.5? 0.502 > 0.5 → yes, just about: **better**.

With 6 of 10: p is still 0.6, but n is only 10, so the margin is 2 × √(0.024) ≈ 0.31, and the low end is 0.29. Way below 0.5 → **not proven**. More test questions = smaller margin.

## 🐍 The Python in this puzzle

| Piece | Say it | What it does |
|---|---|---|
| `" Paris ".strip()` | "strip" | removes spaces at the ends: `"Paris"` |
| `"Paris".lower()` | "lower" | small letters: `"paris"` |
| `==` | "equals?" | `True` if both sides are the same. (One `=` puts into a box; two `==` compares.) |
| `right = right + 1` | | count one more |
| `(a, b)` | a pair | gives back two numbers at once |
| `win_interval(...)[0]` | "the first of the pair" | the low end |
| `1 - p` | "one minus p" | the losing rate |

## 🧩 Your puzzle

1. Compare after **strip and lower** (decoy: plain `==` would say "Paris" ≠ "paris").
2. If they match, count one more.
3. Accuracy: right ÷ how many.
4. The win rate p.
5. The interval: (p minus margin, p plus margin).
6. Better only if the low end is above **0.5** (decoy: 0.6).

Run it: `0.666… (0.502…, 0.697…) False`.

**Remember:** count fairly, then ask "could this be luck?"
