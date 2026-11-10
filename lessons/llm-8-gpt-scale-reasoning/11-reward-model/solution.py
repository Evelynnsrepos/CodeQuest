import math


def reward(w, features):
    total = 0
    for i in range(len(w)):
        total = total + w[i] * features[i]
    return total


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def pair_loss(r_chosen, r_rejected):
    diff = r_chosen - r_rejected
    if diff >= 0:
        return math.log1p(math.exp(-diff))
    return -diff + math.log1p(math.exp(diff))


def train_reward(pairs, lr, epochs):
    w = [0.0] * len(pairs[0][0])
    for epoch in range(epochs):
        for c, r in pairs:
            diff = reward(w, c) - reward(w, r)
            scale = -(1 - sigmoid(diff))
            for i in range(len(w)):
                w[i] = w[i] - lr * scale * (c[i] - r[i])
    return w


# features: [is_correct, is_polite, length_in_100_words]
pairs = [([1, 1, 1], [0, 1, 1]), ([1, 0, 2], [0, 0, 2]), ([1, 1, 1], [1, 0, 1]), ([0, 1, 1], [0, 0, 3])]
w = train_reward(pairs, lr=0.5, epochs=200)
print("weights:", [round(x, 2) for x in w])
print("mean loss:", round(sum(pair_loss(reward(w, c), reward(w, r)) for c, r in pairs) / len(pairs), 4))
