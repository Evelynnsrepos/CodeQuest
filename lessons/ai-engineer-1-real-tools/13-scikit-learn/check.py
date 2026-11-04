from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline
sp, mm, ev = ns.get("split"), ns.get("make_model"), ns.get("evaluate")
assert sp and mm and ev, "Keep split, make_model and evaluate."
X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = sp(X, y)
assert len(Xte) == 114 and len(Xtr) == 455, "split: 20% test = 114 rows."
assert abs(yte.mean() - y.mean()) < 0.01, "split: use stratify=y so both parts have the same share of each class."
m = mm()
assert isinstance(m, Pipeline) and [type(s).__name__ for _, s in m.steps] == ["StandardScaler", "LogisticRegression"], "make_model: a pipeline of StandardScaler then LogisticRegression."
acc, cv = ev(X, y)
assert 0.95 <= acc <= 1.0, f"Test accuracy should be about 0.98, got {acc:.3f}."
assert 0.95 <= cv <= 1.0 and abs(cv - acc) < 0.05, f"cv_mean should be about 0.98, got {cv:.3f}. Cross-validate on the training part only."
