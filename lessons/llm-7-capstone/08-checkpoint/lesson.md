---
title: Final checkpoint, explain every why
xp: 100
---
# The whole pipeline, and why each step is there

> **Warm-up:** without looking back, say out loud the steps from "I have an idea" to "it runs in LM Studio with a tool".

Your plan's last checkpoint: *can you explain why you made each choice?* Knowing **why** is the difference between following a tutorial and understanding the field. This quiz covers all seven courses; each question asks for the reason behind a step.

**On your machine:** the real checkpoint is your repo. It should contain your plan (lesson 1), data scripts (2–3), training config and logs (4), evaluation results (5–6) and the model card (7). If you can explain every file in it to someone else, you've finished.

## Your quest

Fill `ANSWERS` with the letter of the best answer to each question.

1. Why quantize to Q4_K_M instead of running FP16 on a 12 GB GPU?
   a) It makes the model smarter  b) An 8B model in FP16 (~16 GB) doesn't fit; Q4_K_M (~5 GB) does with little quality loss  c) GGUF can't store FP16
2. Why QLoRA rather than full fine-tuning?
   a) Full fine-tuning of an 8B model needs ~16 bytes per parameter (weights, gradients, Adam states), far beyond 12 GB; QLoRA trains small adapters on a 4-bit frozen base  b) QLoRA always gives better quality  c) Full fine-tuning doesn't work on Linux
3. Why hold out a test split you never look at during training?
   a) To make training faster  b) Training and validation data have influenced your choices, so only unseen data gives an honest score  c) Hugging Face requires it
4. Why mask the prompt tokens out of the loss?
   a) So the model learns to produce answers instead of learning to predict the user's questions  b) To save disk space  c) Because tokenizers can't handle prompts
5. Why keep the checkpoint with the lowest eval_loss instead of the last one?
   a) The last one is always corrupted  b) After that point the model starts overfitting the training data  c) Lower eval_loss means a smaller file
6. Why randomize A and B in the blind evaluation?
   a) Judges (human or LLM) are biased toward position and toward answers they know are "theirs"  b) To make the answers shorter  c) It's required by the license
7. Why try RAG before fine-tuning when the goal is "know my documents"?
   a) RAG retrieves current facts at question time and is cheap to update; fine-tuning is better at style and format than at adding facts  b) Fine-tuning can't run on AMD  c) RAG makes the model smaller
8. Why re-test tool calling after fine-tuning?
   a) Training on one kind of output can make the model forget others (catastrophic forgetting)  b) GGUF conversion deletes tools  c) MCP servers expire

## Review

<details><summary>What's the formula for the 95% confidence interval of a win rate p over n prompts?</summary>p ± 1.96 × sqrt(p(1−p)/n)</details>
<details><summary>Name the six sections of a model card.</summary>Base model, training data, training, evaluation, limitations, how to run.</details>
<details><summary>What does backpropagation compute, in one sentence?</summary>The gradient of the loss with respect to every weight, by applying the chain rule backward through the computation graph.</details>

## What's next

You've done the whole path: how LLMs work, running them, tools, the math, training from scratch, training options and one real project. Good next steps: Andrej Karpathy's "Let's build GPT" and nanoGPT, the Hugging Face LLM course, and reading new papers on arXiv (start with the abstract and figures). Pick a second project with a different goal (for example DPO on your own preferences) and repeat the pipeline.
