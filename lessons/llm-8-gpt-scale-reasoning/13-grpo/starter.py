import math


def verify(text, truth):
    return 0.0


def group_advantages(rewards, eps=1e-6):
    return [0.0] * len(rewards)


group = [
    "12 * 3 = 36, plus 6 is 42.\nAnswer: 42",
    "I think it's 40.\nAnswer: 40",
    "Answer: 42",
    "The result is 42 but I won't format it.",
]
rewards = [verify(g, "42") for g in group]
print("rewards:", rewards)
print("advantages:", [round(a, 3) for a in group_advantages(rewards)])
