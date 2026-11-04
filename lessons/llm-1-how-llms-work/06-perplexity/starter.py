import math


def total_log_prob(probs):
    return 0


def perplexity(probs):
    return 0


confident = [0.8, 0.8, 0.8, 0.8]
unsure = [0.25, 0.25, 0.25, 0.25]
print("confident:", round(perplexity(confident), 2))
print("unsure:", round(perplexity(unsure), 2))
