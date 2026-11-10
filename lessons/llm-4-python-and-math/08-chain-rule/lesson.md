---
title: The chain rule, and the gradient every LLM trains with
minutes: 70
xp: 50
hint: sigmoid: return 1 / (1 + math.exp(-z))
hint: dsigmoid: s = sigmoid(z), then return s * (1 - s)
hint: ce_grad: grad = softmax(logits), then grad[target] = grad[target] - 1, then return grad
---
# Derivatives of nested functions

⏱️ About 70 minutes

> **Warm-up:** a model is a function inside a function inside a function, hundreds deep. If you know how each piece changes, how do you get how the whole thing changes?

Multiply. The **chain rule**: if `y = f(g(x))`, then

```
dy/dx = f'(g(x)) · g'(x)          ("outer derivative at the inner value, times inner derivative")
```

Intuition: if `g` doubles any change in `x`, and `f` triples any change in `g`, the whole thing sextuples it. **Backpropagation** (Module 5) is nothing but the chain rule applied systematically from the loss back through every layer.

**Example 1: the sigmoid** `σ(z) = 1 / (1 + e⁻ᶻ)`, a classic activation that squashes any number into (0, 1). Write it as `σ(z) = u⁻¹` with `u = 1 + e⁻ᶻ`:

```
dσ/du = −u⁻²        du/dz = −e⁻ᶻ
dσ/dz = −u⁻² · (−e⁻ᶻ) = e⁻ᶻ / (1 + e⁻ᶻ)²  = σ(z) · (1 − σ(z))
```

That last neat form is why sigmoid was popular: its derivative reuses its own output.

**Example 2: softmax + cross-entropy**, the loss of every LLM. For logits `z`, probabilities `p = softmax(z)` and the true next token `t`, the loss is `L = −log p_t`. Working the chain rule through softmax (a page of algebra, worth doing once on paper) gives a stunningly simple result:

```
∂L/∂zᵢ = pᵢ − yᵢ          where y is 1 for the true token and 0 elsewhere ("one-hot")
```

In words: the gradient **pushes up the true token's logit** by how much probability it was missing, and **pushes down every other logit** by exactly the probability it wrongly received. Every training step of every LLM starts with this vector.

## 🔬 Take the formulas apart

**The number e and exp.** `e` ≈ 2.718 is a special number, like π. `eˣ` ("e to the x") is written `math.exp(x)` in Python. e⁰ = 1, e¹ ≈ 2.718, e² ≈ 7.39. A **minus** in the power flips it: e⁻² = 1 / e² ≈ 0.135. So e⁻ᶻ is big when z is very negative and tiny when z is big.

**The chain rule** <div class="formula">dy/dx = <span class="k1">f'(g(x))</span> · <span class="k2">g'(x)</span></div>
- `dy/dx` reads "d y by d x": how fast y changes when x changes. Same idea as f'(x).
- `f(g(x))` is a function inside a function: first do `g`, then `f` on the result.
- <span class="k2">g'(x)</span>: how much the inner part reacts to x.
- <span class="k1">f'(g(x))</span>: how much the outer part reacts to its input, measured where that input is right now.
- Multiply them.

Numbers: y = (3x)². Inner g(x) = 3x, so g' = 3. Outer f(u) = u², so f'(u) = 2u. At x = 1: u = 3, f'(3) = 6. Chain rule: 6 × 3 = **18**. Check by expanding: (3x)² = 9x², slope 18x, at x = 1 that's 18. ✅

**Sigmoid** <div class="formula">σ(z) = <span class="k1">1</span> / (<span class="k2">1 + e⁻ᶻ</span>)</div>
`σ` is the Greek letter sigma, here just the name of the function.

1. z = 0: e⁰ = 1, so σ = 1 / (1 + 1) = **0.5**.
2. z = 4: e⁻⁴ ≈ 0.018, so σ ≈ 1 / 1.018 ≈ **0.98** (close to 1).
3. z = −4: e⁴ ≈ 54.6, so σ ≈ 1 / 55.6 ≈ **0.018** (close to 0).

Any number goes in; something between 0 and 1 comes out.

**Its slope** <div class="formula">σ'(z) = <span class="k1">σ(z)</span> · (<span class="k2">1 − σ(z)</span>)</div>
At z = 0: 0.5 × (1 − 0.5) = **0.25**, the steepest point. At z = 4: 0.98 × 0.02 ≈ 0.02, nearly flat. You don't need to redo the algebra above; the check compares your answer with a numerical slope (lesson 6) to show it's right.

**The LLM gradient** <div class="formula">∂L/∂zᵢ = <span class="k1">pᵢ</span> − <span class="k2">yᵢ</span></div>
- `zᵢ` is logit number i (a raw score), `pᵢ` its probability after softmax (LLMs 1).
- <span class="k2">yᵢ</span> is **1** for the true next token and **0** for all others. That list is called "one-hot".
- So: subtract 1 from the true token's probability, leave the rest as they are.

Numbers: p = [0.659, 0.242, 0.099], true token 1. Gradient = [0.659, 0.242 − 1, 0.099] = **[0.659, −0.758, 0.099]**. The minus means "push this logit **up**"; the others get pushed down. The entries add up to 0.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `math.exp(-z)` | "e to the minus z" | e⁻ᶻ |
| `1 / (1 + math.exp(-z))` | | the brackets make sure you divide by the **whole** bottom |
| `s = sigmoid(z)` | | compute once, keep it in `s`, use it twice |
| `grad = softmax(logits)` | | a fresh list of probabilities |
| `grad[target] = grad[target] - 1` | | change one entry: the true token's |

`softmax` and `cross_entropy` are given (written with plain loops).

### 👀 Worked example: the same shape with other numbers

```python
s = sigmoid(2)        # 1 / (1 + e⁻²) = 1 / 1.135 ≈ 0.881
slope = s * (1 - s)   # 0.881 × 0.119 ≈ 0.105

grad = [0.2, 0.5, 0.3]      # pretend softmax output
grad[0] = grad[0] - 1       # true token is 0
print(grad)                 # [-0.8, 0.5, 0.3]
```

## 🎯 Your quest

`sigmoid(z)`: replace `return 0` with `    return 1 / (1 + math.exp(-z))`

`dsigmoid(z)`: replace `return 0` with:

1. `    s = sigmoid(z)`
2. `    return s * (1 - s)`

`ce_grad(logits, target)`: replace `return []` with:

1. `    grad = softmax(logits)`
2. `    grad[target] = grad[target] - 1`
3. `    return grad`

The program prints the gradient `[0.659, -0.758, 0.099]`.

## Review

<details><summary>Which direction does the gradient point?</summary>The direction of steepest increase. Gradient descent steps the opposite way.</details>
<details><summary>What goes wrong with a learning rate that's too large?</summary>Steps overshoot the minimum; the loss bounces or explodes.</details>
<details><summary>What is σ(0)?</summary>0.5: e⁰ = 1, and 1 / (1 + 1) = 0.5.</details>
