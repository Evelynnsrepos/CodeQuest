import math


def verify(text, truth):
    answers = [line for line in text.splitlines() if line.startswith("Answer:")]
    if not answers:
        return 0.0
    return 1.0 if answers[-1][len("Answer:"):].strip() == truth else 0.0


def group_advantages(rewards, eps=1e-6):
    n = len(rewards)
    mean = sum(rewards) / n
    std = math.sqrt(sum((r - mean) ** 2 for r in rewards) / n)
    return [(r - mean) / (std + eps) for r in rewards]


group = [
    "12 * 3 = 36, plus 6 is 42.\nAnswer: 42",
    "I think it's 40.\nAnswer: 40",
    "Answer: 42",
    "The result is 42 but I won't format it.",
]
rewards = [verify(g, "42") for g in group]
print("rewards:", rewards)
print("advantages:", [round(a, 3) for a in group_advantages(rewards)])
