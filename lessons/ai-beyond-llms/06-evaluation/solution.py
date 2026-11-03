def counts(y_true, y_pred):
    tp = sum(t == 1 and p == 1 for t, p in zip(y_true, y_pred))
    fp = sum(t == 0 and p == 1 for t, p in zip(y_true, y_pred))
    fn = sum(t == 1 and p == 0 for t, p in zip(y_true, y_pred))
    return tp, fp, fn


def precision(y_true, y_pred):
    tp, fp, fn = counts(y_true, y_pred)
    return tp / (tp + fp) if tp + fp else 0.0


def recall(y_true, y_pred):
    tp, fp, fn = counts(y_true, y_pred)
    return tp / (tp + fn) if tp + fn else 0.0


def f1(y_true, y_pred):
    p, r = precision(y_true, y_pred), recall(y_true, y_pred)
    return 2 * p * r / (p + r) if p + r else 0.0


truth = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
model = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
lazy = [0] * 10
for name, pred in [("model", model), ("always 0", lazy)]:
    acc = sum(t == p for t, p in zip(truth, pred)) / len(truth)
    print(f"{name:9} accuracy {acc:.1f}  precision {precision(truth, pred):.2f}  recall {recall(truth, pred):.2f}  F1 {f1(truth, pred):.2f}")
