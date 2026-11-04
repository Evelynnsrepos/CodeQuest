def precision(y_true, y_pred):
    return 0.0


def recall(y_true, y_pred):
    return 0.0


def f1(y_true, y_pred):
    return 0.0


truth = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
model = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
lazy = [0] * 10
for name, pred in [("model", model), ("always 0", lazy)]:
    acc = sum(t == p for t, p in zip(truth, pred)) / len(truth)
    print(f"{name:9} accuracy {acc:.1f}  precision {precision(truth, pred):.2f}  recall {recall(truth, pred):.2f}  F1 {f1(truth, pred):.2f}")
