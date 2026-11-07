---
title: Temperature
minutes: 30
xp: 25
hint: Inside softmax_t, after scaled = []: for z in logits: and inside it scaled.append(z / T)
hint: Change the last line to: return softmax(scaled) (not logits!)
hint: Code needs the most likely, most exact tokens: code_temperature = "low"
---
# Sampling and temperature

⏱️ About 30 minutes

> **Warm-up:** if you ask the same question twice in LM Studio, you often get two different answers. Where does the randomness come from, if the weights never change?

The model's output is deterministic: same tokens in, same probabilities out. The randomness comes from the **sampler**, the step that picks the next token. Instead of always taking the top token (greedy), it usually draws one at random, weighted by the probabilities. A token with 0.7 probability is picked 70% of the time.

**Temperature** reshapes the distribution *before* the draw. You divide every logit by `T`, then apply softmax:

```
probabilities = softmax(logits / T)
```

| T | Effect |
|---|---|
| close to 0 | The gap between logits is blown up. The top token gets almost all the probability: nearly greedy. |
| 1 | The model's own distribution, unchanged. |
| above 1 | Gaps shrink, the distribution flattens, unlikely tokens get picked more often: "creative", then incoherent. |

Runners treat `T = 0` as plain greedy decoding (you can't divide by zero).

In LM Studio you find **Temperature** in the model settings sidebar of a chat. Typical values: 0 to 0.3 for code, facts and tool calling, 0.7 to 1.0 for chat and creative writing. Model cards often recommend a value; follow it unless you have a reason not to.

<div class="quiz" data-answer="0" data-why="Divide every logit by T: 2 ÷ 2 = 1 and 1 ÷ 2 = 0.5. The gap shrinks, so the choice gets more random."><p><b>Predict first:</b> with T = 2, what do the logits 2 and 1 become before the softmax?</p><button>1 and 0.5</button><button>4 and 2</button><button>2 and 1</button></div>

<div class="explore" data-widget="temperature"></div>

## 🔬 Take the formula apart

<div class="formula">probabilities = softmax(<span class="k1">logits</span> <span class="k2">/ T</span>)</div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">logits</span> | | the model's raw scores, one per token |
| <span class="k2">/ T</span> | "divided by T" | divide **every** logit by the same number T, the temperature |
| softmax(…) | | lesson 5: turn scores into probabilities that add up to 1 |

Why does dividing change anything? Softmax only cares about the **gaps** between logits. Take two logits, 2 and 1 (a gap of 1):

| T | logits after ÷ T | gap | softmax |
|---|---|---|---|
| 0.5 | 4 and 2 | 2 | 0.88 and 0.12: sharper, the top token wins more often |
| 1 | 2 and 1 | 1 | 0.73 and 0.27: unchanged |
| 2 | 1 and 0.5 | 0.5 | 0.62 and 0.38: flatter, more random |

Dividing by a number **below 1** makes the numbers bigger and the gap wider. Dividing by a number **above 1** shrinks them and the gap.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `scaled = []` | | a new, empty list |
| `for z in logits:` | "for each z in logits" | once per logit |
| `scaled.append(z / T)` | | the logit divided by T, added to the new list |
| `softmax(scaled)` | | calls the given softmax with your new list |
| `"low"` | "the text low" | text goes in quotes |

### 👀 Worked example: halve every price

```python
def halve_all(prices):
    halved = []
    for p in prices:
        halved.append(p / 2)
    return halved

print(halve_all([10, 4]))   # [5.0, 2.0]
```

1. 10 / 2 = 5.0 goes in. 2. 4 / 2 = 2.0 goes in. 3. Returns the new list. The old list is untouched.

`softmax_t` is this with `/ T` instead of `/ 2`, and then softmax on the new list.

## 🎯 Your quest

`softmax` is already written.

1. In `softmax_t`, replace the comment line with:
   - `for z in logits:`
   - `    scaled.append(z / T)`
2. Change the last line to `return softmax(scaled)`. The starter gives the **old** list to softmax, so nothing changes yet.
3. Set `code_temperature` to `"low"` or `"high"`: which would you use for generating code?

Run it and compare how much probability `" Paris"` gets at each temperature.

## Review

<details><summary>Name two ways generation stops.</summary>The model emits its end-of-sequence token, or the max-tokens limit is reached.</details>
<details><summary>What does the KV cache store and why does it cost VRAM?</summary>Intermediate results for every earlier token, so they don't have to be recomputed each step. It grows with every token in the context.</details>
<details><summary>What is greedy decoding?</summary>Always picking the single most likely next token.</details>
<details><summary>Logits 4 and 2 at T = 2: what goes into softmax?</summary>2 and 1. The gap shrinks from 2 to 1, so the result is flatter.</details>
