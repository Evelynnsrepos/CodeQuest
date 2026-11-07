---
title: Momentum, Adam, AdamW and LR schedules
minutes: 70
xp: 50
hint: adamw_step, inside the given loop (8 spaces): g = grads[i], then m[i] = beta1 * m[i] + (1 - beta1) * g
hint: Next: v[i] = beta2 * v[i] + (1 - beta2) * g * g
hint: Then m_hat = m[i] / (1 - beta1 ** t) and v_hat = v[i] / (1 - beta2 ** t)
hint: Last: params[i] = params[i] - lr * wd * params[i] - lr * m_hat / (math.sqrt(v_hat) + eps)
hint: lr_at: if step < warmup: return max_lr * (step + 1) / warmup. Then progress = (step - warmup) / (total - warmup)
hint: lr_at ends: return max_lr * 0.5 * (1 + math.cos(math.pi * progress))
---
# Smarter steps than plain SGD

⏱️ About 70 minutes

> **Warm-up:** in a long narrow valley, the gradient points mostly at the steep walls, not along the valley floor. What happens to plain gradient descent there?

It zig-zags between the walls and crawls along the floor. With a learning rate small enough not to explode on the steep direction, the shallow direction barely moves. Real loss surfaces are full of such valleys, so better optimizers keep extra state per weight:

**Momentum** keeps a running average of past gradients (`m`), so consistent directions build up speed and zig-zags cancel out.

**Adam** (Kingma & Ba, 2014) also tracks a running average of **squared** gradients (`v`) and divides by its square root. Every weight gets its own effective step size: steep directions are damped, shallow ones boosted. Both averages start at 0, so early on they're biased towards 0; Adam corrects that by dividing by `1 − βᵗ`.

**AdamW** (Loshchilov & Hutter, 2017) adds **weight decay** the right way: shrink every weight a little towards 0 each step, separately from the gradient. It's the default optimizer for training transformers, including every LLM fine-tune you'll run.

```
for each weight p with gradient g, at step t (starting at 1):
    m = β₁·m + (1 − β₁)·g
    v = β₂·v + (1 − β₂)·g²
    m̂ = m / (1 − β₁ᵗ)          v̂ = v / (1 − β₂ᵗ)
    p = p − lr·wd·p − lr · m̂ / (√v̂ + ε)
typical: β₁ = 0.9, β₂ = 0.999, ε = 1e-8, wd = 0.01
```

The cost: two extra numbers (`m`, `v`) **per weight**. That's why full fine-tuning needs so much memory (lesson 13) and why LoRA (Module 6) only trains a few weights.

