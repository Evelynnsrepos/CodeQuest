---
title: scikit-learn: classic ML done right
xp: 60
---
# Train, test, cross-validate

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

## Your quest

Use the built-in breast cancer dataset (`load_breast_cancer(return_X_y=True)`, 569 patients, 30 measurements, ships with scikit-learn, no download).

1. `split(X, y)`: `train_test_split` with `test_size=0.2`, `random_state=0`, `stratify=y`; return `(X_train, X_test, y_train, y_test)`.
2. `make_model()`: a pipeline of `StandardScaler` and `LogisticRegression(max_iter=1000)`.
3. `evaluate(X, y)`: split, fit `make_model()` on the training part, and return `(test_accuracy, cv_mean)` where `cv_mean` is the mean of 5-fold `cross_val_score` of a **fresh** `make_model()` on the **training** part only.

**Remember:** split first, pipeline the preprocessing, cross-validate.

## Review

<details><summary>What does errors="coerce" do in pandas?</summary>Turns values it can't parse into missing values (NaN/NaT) instead of raising an error.</details>
