import math


def best_checkpoint(history):
    evals = [h for h in history if "eval_loss" in h]
    return min(evals, key=lambda h: h["eval_loss"])["step"]


def diagnose(history):
    problems = []
    train = [h["loss"] for h in history if "loss" in h]
    evals = [h["eval_loss"] for h in history if "eval_loss" in h]
    if any(math.isnan(x) for x in train):
        problems.append("nan loss")
    if evals and evals[-1] > min(evals):
        problems.append("overfitting")
    if train and train[-1] < 0.05:
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
