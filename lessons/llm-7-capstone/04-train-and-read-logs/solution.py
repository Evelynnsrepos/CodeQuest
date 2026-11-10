import math


def best_checkpoint(history):
    best_step = None
    best_loss = None
    for h in history:
        if "eval_loss" in h:
            if best_loss is None or h["eval_loss"] < best_loss:
                best_loss = h["eval_loss"]
                best_step = h["step"]
    return best_step


def diagnose(history):
    problems = []
    train = []
    evals = []
    for h in history:
        if "loss" in h:
            train.append(h["loss"])
        if "eval_loss" in h:
            evals.append(h["eval_loss"])
    has_nan = False
    for x in train:
        if math.isnan(x):
            has_nan = True
    if has_nan:
        problems.append("nan loss")
    if len(evals) > 0 and evals[-1] > min(evals):
        problems.append("overfitting")
    if len(train) > 0 and train[-1] < 0.05:
        problems.append("memorizing")
    return problems


history = [
    {"step": 10, "loss": 1.92, "grad_norm": 1.1}, {"step": 20, "loss": 1.51, "grad_norm": 0.8},
    {"step": 20, "eval_loss": 1.60},
    {"step": 30, "loss": 1.22, "grad_norm": 0.7}, {"step": 40, "loss": 0.98, "grad_norm": 0.6},
    {"step": 40, "eval_loss": 1.41},
    {"step": 50, "loss": 0.71, "grad_norm": 0.6}, {"step": 60, "loss": 0.44, "grad_norm": 0.5},
    {"step": 60, "eval_loss": 1.47},
]
print("best checkpoint: step", best_checkpoint(history))
print("problems:", diagnose(history))
