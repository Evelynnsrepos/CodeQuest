def scores(tp, fp, fn, tn):
    return (0, 0, 0)


def weights(h, w, k):
    return (0, 0)


def q_new(q, r, best_next, alpha, gamma):
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
