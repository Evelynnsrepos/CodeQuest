import math
import random

TEXT = ("a language model reads tokens and predicts the next one. it learns by guessing, "
        "measuring how wrong it was, and nudging every weight a little. the loss goes down "
        "as the model gets better at guessing. after enough steps it can write text that "
        "looks a bit like the text it was trained on. small models make letter soup, big "
        "models make essays. the training loop is the same for both: forward, loss, "
        "backward, update, repeat. that is the whole secret of deep learning, the rest "
        "is data, compute and patience. ")


def softmax(row):
    m = max(row)
    e = [math.exp(x - m) for x in row]
    s = sum(e)
    return [x / s for x in e]


vocab = sorted(set(TEXT))
V = len(vocab)
stoi = {ch: i for i, ch in enumerate(vocab)}
pairs = [(stoi[a], stoi[b]) for a, b in zip(TEXT, TEXT[1:])]
cut = int(len(pairs) * 0.9)
train, val = pairs[:cut], pairs[cut:]
W = [[0.0] * V for _ in range(V)]


def loss_on(data):
    probs = [softmax(row) for row in W]
    return sum(-math.log(probs[a][b]) for a, b in data) / len(data)


val_loss_start = loss_on(val)
train_losses = []
for epoch in range(40):
    probs = [softmax(row) for row in W]
    grad = [[0.0] * V for _ in range(V)]
    loss = 0.0
    for a, b in train:
        loss -= math.log(probs[a][b])
        for j in range(V):
            grad[a][j] += probs[a][j]
        grad[a][b] -= 1
    train_losses.append(loss / len(train))
    for i in range(V):
        for j in range(V):
            W[i][j] -= 30 * grad[i][j] / len(train)
    if epoch % 5 == 0:
        print(f"epoch {epoch:2}: train loss {train_losses[-1]:.3f}")
val_loss_end = loss_on(val)
print(f"validation loss: {val_loss_start:.3f} → {val_loss_end:.3f}")


def generate(start, length, rng):
    i, out = stoi[start], ""
    for _ in range(length):
        i = rng.choices(range(V), weights=softmax(W[i]))[0]
        out += vocab[i]
    return out


print(generate("t", 60, random.Random(0)))
