---
title: LLM-as-judge, done carefully
xp: 60
---
# Let a model grade, then check the grader

> **Warm-up:** you have 500 answers to grade. Reading them takes a day. What could go wrong if a model grades them instead?

For open-ended answers there's no exact "right string", so teams use a strong model as a **judge**. It's cheap and fast, and it's biased in known ways:

- **Position bias:** in "A or B?", judges prefer one position. Fix: ask twice with A and B **swapped**, and only count a win if both orders agree; otherwise it's a tie.
- **Verbosity bias:** longer answers look better. Fix: say in the rubric that length isn't quality.
- **Self-preference:** models like their own style. Fix: use a different model family as judge.
- **Format drift:** the judge answers in prose. Fix: demand JSON like `{"winner": "A", "reason": "..."}` and validate it (LLMs 9 lesson 08).

**Then validate the judge itself:** grade 50 items by hand, run the judge on the same items, and measure **agreement**. Raw agreement flatters (two random graders agree 50% of the time on yes/no), so use **Cohen's κ** (kappa):

**κ = (p_o − p_e) / (1 − p_e)**, where `p_o` is how often the two agree, and `p_e` how often they'd agree by chance: the sum over labels of (share of A's labels that are this label) × (share of B's).

κ above about 0.6 is "substantial agreement": trust the judge for this task. Below 0.4, fix the rubric.

## Your quest

1. `parse_verdict(text)`: find the first `{...}` in the text, `json.loads` it, and return its `"winner"` if it's `"A"`, `"B"` or `"tie"`; otherwise `None` (also on invalid JSON).
2. `pairwise(judge, question, x, y)`: `judge(question, a, b)` returns the judge's raw text. Ask with `(x, y)` and with `(y, x)`. Return `"x"` if x wins both times, `"y"` if y wins both, otherwise `"tie"`.
3. `kappa(a, b)`: Cohen's κ for two equal-length lists of labels.

**Remember:** swap positions, demand JSON, measure the judge against humans.

## Review

<details><summary>Which HTTP errors are worth retrying?</summary>429 and 5xx and timeouts; not 400 or 401.</details>
