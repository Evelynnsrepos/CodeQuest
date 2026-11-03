import math


def total_log_prob(probs):
    total = 0
    for p in probs:
        total += math.log(p)
    return total


def perplexity(probs):
    return math.exp(-total_log_prob(probs) / len(probs))


confident = [0.8, 0.8, 0.8, 0.8]
unsure = [0.25, 0.25, 0.25, 0.25]
print("confident:", round(perplexity(confident), 2))
print("unsure:", round(perplexity(unsure), 2))
