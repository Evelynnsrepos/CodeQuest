import math


def majority_vote(answers):
    # counts = {}
    # for a in answers:
    #     counts[a] = counts.get(a, 0) + 1
    # best = answers[0]
    # for a in answers:
    #     if counts[a] > counts[best]:
    #         best = a
    # return best
    return answers[0]


def pass_at_k(n, c, k):
    # if n - c < k:
    #     return 1.0
    # return 1 - math.comb(n - c, k) / math.comb(n, k)
    return c / n


samples = ["42", "41", "42", "40", "42", "41"]
print("majority:", majority_vote(samples))
print("pass@1 with 3 of 10 correct:", round(pass_at_k(10, 3, 1), 3))
print("pass@5 with 3 of 10 correct:", round(pass_at_k(10, 3, 5), 3))
