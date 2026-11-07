def scores(tp, fp, fn, tn):
    # accuracy = (tp + tn) / (tp + fp + fn + tn)
    # if tp + fp == 0:
    #     precision = 0.0
    # else:
    #     precision = tp / (tp + fp)
    # if tp + fn == 0:
    #     recall = 0.0
    # else:
    #     recall = tp / (tp + fn)
    # return (accuracy, precision, recall)
    return (0, 0, 0)


def weights(h, w, k):
    # dense = (h * w) ** 2
    # conv = k * k
    # return (dense, conv)
    return (0, 0)


def q_new(q, r, best_next, alpha, gamma):
    # return q + alpha * (r + gamma * best_next - q)
    return q


print(scores(2, 3, 98, 19897), weights(28, 28, 3), q_new(0, 1, 0, 0.5, 0.9))


ANSWERS = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
