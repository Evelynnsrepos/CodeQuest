import math


def reward(w, features):
    return sum(a * b for a, b in zip(w, features))


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def pair_loss(r_chosen, r_rejected):
    return 0.0


def train_reward(pairs, lr, epochs):
    return [0.0] * len(pairs[0][0])


# features: [is_correct, is_polite, length_in_100_words]
pairs = [([1, 1, 1], [0, 1, 1]), ([1, 0, 2], [0, 0, 2]), ([1, 1, 1], [1, 0, 1]), ([0, 1, 1], [0, 0, 3])]
w = train_reward(pairs, lr=0.5, epochs=200)
print("weights:", [round(x, 2) for x in w])
print("mean loss:", round(sum(pair_loss(reward(w, c), reward(w, r)) for c, r in pairs) / len(pairs), 4))
