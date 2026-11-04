def scores(tp, fp, fn, tn):
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return (accuracy, precision, recall)


def weights(h, w, k):
    return ((h * w) ** 2, k * k)


def q_new(q, r, best_next, alpha, gamma):
    return q + alpha * (r + gamma * best_next - q)


print(scores(2, 3, 98, 19897), weights(28, 28, 3), q_new(0, 1, 0, 0.5, 0.9))


ANSWERS = {
    1: "b",
    2: "c",
    3: "a",
    4: "d",
    5: "b",
    6: "a",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
