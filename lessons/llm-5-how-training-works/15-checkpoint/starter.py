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


vocab = []
train_losses = []
val_loss_start = None
val_loss_end = None


def generate(start, length, rng):
    return ""


print(generate("t", 60, random.Random(0)))
