---
title: scikit-learn: classic ML done right
minutes: 30
xp: 60
hint: split: return train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)
hint: make_model: return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
hint: evaluate: split, then model = make_model() and model.fit(X_train, y_train), test_accuracy = model.score(X_test, y_test)
hint: evaluate: cv = cross_val_score(make_model(), X_train, y_train, cv=5), then return (test_accuracy, cv.mean())
---
# Train, test, cross-validate

⏱️ About 30 minutes

> **Warm-up:** in AI beyond LLMs you wrote logistic regression by hand. What did you have to code that a library could do for you?

**scikit-learn** is the standard library for classic machine learning: linear and logistic regression, trees, random forests, gradient boosting, k-means, plus everything around them. Every model has the same two methods:

```python
model.fit(X_train, y_train)      # learn
model.predict(X_test)            # use
```

The three habits that make results trustworthy:

1. **Split** before anything else: `train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)`. `stratify=y` keeps the class balance equal in both parts.
2. **Pipeline** the preprocessing with the model: `make_pipeline(StandardScaler(), LogisticRegression())`. The scaler then learns its means **only from training data**. Scaling on all the data first leaks test information into training (a classic mistake that inflates scores).
3. **Cross-validate**: `cross_val_score(pipe, X, y, cv=5)` trains 5 times on different splits and gives 5 scores. Report the mean ± spread, not one lucky number.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `train_test_split(X, y, ...)` | | returns **four** things, in this order: X_train, X_test, y_train, y_test |
| `X_train, X_test, y_train, y_test = split(X, y)` | | catches the four into four names |
| `make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))` | | one model that first scales, then classifies. `max_iter=1000` lets it try longer before giving up. |
| `model.fit(X_train, y_train)` | | learn from the training part |
| `model.score(X_test, y_test)` | | the accuracy on the test part |
| `cross_val_score(model, X, y, cv=5)` | | trains and tests 5 times, returns 5 accuracies |
| `cv.mean()` | | their average |

### 👀 What cross-validation does, with 10 rows

`cv=5` cuts the training rows into 5 groups of 2. Round 1 tests on group 1 and trains on groups 2–5. Round 2 tests on group 2, and so on. Every row is tested exactly once, and you get 5 scores, like (0.95, 0.97, 0.96, 0.99, 0.95). Their mean, 0.964, is more trustworthy than any single one.

## 🎯 Your quest

Use the built-in breast cancer dataset (`load_breast_cancer(return_X_y=True)`, 569 patients, 30 measurements, ships with scikit-learn, no download).

1. `split(X, y)`: `train_test_split` with `test_size=0.2`, `random_state=0`, `stratify=y`; return `(X_train, X_test, y_train, y_test)`.
2. `make_model()`: a pipeline of `StandardScaler` and `LogisticRegression(max_iter=1000)`.
3. `evaluate(X, y)`: split, fit `make_model()` on the training part, and return `(test_accuracy, cv_mean)` where `cv_mean` is the mean of 5-fold `cross_val_score` of a **fresh** `make_model()` on the **training** part only.

**Part 1:** `split`. Replace `return X, X, y, y` with:

1. `return train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)`

**Part 2:** `make_model`. Replace `return None` with:

1. `return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))`

**Part 3:** `evaluate`. Replace `return (0.0, 0.0)` with:

1. `X_train, X_test, y_train, y_test = split(X, y)`
2. `model = make_model()`
3. `model.fit(X_train, y_train)`
4. `test_accuracy = model.score(X_test, y_test)`
5. `cv = cross_val_score(make_model(), X_train, y_train, cv=5)`
6. `return (test_accuracy, cv.mean())`

**Remember:** split first, pipeline the preprocessing, cross-validate.

## Review

<details><summary>What does errors="coerce" do in pandas?</summary>Turns values it can't parse into missing values (NaN/NaT) instead of raising an error.</details>
