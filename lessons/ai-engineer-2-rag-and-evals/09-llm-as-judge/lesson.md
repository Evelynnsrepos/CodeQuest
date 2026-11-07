---
title: LLM-as-judge, done carefully
minutes: 45
xp: 60
hint: parse_verdict: m = re.search(r"\{.*?\}", text, re.S), if m is None: return None, then try: data = json.loads(m.group(0)) and w = data.get("winner")
hint: parse_verdict: except (json.JSONDecodeError, AttributeError): return None. Then if w in ["A", "B", "tie"]: return w, else return None
hint: pairwise: first = parse_verdict(judge(question, x, y)), second = parse_verdict(judge(question, y, x)). x wins only if first == "A" and second == "B"
hint: kappa: p_o = share of positions where a[i] == b[i]. p_e: for label in set(a) | set(b): add (a.count(label) / n) * (b.count(label) / n)
---
# Let a model grade, then check the grader

⏱️ About 45 minutes

> **Warm-up:** you have 500 answers to grade. Reading them takes a day. What could go wrong if a model grades them instead?

For open-ended answers there's no exact "right string", so teams use a strong model as a **judge**. It's cheap and fast, and it's biased in known ways:

- **Position bias:** in "A or B?", judges prefer one position. Fix: ask twice with A and B **swapped**, and only count a win if both orders agree; otherwise it's a tie.
- **Verbosity bias:** longer answers look better. Fix: say in the rubric that length isn't quality.
- **Self-preference:** models like their own style. Fix: use a different model family as judge.
- **Format drift:** the judge answers in prose. Fix: demand JSON like `{"winner": "A", "reason": "..."}` and validate it (LLMs 9 lesson 08).

**Then validate the judge itself:** grade 50 items by hand, run the judge on the same items, and measure **agreement**. Raw agreement flatters (two random graders agree 50% of the time on yes/no), so use **Cohen's κ** (kappa):

**κ = (p_o − p_e) / (1 − p_e)**, where `p_o` is how often the two agree, and `p_e` how often they'd agree by chance: the sum over labels of (share of A's labels that are this label) × (share of B's).

κ above about 0.6 is "substantial agreement": trust the judge for this task. Below 0.4, fix the rubric.

## 🧮 Worked example

You and the judge each grade the same 10 answers "good" or "bad". You both say "good" 6 times, and you agree on 8 of the 10.

1. **p_o** (agreement you saw) = 8 ÷ 10 = **0.8**
2. **p_e** (agreement by luck) = 0.6 · 0.6 (both "good") + 0.4 · 0.4 (both "bad") = 0.36 + 0.16 = **0.52**
3. **κ** = (0.8 − 0.52) ÷ (1 − 0.52) = 0.28 ÷ 0.48 = **0.58**

80% agreement sounds great, but κ = 0.58 is just under "substantial": tighten the rubric a little before trusting this judge.

The signs: `p_o` is "p observed" (the agreement you actually saw), `p_e` is "p expected" (what two people who guess at random with the same habits would agree on), and `κ` is the Greek letter **kappa**. κ = 1 is perfect agreement, κ = 0 is no better than luck.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `re.search(r"\{.*?\}", text, re.S)` | | finds the first `{...}` in the text. `.*?` means "as little as possible", `re.S` lets it cross line breaks. |
| `m.group(0)` | | the text it found |
| `except (json.JSONDecodeError, AttributeError):` | | catches two kinds of error: broken JSON, or JSON that isn't a dictionary (so it has no `.get`) |
| `judge(question, y, x)` | | the same judge, with the answers swapped |
| `set(a) \| set(b)` | "set a or set b" | every label that appears in either list |
| `a.count(label) / n` | | the share of a's labels that are this label |

### 👀 Worked example: the swap

Answers x and y. The judge says "A" when shown (x, y), so x won. Shown (y, x), it says "A" again: now that means y won. It just likes whatever comes first! first = "A", second = "A" → neither rule matches → **"tie"**. Only "A" then "B" (x wins in both orders) gives "x".

## 🎯 Your quest

1. `parse_verdict(text)`: find the first `{...}` in the text, `json.loads` it, and return its `"winner"` if it's `"A"`, `"B"` or `"tie"`; otherwise `None` (also on invalid JSON).
2. `pairwise(judge, question, x, y)`: `judge(question, a, b)` returns the judge's raw text. Ask with `(x, y)` and with `(y, x)`. Return `"x"` if x wins both times, `"y"` if y wins both, otherwise `"tie"`.
3. `kappa(a, b)`: Cohen's κ for two equal-length lists of labels.

**Part 1:** `parse_verdict`. Replace `return None` with:

1. `m = re.search(r"\{.*?\}", text, re.S)`
2. `if m is None:`
3. `    return None`
4. `try:`
5. `    data = json.loads(m.group(0))`
6. `    w = data.get("winner")`
7. `except (json.JSONDecodeError, AttributeError):`
8. `    return None`
9. `if w in ["A", "B", "tie"]:`
10. `    return w`
11. `return None`

**Part 2:** `pairwise`. Above its `return "tie"` line, type:

1. `first = parse_verdict(judge(question, x, y))`
2. `second = parse_verdict(judge(question, y, x))`
3. `if first == "A" and second == "B":`
4. `    return "x"`
5. `if first == "B" and second == "A":`
6. `    return "y"`

**Part 3:** `kappa`. Replace `return 0.0` with:

1. `n = len(a)`
2. `same = 0`
3. `for i in range(n):`
4. `    if a[i] == b[i]:`
5. `        same = same + 1`
6. `p_o = same / n`
7. `p_e = 0`
8. `for label in set(a) | set(b):`
9. `    p_e = p_e + (a.count(label) / n) * (b.count(label) / n)`
10. `if p_e == 1:`
11. `    return 1.0`
12. `return (p_o - p_e) / (1 - p_e)`

Lines 10 and 11: if both always give the same single label, 1 − p_e would be 0, and you can't divide by 0.

**Remember:** swap positions, demand JSON, measure the judge against humans.

## Review

<details><summary>Which HTTP errors are worth retrying?</summary>429 and 5xx and timeouts; not 400 or 401.</details>
