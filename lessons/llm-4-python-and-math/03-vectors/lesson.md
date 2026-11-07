---
title: Vectors
minutes: 50
xp: 30
hint: add: out = [], for i in range(len(a)): out.append(a[i] + b[i]), return out
hint: scale: out = [], for x in a: out.append(c * x), return out
hint: dot: total = 0, for i in range(len(a)): total = total + a[i] * b[i], return total
hint: norm: return math.sqrt(dot(a, a))
hint: rms_norm: rms = math.sqrt(dot(a, a) / len(a)), then out = [], for x in a: out.append(x / rms), return out
---
# Lists of numbers with a direction

⏱️ About 50 minutes

> **Warm-up:** in LLMs 1 you used embeddings and dot products. What does it mean, geometrically, to *add* two vectors?

A **vector** is a list of numbers, and you can picture it as an arrow from the origin. `[3, 4]` points 3 right and 4 up. The basic operations:

| Operation | Formula | Picture |
|---|---|---|
| addition `a + b` | `[a₁+b₁, a₂+b₂, …]` | put the arrows tip to tail |
| scaling `c·a` | `[c·a₁, c·a₂, …]` | stretch (or flip, if c < 0) |
| dot product `a · b` | `a₁b₁ + a₂b₂ + …` | `\|a\|·\|b\|·cos(angle)`: how much they point the same way |
| length (norm) `\|a\|` | `√(a · a)` | Pythagoras: `\|[3, 4]\| = 5` |

Every one of these is used in an LLM thousands of times per token:

- the **residual stream**: each layer *adds* its output vector onto the token's vector
- **scaling**: the learning rate scales the gradient vector before it's subtracted from the weights
- **dot products**: attention scores, logits
- **norms**: RMSNorm divides a vector by its (root-mean-square) length to keep sizes stable; gradient clipping caps the gradient's norm

The famous example of meaning-as-direction: in classic word embeddings, `vec("king") − vec("man") + vec("woman")` lands near `vec("queen")`.

## 🔬 Take the formulas apart

**The small numbers.** `a₁` ("a sub one") means "the first entry of a", `a₂` the second. In Python they are `a[0]` and `a[1]`, because Python counts from 0. The `…` means "and so on, for every entry".

**Addition** <div class="formula"><span class="k1">a + b</span> = [<span class="k2">a₁+b₁</span>, <span class="k3">a₂+b₂</span>, …]</div>
Add the matching entries. `[1, 2] + [3, 4]` = [1+3, 2+4] = **[4, 6]**.

**Scaling** <div class="formula"><span class="k1">c·a</span> = [<span class="k2">c·a₁</span>, <span class="k3">c·a₂</span>, …]</div>
The dot `·` here means "times". `c` is one plain number. Multiply every entry by it: 2·[1, −1] = **[2, −2]**.

**Dot product** <div class="formula"><span class="k1">a · b</span> = <span class="k2">a₁b₁</span> + <span class="k3">a₂b₂</span> + …</div>
`a₁b₁` written side by side also means "times". Multiply the matching entries, then add **all** of them into one number: [1, 2, 3] · [4, 5, 6] = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = **32**.

**Length (norm)** <div class="formula"><span class="k1">|a|</span> = <span class="k2">√</span>(<span class="k3">a · a</span>)</div>
- The bars `| |` around a vector mean "its length".
- `√` is the **square root**: "which number times itself gives this?" √25 = 5 because 5 × 5 = 25.
- For `[3, 4]`: a · a = 3×3 + 4×4 = 9 + 16 = 25, and √25 = **5**. That's Pythagoras: an arrow 3 right and 4 up is 5 long.

**Root mean square** <div class="formula">rms = <span class="k1">√</span>( <span class="k2">(a₁² + a₂² + …)</span> <span class="k3">/ n</span> )</div>
Read it from the inside out, which is the order you compute it:
1. <span class="k2">square</span> every entry (`²` means "times itself") and add them. That's `a · a` again.
2. <span class="k3">divide by n</span>, the number of entries: the **mean** (average) of the squares.
3. take the <span class="k1">square root</span>: the **root** of the mean of the squares.

For `[3, 4]`: 9 + 16 = 25, 25 / 2 = 12.5, √12.5 ≈ 3.536. `rms_norm` divides every entry by it: [3 / 3.536, 4 / 3.536] ≈ **[0.849, 1.131]**.

<div class="wrong">❌ Dividing by the length |a| instead: the result's length is 1, but with many entries each entry gets tiny.</div>
<div class="right">✅ Dividing by the rms: the entries stay "about size 1" each, however many there are. That's what RMSNorm wants.</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `for i in range(len(a)):` | | goes through the positions 0, 1, 2, … of `a` |
| `a[i] + b[i]` | "a at i plus b at i" | the matching entries of both lists |
| `for x in a:` | | goes through the entries themselves |
| `total = total + a[i] * b[i]` | | a **running total**: adds one more product each round |
| `math.sqrt(25)` | "square root of 25" | `5.0` |
| `dot(a, a)` | | you may use your own functions inside others |

### 👀 Worked example: two shopping lists

Prices `p = [2, 5]` (bread, cheese) and amounts `n = [3, 1]`.

```python
def total_cost(p, n):
    total = 0
    for i in range(len(p)):
        total = total + p[i] * n[i]
    return total
```

1. `i` = 0: total = 0 + 2×3 = 6.
2. `i` = 1: total = 6 + 5×1 = **11**.

That's a dot product: "price times amount, all added up". Your `dot` is exactly this.

## 🎯 Your quest

Replace each placeholder `return` with these lines (4 spaces inside each function):

`add(a, b)`:

1. `    out = []`
2. `    for i in range(len(a)):`
3. `        out.append(a[i] + b[i])`
4. `    return out`

`scale(c, a)`:

1. `    out = []`
2. `    for x in a:`
3. `        out.append(c * x)`
4. `    return out`

`dot(a, b)`:

1. `    total = 0`
2. `    for i in range(len(a)):`
3. `        total = total + a[i] * b[i]`
4. `    return total`

`norm(a)`: `    return math.sqrt(dot(a, a))`

`rms_norm(a)`:

1. `    rms = math.sqrt(dot(a, a) / len(a))`
2. `    out = []`
3. `    for x in a:`
4. `        out.append(x / rms)`
5. `    return out`

(Real RMSNorm also adds a tiny number and multiplies by learned weights; leave those out.) The last line prints `[0.849, 1.131]`.

## Review

<details><summary>What does __call__ do in a Python class?</summary>It runs when you call the object like a function: model(x).</details>
<details><summary>How are big models built from classes?</summary>By nesting: blocks hold attention and MLP objects, the model holds a list of blocks.</details>
<details><summary>What is |[6, 8]|?</summary>√(6×6 + 8×8) = √(36 + 64) = √100 = 10.</details>
