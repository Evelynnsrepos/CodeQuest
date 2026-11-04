---
title: Preference tuning, RLHF and DPO
xp: 55
---
# Teaching "better", not just "correct"

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

## Python you need

`σ(x) = 1 / (1 + e⁻ˣ)`. For numerical safety, `−log σ(x)` can be written as `softplus(−x) = log(1 + e⁻ˣ)`.

## Your quest

1. `implicit_reward(logp_policy, logp_ref, beta)`: `beta · (logp_policy − logp_ref)`.
2. `dpo_loss(pc, pr, rc, rr, beta)`: policy chosen/rejected and reference chosen/rejected log-probs → the DPO loss.
3. `reward_accuracy(batch, beta)`: the share of examples in the batch (tuples `(pc, pr, rc, rr)`) where the chosen implicit reward beats the rejected one.

## Review

<details><summary>What does LoRA's lora_alpha do?</summary>Scales the update by alpha / r, so the rank can change without retuning the learning rate.</details>
<details><summary>What do the libraries peft, trl and bitsandbytes do?</summary>peft: LoRA adapters. trl: SFT/DPO trainers. bitsandbytes: 4-/8-bit quantization for QLoRA.</details>
