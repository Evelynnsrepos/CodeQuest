---
title: Run the training and read its logs
xp: 50
---
# Training is the easy part; reading it is the skill

> **Warm-up:** your run finished. Which numbers would tell you it went well, and which would tell you it went wrong?

**On your machine (or a rented GPU):** take the TRL script from LLMs 6 lesson 8 or an Unsloth notebook for your base model, point it at your `train.jsonl` / `val.jsonl`, and set:

- `eval_strategy="steps"` with `eval_steps` so you get a validation loss every few dozen steps,
- `save_strategy="steps"` (same interval) so there's a checkpoint for each evaluation,
- `load_best_model_at_end=True`, `metric_for_best_model="eval_loss"` for early stopping,
- `logging_steps` small (5–10) so you see the curve.

First do a **smoke test**: 10 steps on 20 examples. It catches broken data, wrong templates and out-of-memory in minutes, not hours.

The Hugging Face Trainer writes every logged value to `trainer_state.json` under `"log_history"`, a list of dictionaries:

```json
{"step": 10, "loss": 1.82, "grad_norm": 0.91, "learning_rate": 0.0002, "epoch": 0.4}
{"step": 20, "eval_loss": 1.64, "epoch": 0.8}
```

What to look for:

| Signal | Meaning |
|---|---|
| `loss` falls, then flattens | normal |
| `eval_loss` falls, then rises | overfitting from that point (LLMs 5, lesson 8): use the best checkpoint |
| `loss` → near 0 | memorizing |
| `loss` is `nan` or explodes | learning rate too high, bad data, or precision problem |
| `grad_norm` spikes far above its usual level | unstable step; often a bad example or too-high LR |

## Your quest

`history` is a list like the one above (training entries have `"loss"`, evaluation entries have `"eval_loss"`).

1. `best_checkpoint(history)`: the `step` of the entry with the lowest `eval_loss`.
2. `diagnose(history)`: a list of problems, in this order:
   - `"nan loss"` if any training loss is not a number (`math.isnan`)
   - `"overfitting"` if the **last** `eval_loss` is higher than the lowest one
   - `"memorizing"` if the last training loss is below `0.05`

## Review

<details><summary>Why round max_seq_length up to at least the longest example?</summary>Longer examples get cut at the end, which removes the answer the model should learn.</details>
<details><summary>Roughly how many characters per token in English?</summary>About 4.</details>
