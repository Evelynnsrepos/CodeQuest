---
title: Temperature
xp: 25
---
# Sampling and temperature

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

## Your quest

`softmax` from two lessons ago is already written.

1. Write `softmax_t(logits, T)`: divide every logit by `T`, then return `softmax` of the result.
2. Set `code_temperature` to `"low"` or `"high"`: which would you use for generating code?

Run it and compare how much probability `" Paris"` gets at each temperature.

## Review

<details><summary>Name two ways generation stops.</summary>The model emits its end-of-sequence token, or the max-tokens limit is reached.</details>
<details><summary>What does the KV cache store and why does it cost VRAM?</summary>Intermediate results for every earlier token, so they don't have to be recomputed each step. It grows with every token in the context.</details>
<details><summary>What is greedy decoding?</summary>Always picking the single most likely next token.</details>
