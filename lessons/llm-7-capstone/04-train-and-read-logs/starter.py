import math


def best_checkpoint(history):
    return None


def diagnose(history):
    problems = []
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
