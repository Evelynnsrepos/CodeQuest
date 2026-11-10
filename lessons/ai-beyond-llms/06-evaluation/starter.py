def counts(y_true, y_pred):
    # tp = 0
    # fp = 0
    # fn = 0
    # for i in range(len(y_true)):
    #     t = y_true[i]
    #     p = y_pred[i]
    #     if t == 1 and p == 1:
    #         tp = tp + 1
    #     if t == 0 and p == 1:
    #         fp = fp + 1
    #     if t == 1 and p == 0:
    #         fn = fn + 1
    # return tp, fp, fn
    return 0, 0, 0


def precision(y_true, y_pred):
    # tp, fp, fn = counts(y_true, y_pred)
    # if tp + fp == 0:
    #     return 0.0
    # return tp / (tp + fp)
    return 0.0


def recall(y_true, y_pred):
    # tp, fp, fn = counts(y_true, y_pred)
    # if tp + fn == 0:
    #     return 0.0
    # return tp / (tp + fn)
    return 0.0


def f1(y_true, y_pred):
    # p = precision(y_true, y_pred)
    # r = recall(y_true, y_pred)
    # if p + r == 0:
    #     return 0.0
    # return 2 * p * r / (p + r)
    return 0.0


truth = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
model = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
lazy = [0] * 10
for name, pred in [("model", model), ("always 0", lazy)]:
    acc = sum(t == p for t, p in zip(truth, pred)) / len(truth)
    print(f"{name:9} accuracy {acc:.1f}  precision {precision(truth, pred):.2f}  recall {recall(truth, pred):.2f}  F1 {f1(truth, pred):.2f}")
