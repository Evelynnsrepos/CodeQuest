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
    e = []
    for x in row:
        e.append(math.exp(x - m))
    s = sum(e)
    out = []
    for x in e:
        out.append(x / s)
    return out


vocab = []
train_losses = []
val_loss_start = None
val_loss_end = None

# Part 1: data
# vocab = sorted(set(TEXT))
# V = len(vocab)
# stoi = {}
# for i in range(V):
#     stoi[vocab[i]] = i
# pairs = []
# for i in range(len(TEXT) - 1):
#     pairs.append((stoi[TEXT[i]], stoi[TEXT[i + 1]]))
# cut = int(len(pairs) * 0.9)
# train = pairs[:cut]
# val = pairs[cut:]
# W = []
# for i in range(V):
#     W.append([0.0] * V)


# def loss_on(data):
#     probs = []
#     for row in W:
#         probs.append(softmax(row))
#     total = 0.0
#     for a, b in data:
#         total = total - math.log(probs[a][b])
#     return total / len(data)


# Part 2: training
# val_loss_start = loss_on(val)
# for epoch in range(40):
#     probs = []
#     for row in W:
#         probs.append(softmax(row))
#     grad = []
#     for i in range(V):
#         grad.append([0.0] * V)
#     loss = 0.0
#     for a, b in train:
#         loss = loss - math.log(probs[a][b])
#         for j in range(V):
#             grad[a][j] = grad[a][j] + probs[a][j]
#         grad[a][b] = grad[a][b] - 1
#     train_losses.append(loss / len(train))
#     for i in range(V):
#         for j in range(V):
#             W[i][j] = W[i][j] - 30 * grad[i][j] / len(train)
#     if epoch % 5 == 0:
#         print("epoch", epoch, "train loss", round(train_losses[-1], 3))
# val_loss_end = loss_on(val)
# print("validation loss:", round(val_loss_start, 3), "->", round(val_loss_end, 3))


# Part 3: generate
def generate(start, length, rng):
    # i = stoi[start]
    # out = ""
    # for step in range(length):
    #     i = rng.choices(range(V), weights=softmax(W[i]))[0]
    #     out = out + vocab[i]
    # return out
    return ""


print(generate("t", 60, random.Random(0)))
