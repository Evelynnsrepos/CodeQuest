---
title: Run the training and read its logs
minutes: 40
xp: 50
hint: best_checkpoint: best_step = None, best_loss = None, then for h in history: if "eval_loss" in h: and the best-so-far check
hint: The best-so-far check: if best_loss is None or h["eval_loss"] < best_loss: best_loss = h["eval_loss"] and best_step = h["step"]
hint: diagnose: first collect two lists, train (every h["loss"]) and evals (every h["eval_loss"])
hint: Then three ifs in order: any math.isnan(x) → "nan loss"; evals[-1] > min(evals) → "overfitting"; train[-1] < 0.05 → "memorizing"
---
# Training is the easy part; reading it is the skill

⏱️ About 40 minutes

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

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `"eval_loss" in h` | | true if the dictionary has that key |
| `best_loss is None or h["eval_loss"] < best_loss` | | the first one always wins; after that only a lower one |
| `math.isnan(x)` | "is not a number" | true for `nan`, the value a broken training produces |
| `has_nan = False` … `has_nan = True` | | a **flag**: starts False, flips to True if any is found |
| `min(evals)` | | the lowest eval loss |
| `evals[-1]`, `train[-1]` | | the last one |
| `len(evals) > 0 and …` | | only check when the list isn't empty |

### 👀 Worked example: reading the log

Eval losses: step 20 → 1.60, step 40 → 1.41, step 60 → 1.47.

1. Best: 1.60 first, then 1.41 is lower → best step 40. 1.47 isn't lower → stays **40**.
2. Last eval 1.47 > lowest 1.41 → **"overfitting"**.
3. Last train loss 0.44 is not < 0.05 → not memorizing. No nan.

## 🎯 Your quest

`best_checkpoint(history)`: replace `return None` with:

1. `    best_step = None`
2. `    best_loss = None`
3. `    for h in history:`
4. `        if "eval_loss" in h:`
5. `            if best_loss is None or h["eval_loss"] < best_loss:`
6. `                best_loss = h["eval_loss"]`
7. `                best_step = h["step"]`
8. `    return best_step`

`diagnose(history)`: between `problems = []` and `return problems`, add:

1. `    train = []`
2. `    evals = []`
3. `    for h in history:`
4. `        if "loss" in h:`
5. `            train.append(h["loss"])`
6. `        if "eval_loss" in h:`
7. `            evals.append(h["eval_loss"])`
8. `    has_nan = False`
9. `    for x in train:`
10. `        if math.isnan(x):`
11. `            has_nan = True`
12. `    if has_nan:`
13. `        problems.append("nan loss")`
14. `    if len(evals) > 0 and evals[-1] > min(evals):`
15. `        problems.append("overfitting")`
16. `    if len(train) > 0 and train[-1] < 0.05:`
17. `        problems.append("memorizing")`

## Review

<details><summary>Why round max_seq_length up to at least the longest example?</summary>Longer examples get cut at the end, which removes the answer the model should learn.</details>
<details><summary>Roughly how many characters per token in English?</summary>About 4.</details>
