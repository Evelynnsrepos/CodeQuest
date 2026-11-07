import math


def entropy(p):
    # total = 0
    # for pi in p:
    #     if pi > 0:
    #         total = total + pi * math.log(pi)
    # return -total
    return 0


def cross_entropy(p, q):
    # total = 0
    # for i in range(len(p)):
    #     if p[i] > 0:
    #         total = total + p[i] * math.log(q[i])
    # return -total
    return 0


def kl(p, q):
    # return cross_entropy(p, q) - entropy(p)
    return 0


coin = [0.5, 0.5]
loaded = [0.9, 0.1]
print("entropy of a fair coin:", round(entropy(coin) / math.log(2), 3), "bits")
print("entropy of a loaded coin:", round(entropy(loaded) / math.log(2), 3), "bits")
truth = [0, 1, 0]          # the real next token is token 1
model = [0.2, 0.7, 0.1]
print("LLM loss for this position:", round(cross_entropy(truth, model), 4), "= -log 0.7 =", round(-math.log(0.7), 4))
print("KL(coin || loaded):", round(kl(coin, loaded), 4), " KL(loaded || coin):", round(kl(loaded, coin), 4))
