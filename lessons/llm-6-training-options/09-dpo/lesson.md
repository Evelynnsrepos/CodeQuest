---
title: Preference tuning, RLHF and DPO
minutes: 50
xp: 55
hint: implicit_reward: return beta * (logp_policy - logp_ref)
hint: dpo_loss: chosen = implicit_reward(pc, rc, beta), rejected = implicit_reward(pr, rr, beta), margin = chosen - rejected
hint: dpo_loss ends: return math.log(1 + math.exp(-margin))
hint: reward_accuracy: wins = 0, for pc, pr, rc, rr in batch: if implicit_reward(pc, rc, beta) > implicit_reward(pr, rr, beta): wins = wins + 1. Then return wins / len(batch)
---
# Teaching "better", not just "correct"

⏱️ About 50 minutes

> **Warm-up:** for "write a friendly reply to this email" there's no single correct answer to imitate, but you can easily say which of two drafts is better. How could a model learn from that?

From **preferences**. A preference dataset holds a prompt with a **chosen** and a **rejected** answer:

```json
{"prompt": "Explain LoRA in one sentence.",
 "chosen": "LoRA freezes the model and trains two small matrices whose product is added to each weight.",
 "rejected": "LoRA is a thing for AI that makes it better at stuff."}
```

**RLHF** (as used for the original ChatGPT): train a separate **reward model** to score answers like humans would, then optimize the LLM with reinforcement learning (**PPO**) to get high reward, with a **KL penalty** (LLMs 4, lesson 10) keeping it close to the original so it doesn't drift into gibberish that fools the reward model. Powerful, but with PPO that is **four** models in memory (the policy being trained, a frozen reference copy for the KL penalty, the reward model, and a value model; see LLMs 8 lesson 12) and notoriously finicky.

**DPO** (Direct Preference Optimization, Rafailov et al., 2023) showed the same objective can be optimized **directly** with a simple classification-style loss, no reward model, no RL. It needs the model being trained (`π`) and a frozen copy of where it started (`π_ref`, usually the SFT model). Using each answer's total log-probability (LLMs 1, lesson 6):

```
margin = β · [ (log π(chosen) − log π_ref(chosen)) − (log π(rejected) − log π_ref(rejected)) ]
loss   = −log σ(margin)
```

In words: raise the chosen answer's probability *relative to where it started*, lower the rejected one's, and `β` (typically 0.1) controls how far it may move from the reference. Each bracket, times β, is the answer's **implicit reward**; "reward accuracy" is how often the chosen answer's implicit reward is higher.

DPO runs as a normal fine-tune, so it works with (Q)LoRA on your card (with LoRA, the reference is just the model with the adapter switched off: no second copy needed). TRL's `DPOTrainer` implements it. Related methods you'll see: **ORPO**, **KTO**, **SimPO**, and **GRPO** (RL with groups of sampled answers, used for reasoning models like DeepSeek-R1).

## 🔬 Take the formulas apart

**The letters.** `π` ("pi", here **not** 3.14) is the model being trained. `π_ref` is the frozen copy. `log π(chosen)` is the model's log-probability of the whole chosen answer: a negative number, closer to 0 = more likely. `β` ("beta") is a setting, 0.1.

**Implicit reward** <div class="formula">reward = <span class="k1">β</span> · (<span class="k2">log π(answer)</span> − <span class="k3">log π_ref(answer)</span>)</div>
"How much more likely is this answer **now** than at the start?" Positive = got likelier.

**Margin** <div class="formula">margin = <span class="k1">reward(chosen)</span> − <span class="k2">reward(rejected)</span></div>
Big positive margin = the model moved the right way.

**Loss** <div class="formula">loss = −log σ(margin) = log(1 + e<sup>−margin</sup>)</div>
σ is the sigmoid from LLMs 4 lesson 8. The two forms are equal; the right one is safer to compute. Margin 0 → log(1 + 1) = log 2 ≈ 0.693. Big margin → e^(−margin) ≈ 0 → loss ≈ log 1 = 0.

**Numbers**, β = 0.1, `later = (−38, −47, −42, −40)` meaning (policy chosen, policy rejected, ref chosen, ref rejected):
1. reward(chosen) = 0.1 × (−38 − (−42)) = 0.1 × 4 = **0.4**
2. reward(rejected) = 0.1 × (−47 − (−40)) = 0.1 × (−7) = **−0.7**
3. margin = 0.4 − (−0.7) = **1.1**
4. loss = log(1 + e⁻¹·¹) = log(1 + 0.333) ≈ **0.287**. Lower than 0.693: it learned.

Watch the minus signs: −38 − (−42) = −38 + 42 = 4.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `beta * (a - b)` | | the brackets subtract first |
| `math.exp(-margin)` | "e to the minus margin" | e<sup>−margin</sup> |
| `math.log(...)` | | natural log |
| `for pc, pr, rc, rr in batch:` | | each example is four numbers; this names them |
| `dpo_loss(*start, 0.1)` | (given) | the `*` unpacks the four numbers of `start` as four inputs |

### 👀 Worked example: the start

`start = (−42, −40, −42, −40)`: policy and reference are the same.
1. reward(chosen) = 0.1 × (−42 + 42) = 0. reward(rejected) = 0.1 × (−40 + 40) = 0.
2. margin = 0, loss = log 2 ≈ 0.693.
3. For reward accuracy, 0 > 0 is **false**: it doesn't count as a win. Of the three test examples only `later` wins → 1/3.

## 🎯 Your quest

`implicit_reward`: replace `return 0` with `    return beta * (logp_policy - logp_ref)`

`dpo_loss(pc, pr, rc, rr, beta)`: replace `return 0` with:

1. `    chosen = implicit_reward(pc, rc, beta)`
2. `    rejected = implicit_reward(pr, rr, beta)`
3. `    margin = chosen - rejected`
4. `    return math.log(1 + math.exp(-margin))`

`reward_accuracy(batch, beta)`: replace `return 0` with:

1. `    wins = 0`
2. `    for pc, pr, rc, rr in batch:`
3. `        if implicit_reward(pc, rc, beta) > implicit_reward(pr, rr, beta):`
4. `            wins = wins + 1`
5. `    return wins / len(batch)`

## Review

<details><summary>What does LoRA's lora_alpha do?</summary>Scales the update by alpha / r, so the rank can change without retuning the learning rate.</details>
<details><summary>What do the libraries peft, trl and bitsandbytes do?</summary>peft: LoRA adapters. trl: SFT/DPO trainers. bitsandbytes: 4-/8-bit quantization for QLoRA.</details>