**Learning-rate schedules.** Almost every LLM run uses **warmup** (ramp the LR up from ~0 over the first steps, while Adam's statistics are still unreliable) followed by **cosine decay** (smoothly down towards 0, so the end of training makes fine adjustments):

```
step < warmup:   lr = max_lr · (step + 1) / warmup
afterwards:      lr = max_lr · ½ · (1 + cos(π · progress)),  progress = (step − warmup) / (total − warmup)
```

## 🔬 Take the formulas apart

**The Greek letters are just names.** β₁ ("beta one") = 0.9 and β₂ ("beta two") = 0.999 control how long the averages remember. ε ("epsilon") = 0.00000001 is a tiny number that stops a division by 0. `t` is the step number: 1, 2, 3, …

**Line 1: the running average of the gradient** <div class="formula">m = <span class="k1">β₁·m</span> + <span class="k2">(1 − β₁)·g</span></div>
Keep <span class="k1">90% of the old average</span> and mix in <span class="k2">10% of the new gradient</span> g. A gradient that keeps pointing the same way builds up; one that flips back and forth (the zig-zag) cancels out.

**Line 2: the running average of the squared gradient** <div class="formula">v = <span class="k1">β₂·v</span> + <span class="k2">(1 − β₂)·g²</span></div>
The same, with g² (g times g). It measures "how big are the gradients here, usually?", ignoring the sign.

**Line 3: the start-up fix** <div class="formula">m̂ = m / <span class="k3">(1 − β₁ᵗ)</span></div>
`m̂` is "m hat". Both averages start at 0, so at first they're far too small. β₁ᵗ is β₁ multiplied by itself t times: 0.9¹ = 0.9, 0.9² = 0.81, … it shrinks towards 0. So <span class="k3">1 − β₁ᵗ</span> starts at 0.1 and grows to 1: a big correction at first, none later.

**Line 4: the step** <div class="formula">p = p − <span class="k1">lr·wd·p</span> − <span class="k2">lr · m̂ / (√v̂ + ε)</span></div>
- <span class="k1">lr·wd·p</span>: weight decay. Shrink the weight a tiny bit towards 0 (`wd` = weight decay, like 0.01).
- <span class="k2">m̂ / √v̂</span>: the average direction, divided by the typical size. Steep directions (big v̂) get damped, shallow ones boosted.

**Follow step 1 with numbers**, gradient g = 2, wd = 0:
1. m = 0.9·0 + 0.1·2 = 0.2
2. v = 0.999·0 + 0.001·4 = 0.004
3. m̂ = 0.2 / (1 − 0.9) = 0.2 / 0.1 = **2**. v̂ = 0.004 / (1 − 0.999) = 0.004 / 0.001 = **4**.
4. Step = lr · 2 / (√4 + ε) = lr · 2 / 2 = **lr · 1**.

With g = 200 you'd get exactly the same step: Adam cares about direction, not size. That's why it doesn't explode in the steep valley.

**The schedule**
<div class="formula">warmup: lr = max_lr · <span class="k1">(step + 1) / warmup</span></div>
A straight ramp: with warmup = 10, step 0 gives 1/10 of max_lr, step 4 gives 5/10, step 9 gives 10/10.

<div class="formula">afterwards: lr = max_lr · <span class="k2">½ · (1 + cos(π · progress))</span></div>

- `progress` goes from 0 (just after warmup) to almost 1 (the end).
- π ("pi") ≈ 3.14159. `cos` is a wave: cos(0) = 1, cos(π/2) = 0, cos(π) = −1.
- So 1 + cos goes 2 → 1 → 0, and ½ of that goes **1 → ½ → 0**: a smooth slide down.

With max_lr = 3, warmup 10, total 100: step 55 → progress = 45/90 = 0.5 → cos(π/2) = 0 → lr = 3 · ½ · 1 = **1.5**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `beta1, beta2, eps = 0.9, 0.999, 1e-8` | (given) | three names set in one line |
| `m[i] = …` | | changes the list **in place**: the caller sees the new values |
| `g * g` | | g squared |
| `beta1 ** t` | "beta one to the power t" | β₁ᵗ |
| `math.sqrt(v_hat)` | | √v̂ |
| `math.cos(x)`, `math.pi` | | cosine, and π |

### 👀 Worked example: a running average of temperatures

```python
avg = 0.0
for temp in [20, 20, 20]:
    avg = 0.9 * avg + 0.1 * temp
    print(round(avg, 2))       # 2.0, 3.8, 5.42: far too low at first
```

Divide by (1 − 0.9ᵗ): 2.0 / 0.1 = 20, 3.8 / 0.19 = 20, 5.42 / 0.271 = 20. The fix gives the right answer from the very first step. That's m̂.

## 🎯 Your quest

`adamw_step`: replace `pass` inside the given `for i` loop with (8 spaces):

1. `        g = grads[i]`
2. `        m[i] = beta1 * m[i] + (1 - beta1) * g`
3. `        v[i] = beta2 * v[i] + (1 - beta2) * g * g`
4. `        m_hat = m[i] / (1 - beta1 ** t)`
5. `        v_hat = v[i] / (1 - beta2 ** t)`
6. `        params[i] = params[i] - lr * wd * params[i] - lr * m_hat / (math.sqrt(v_hat) + eps)`

`lr_at`: replace `return max_lr` with:

1. `    if step < warmup:`
2. `        return max_lr * (step + 1) / warmup`
3. `    progress = (step - warmup) / (total - warmup)`
4. `    return max_lr * 0.5 * (1 + math.cos(math.pi * progress))`

AdamW should end with a much lower loss than SGD, and the schedule prints `[0.3, 1.5, 3.0, 3.0, 1.5, 0.0]`.

## Review

<details><summary>How do you spot overfitting?</summary>Training loss keeps falling while validation loss starts rising.</details>
<details><summary>What does early stopping keep?</summary>The checkpoint with the lowest validation loss.</details>
<details><summary>Why must validation data never leak into training?</summary>Then the validation score measures memorization instead of generalization and lies to you.</details>
