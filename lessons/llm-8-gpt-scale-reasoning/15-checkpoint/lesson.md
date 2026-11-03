---
title: Checkpoint: from scratch to reasoning
xp: 100
---
# Explain the frontier

> **Warm-up:** describe, in a few sentences, how a model like DeepSeek-R1 goes from random weights to solving math step by step.

Your answer should have touched: an architecture (transformer blocks with attention, MLPs, residuals, norms, RoPE), pretraining on trillions of filtered tokens with a compute budget guided by scaling laws, spread over many GPUs, then SFT, then RL with verifiable rewards (GRPO), then evaluation with pass@k on uncontaminated benchmarks.

## Your quest

Fill `ANSWERS` with the best letter for each question.

1. Why does a pre-norm transformer still train with 80+ layers?
   a) Residual connections pass the gradient straight through, and norms keep the stream's scale stable  b) Deep models need no gradient  c) RoPE fixes vanishing gradients
2. You double the context length a RoPE model was trained on. What do methods like YaRN change?
   a) The vocabulary  b) The rotation frequencies θ, so new positions look like trained ones  c) The number of layers
3. Chinchilla-optimal training uses about how many tokens per parameter, and why are small models trained on far more?
   a) 1; to save data  b) 20; over-training makes a model that's cheaper to run at the same quality  c) 1000; it's required by law
4. With 64 GPUs, which ZeRO stage lets the largest model fit?
   a) Stage 1  b) Stage 2  c) Stage 3
5. Why does RLHF add a KL penalty to the reference model?
   a) To speed up sampling  b) To stop the policy drifting into text that exploits the reward model  c) To shrink the model
6. What does GRPO use instead of PPO's value model?
   a) The mean reward of a group of answers to the same prompt  b) A second reward model  c) Human ratings for every token
7. A model's first training loss on a 32,000-token vocabulary is 31.5. What's likely wrong?
   a) Nothing  b) The initialization (a uniform guess gives ln 32000 ≈ 10.4)  c) The learning-rate schedule
8. Why sample several answers and majority-vote?
   a) Wrong reasoning paths disagree with each other while correct ones tend to agree  b) It lowers the temperature  c) It removes the need for a tokenizer

## Review

<details><summary>Write the pass@k estimator.</summary>1 − C(n − c, k) / C(n, k).</details>
<details><summary>Training FLOPs for N parameters on D tokens?</summary>About 6·N·D.</details>
<details><summary>What does an induction head do?</summary>Copies patterns: after seeing "A B … A", it predicts "B".</details>

## What's next

Read the primary papers you now understand: *Attention Is All You Need* (2017), *Training Compute-Optimal Large Language Models* (Chinchilla, 2022), *Training language models to follow instructions with human feedback* (InstructGPT, 2022), *DeepSeekMath* (GRPO, 2024) and *DeepSeek-R1* (2025). Then build and train nanoGPT yourself, and try GRPO on a small model with Hugging Face TRL's `GRPOTrainer` on a rented GPU.
