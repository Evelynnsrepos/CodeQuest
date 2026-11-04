---
title: Final checkpoint, explain every why
xp: 120
---
# The whole pipeline, and why each step is there

> **Warm-up:** without looking back, say out loud the steps from "I have an idea" to "it runs in LM Studio with a tool".

Your plan's last checkpoint: *can you explain why you made each choice, and can you do the numbers behind it?* Knowing **why** is the difference between following a tutorial and understanding the field.

**On your machine:** the real checkpoint is your repo. It should contain your plan (lesson 1), data scripts (2–3), training config and logs (4), evaluation results (5–6) and the model card (7). If you can explain every file in it to someone else, you've finished.

## Your quest

### Part 1: the numbers

1. `fits(params_b, bits, vram_gb, overhead_gb=1.5)`: `True` if the weights (`params_b` billion parameters × `bits` / 8 bytes, in GB) plus `overhead_gb` fit in `vram_gb`. An 8B model at 16 bits needs 16 + 1.5 GB; at Q4_K_M (about 4.5 bits per weight) it needs 4.5 + 1.5.
2. `full_ft_gb(params_b)`: memory for **full** fine-tuning with Adam, at 16 bytes per parameter (weights, gradients, two Adam states, a float32 master copy). 8B → 128 GB.
3. `best_step(log)`: `log` is a list of `(step, eval_loss)`. Return the step with the **lowest** eval_loss (the checkpoint you keep).
4. `win_interval(wins, n)`: the 95% interval `(low, high)` of a blind-eval win rate, `p ± 1.96·√(p(1−p)/n)` (Math 4, lesson 11). Then `clear_win(wins, n)`: `True` only if `low > 0.5`.

### Part 2: why questions

Fill `ANSWERS` with the letter of the **best** answer. Every option sounds reasonable on purpose: think about *why* each wrong one is wrong.

1. You picked the learning rate and the checkpoint by watching validation scores. Why do you still need a separate test split you never looked at?
   - **a)** Validation loss is computed with dropout on, so it reads too high.
   - **b)** Every choice you made by looking at validation results bent the model toward that data, so its score is too optimistic; only untouched data gives an honest number.
   - **c)** The test split has to come from a different source than the training data.
   - **d)** Evaluating on validation data during training leaks its gradients into the weights.

2. Why are the prompt (user) tokens masked out of the loss in SFT?
   - **a)** Masked tokens skip the forward pass, which halves training time.
   - **b)** Prompts are noisy, and including them makes the loss diverge.
   - **c)** The gradient should reward writing good answers; learning to predict the user's questions spends capacity on the wrong job and can make the model talk like a user.
   - **d)** The tokenizer can't place special tokens in masked positions.

3. eval_loss falls until step 600, then rises, while train loss keeps falling. What do you do?
   - **a)** Raise the learning rate to jump out of the bump.
   - **b)** Keep training: eval loss always comes back down later.
   - **c)** Lower the batch size so each step sees fewer examples.
   - **d)** Keep the step-600 checkpoint: after it the model starts memorizing the training set (overfitting).

4. In the blind A/B evaluation, why shuffle which side your model's answer appears on?
   - **a)** Judges, people and LLMs alike, tend to prefer one position (often the first); a fixed order adds a bias that looks like a win.
   - **b)** So the judge can't read the model's name in the answer.
   - **c)** To average out the sampling temperature.
   - **d)** Pairwise comparisons need an even number of samples on each side.

5. Goal: answer questions about your 300 notes, which change every week. Best first approach?
   - **a)** Full fine-tune on the notes.
   - **b)** QLoRA on the notes, retrained every week.
   - **c)** RAG over the notes; fine-tune later only if the style or format is still wrong.
   - **d)** Paste all 300 notes into every prompt.

6. After fine-tuning, tool-call success dropped from 92% to 70%. Most likely cause and fix?
   - **a)** The LoRA rank was too high; lower it to 4.
   - **b)** Catastrophic forgetting: training only on chat answers moved the model away from the tool-call format. Mix tool-call examples into the training data.
   - **c)** The MCP server cached old answers; restart it.
   - **d)** 4-bit quantization always removes tool calling; use FP16.

## Review

<details><summary>What's the formula for the 95% confidence interval of a win rate p over n prompts?</summary>p ± 1.96 × sqrt(p(1−p)/n)</details>
<details><summary>Name the six sections of a model card.</summary>Base model, training data, training, evaluation, limitations, how to run.</details>
<details><summary>What does backpropagation compute, in one sentence?</summary>The gradient of the loss with respect to every weight, by applying the chain rule backward through the computation graph.</details>

## What's next

You've done the whole path: how LLMs work, running them, tools, the math, training from scratch, training options and one real project. Good next steps: Andrej Karpathy's "Let's build GPT" and nanoGPT, the Hugging Face LLM course, and reading new papers on arXiv (start with the abstract and figures). Pick a second project with a different goal (for example DPO on your own preferences) and repeat the pipeline.
