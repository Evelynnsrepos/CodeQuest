---
title: Statistics for evaluating models
minutes: 60
xp: 40
hint: mean: return sum(xs) / len(xs)
hint: std: m = mean(xs), total = 0, for x in xs: total = total + (x - m) ** 2, then return math.sqrt(total / (len(xs) - 1))
hint: ci95: se = std(xs) / math.sqrt(len(xs)), m = mean(xs), return (m - 1.96 * se, m + 1.96 * se)
hint: clearly_better: low, high = ci95(wins), then return low > 0.5
---
# Is the difference real?

⏱️ About 60 minutes

> **Warm-up:** your fine-tuned model beats the base model on 13 of 20 test prompts. Is it better?

Maybe. Flip a fair coin 20 times and you'll get 13 or more heads about 13% of the time. Small evaluations are **noisy**, and the capstone's "compare on 20 held-out prompts" needs you to know how noisy.

The tools:

```
mean            x̄ = (x₁ + … + xₙ) / n
sample std dev  s = √( Σ (xᵢ − x̄)² / (n − 1) )      (n − 1: "Bessel's correction")
standard error  SE = s / √n                         how much x̄ itself would wobble
95% confidence interval ≈ x̄ ± 1.96 · SE
```

Encode each prompt as **1** if the tuned model won and **0** if it lost; the mean is the **win rate**. If the confidence interval includes **0.5**, you can't tell the models apart yet: you need more prompts, or the difference is too small to matter.

Notice `√n` in the standard error: to halve the uncertainty you need **four times** as many prompts. That's why serious benchmarks have hundreds or thousands of items. (With very small n or win rates near 0 or 1, the ±1.96·SE shortcut gets rough; boot.dev's *Learn Statistics for Programmers* and proper tests like the binomial test or Wilson interval do better.)

Other habits that matter more than formulas:

- **Held-out** prompts the model never saw in training, written *before* you look at results.
- **Blind** judging: shuffle which answer is A and B so you can't favour your own model.
- Fixed settings (same temperature, same seed where possible), or several samples per prompt.

## 🔬 Take the formulas apart

**Mean** <div class="formula"><span class="k1">x̄</span> = (<span class="k2">x₁ + … + xₙ</span>) / <span class="k3">n</span></div>
`x̄` ("x bar") is the average. Add all <span class="k2">values</span>, divide by <span class="k3">how many</span> there are. [2, 4, 9]: 15 / 3 = **5**.

**Sample standard deviation** <div class="formula">s = <span class="k1">√</span>( <span class="k2">Σ (xᵢ − x̄)²</span> / <span class="k3">(n − 1)</span> )</div>
Inside out:
1. <span class="k2">xᵢ − x̄</span>: how far each value is from the mean. Square it, then Σ (add them all).
2. <span class="k3">divide by n − 1</span>, not n. With a small sample, your mean sits a bit too close to your own data, and n − 1 corrects for that ("Bessel's correction").
3. <span class="k1">√</span>: back to the original units.

Numbers, [1, 0, 1, 1] (won, lost, won, won): mean = 3/4 = 0.75.
1. Distances squared: (0.25)² = 0.0625 three times, (−0.75)² = 0.5625 once. Sum = 0.1875 + 0.5625 = 0.75.
2. Divide by 4 − 1 = 3: 0.25.
3. √0.25 = **0.5**.

**Standard error** <div class="formula">SE = <span class="k1">s</span> / <span class="k2">√n</span></div>
How much the **mean itself** would wobble if you repeated the test with new prompts. More prompts (<span class="k2">bigger n</span>) → smaller wobble. For [1, 0, 1, 1]: 0.5 / √4 = 0.5 / 2 = **0.25**.

**95% confidence interval** <div class="formula"><span class="k1">x̄</span> <span class="k2">±</span> <span class="k3">1.96</span> · SE</div>
`±` ("plus or minus") gives two numbers: one with −, one with +. <span class="k3">1.96</span> is a fixed number from statistics that makes the range catch the true value 95% of the time.

Your 13 of 20 wins: x̄ = 0.65, s ≈ 0.489, SE = 0.489 / √20 ≈ 0.489 / 4.47 ≈ 0.109.
- low = 0.65 − 1.96 × 0.109 ≈ 0.65 − 0.214 = **0.44**
- high = 0.65 + 0.214 = **0.86**

0.5 is inside [0.44, 0.86]: it could just be a coin flip. With 130 of 200 the interval is [0.58, 0.72]: entirely above 0.5.

<div class="wrong">❌ "65% win rate, so it's better."</div>
<div class="right">✅ "65%, but the interval reaches down to 44%: not clear yet."</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `sum(xs)` | "sum of xs" | adds all the numbers in the list |
| `(x - m) ** 2` | | the distance, squared |
| `math.sqrt(...)` | | square root |
| `return (low, high)` | | gives back two numbers together |
| `low, high = ci95(wins)` | | takes the two numbers into two names |
| `return low > 0.5` | | `>` already **is** a yes/no answer: `True` or `False`. No `if` needed. |

### 👀 Worked example: two numbers out, one yes/no back

```python
def range_of(xs):
    return (min(xs), max(xs))

lowest, highest = range_of([4, 9, 2])
print(lowest, highest)   # 2 9
print(lowest > 3)        # False
```

## 🎯 Your quest

`mean(xs)`: replace `return 0` with `    return sum(xs) / len(xs)`

`std(xs)`: replace `return 0` with:

1. `    m = mean(xs)`
2. `    total = 0`
3. `    for x in xs:`
4. `        total = total + (x - m) ** 2`
5. `    return math.sqrt(total / (len(xs) - 1))`

`ci95(xs)`: replace `return (0, 0)` with:

1. `    se = std(xs) / math.sqrt(len(xs))`
2. `    m = mean(xs)`
3. `    return (m - 1.96 * se, m + 1.96 * se)`

`clearly_better(wins)`: replace `return False` with:

1. `    low, high = ci95(wins)`
2. `    return low > 0.5`

## Review

<details><summary>Why is the LLM training loss called cross-entropy?</summary>It's the cross-entropy between the one-hot truth and the model's predicted distribution, which reduces to −log of the probability of the true token.</details>
<details><summary>Where does KL divergence show up in fine-tuning?</summary>RLHF and DPO keep the tuned model close to the reference model with a KL penalty; distillation minimizes KL to a teacher.</details>
<details><summary>To halve the standard error, how many more prompts do you need?</summary>Four times as many, because SE divides by √n and √4 = 2.</details>
