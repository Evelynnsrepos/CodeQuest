import math


def verify(text, truth):
    last = None
    for line in text.splitlines():
        if line.startswith("Answer:"):
            last = line
    if last is None:
        return 0.0
    if last[len("Answer:"):].strip() == truth:
        return 1.0
    return 0.0


def group_advantages(rewards, eps=1e-6):
    n = len(rewards)
    mean = sum(rewards) / n
    total = 0
    for r in rewards:
        total = total + (r - mean) ** 2
    std = math.sqrt(total / n)
    out = []
    for r in rewards:
        out.append((r - mean) / (std + eps))
    return out


group = [
    "12 * 3 = 36, plus 6 is 42.\nAnswer: 42",
    "I think it's 40.\nAnswer: 40",
    "Answer: 42",
    "The result is 42 but I won't format it.",
]
rewards = []
for g in group:
    rewards.append(verify(g, "42"))
print("rewards:", rewards)
print("advantages:", [round(a, 3) for a in group_advantages(rewards)])
