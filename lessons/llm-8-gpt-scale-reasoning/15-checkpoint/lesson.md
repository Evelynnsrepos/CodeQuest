---
title: Checkpoint: from scratch to reasoning
xp: 120
---
# Explain the frontier

> **Warm-up:** describe, in a few sentences, how a model like DeepSeek-R1 goes from random weights to solving math step by step.

Your answer should have touched: an architecture (transformer blocks with attention, MLPs, residuals, norms, RoPE), pretraining on trillions of filtered tokens with a compute budget guided by scaling laws, spread over many GPUs, then SFT, then RL with verifiable rewards (GRPO), then evaluation with pass@k on uncontaminated benchmarks.

## Your quest

### Part 1: the numbers

1. `train_flops(n_params, tokens)`: about **6 · N · D** floating-point operations (lesson 08).
2. `chinchilla_tokens(n_params)`: the compute-optimal amount of data, about **20 tokens per parameter**.
3. `start_loss(vocab)`: the loss of a model that guesses uniformly: **ln(vocab)**. Then `init_ok(first_loss, vocab)`: `True` if the first loss is within 1.0 of that.
4. `advantages(rewards)`: GRPO's group advantages `(r − mean) / std` (std dividing by n). If every reward is the same, return all zeros (no signal).

### Part 2: why questions

Fill `ANSWERS` with the letter of the **best** answer. Every option sounds reasonable on purpose: think about *why* each wrong one is wrong.

1. Why does a pre-norm transformer still train with 80+ layers?
   - **a)** RoPE rotates the gradient so it can't vanish.
   - **b)** The residual stream gives the gradient a direct path around every block, and the norm inside each block keeps the scale of what's added stable.
   - **c)** Attention's softmax normalizes the gradients to 1 at every layer.
   - **d)** Dropout in each layer stops the gradients from shrinking.

2. You want to run a RoPE model at twice the context length it was trained on. What do methods like YaRN change?
   - **a)** They retrain the token embeddings for the new positions.
   - **b)** They add new learned position embeddings after position 4096.
   - **c)** They rescale RoPE's rotation frequencies so far-away positions produce angles the model already saw in training.
   - **d)** They double the number of attention heads.

3. Chinchilla says about 20 tokens per parameter is compute-optimal. Why are small open models trained on 100× that?
   - **a)** The Chinchilla result only holds for models above 70B.
   - **b)** More tokens per parameter makes training itself cheaper.
   - **c)** Small models can't learn from fewer tokens at all.
   - **d)** Over-training gives a better model for its size, and a smaller model is much cheaper to run for millions of users.

4. A model is too big for one GPU even with ZeRO stage 2. What does stage 3 add?
   - **a)** It shards the weights themselves across GPUs, not only the gradients and optimizer states.
   - **b)** It moves the activations to the CPU.
   - **c)** It switches all math to 8-bit.
   - **d)** It splits each layer's matrix multiply across GPUs (tensor parallelism).

5. Why does RLHF add a KL penalty toward the reference model?
   - **a)** To keep the policy's outputs short.
   - **b)** To stop the policy drifting into strange text that scores high on the reward model but isn't actually good (reward hacking).
   - **c)** Because PPO can't compute gradients without it.
   - **d)** To make the reward model's scores sum to 1.

6. A first training loss of 31.5 with a 32,000-token vocabulary. What's most likely wrong?
   - **a)** The learning rate is too low.
   - **b)** The batch is too small.
   - **c)** The initialization is too large: a model that guesses uniformly would start near ln 32000 ≈ 10.4.
   - **d)** Nothing: big vocabularies start with high losses.

## Review

<details><summary>Write the pass@k estimator.</summary>1 − C(n − c, k) / C(n, k).</details>
<details><summary>Training FLOPs for N parameters on D tokens?</summary>About 6·N·D.</details>
<details><summary>What does an induction head do?</summary>Copies patterns: after seeing "A B … A", it predicts "B".</details>

## What's next

Read the primary papers you now understand: *Attention Is All You Need* (2017), *Training Compute-Optimal Large Language Models* (Chinchilla, 2022), *Training language models to follow instructions with human feedback* (InstructGPT, 2022), *DeepSeekMath* (GRPO, 2024) and *DeepSeek-R1* (2025). Then build and train nanoGPT yourself, and try GRPO on a small model with Hugging Face TRL's `GRPOTrainer` on a rented GPU.
