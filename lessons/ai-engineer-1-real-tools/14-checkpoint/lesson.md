---
title: Checkpoint: from a CSV to a trained model
minutes: 60
xp: 120
hint: Load and one-hot: df = pd.read_csv(...), df = pd.get_dummies(df, columns=["Tag"], dtype=float), then X = df.drop(columns="Umsatz").to_numpy(float) and y = df["Umsatz"].to_numpy(float)
hint: Baseline: baseline_model = LinearRegression().fit(X_tr, y_tr) and baseline = r2_score(y_te, baseline_model.predict(X_te))
hint: Scaling: mx, sx from X_tr (add 1e-8 to sx), my, sy from y_tr. Make Xt and yt tensors from the scaled training data
hint: Network: torch.manual_seed(0), a Sequential of Linear(X.shape[1], 32), ReLU, Linear(32, 1), AdamW lr=0.01, 500 steps with mse_loss
hint: Predict under torch.no_grad(), then undo the scaling: pred = scaled * sy + my
---
# The whole toolbox, once

⏱️ About 60 minutes

> **Warm-up:** list the libraries from this course and the one job each is best at.

(NumPy: fast math on arrays. pandas: loading and shaping tables. scikit-learn: classic models, splits, metrics. PyTorch: neural networks and gradients.)

A real AI engineering task, start to finish: a café gives you a German CSV of daily sales (`make_csv()` in the starter builds it). Predict `Umsatz` from the day, the temperature and rain.

## Your quest

`run(text)` returns a dict:

1. **Load** with pandas (`sep=";"`, `decimal=","`). Turn `Tag` into one-hot columns with `pd.get_dummies(df, columns=["Tag"], dtype=float)`: a model can't multiply "Sa", but it can use a column that is 1.0 on Saturdays.
2. **Split** features `X` (everything except `Umsatz`) and target `y`, then `train_test_split(..., test_size=0.25, random_state=0)`.
3. **Baseline:** scikit-learn `LinearRegression`, scored with `r2_score` on the test part. **R²** says how much of the ups and downs the model explains: 1 = perfect, 0 = no better than always guessing the average.
4. **PyTorch:** standardize `X` with the **training** mean and std (lesson 02, and lesson 13's leak warning), standardize `y` the same way, train an MLP (`n_features → 32 → 1`, ReLU) with AdamW (`lr=0.01`) for 500 full-batch steps with seed 0, predict the test part, undo the `y` scaling, and compute R².
5. Return `{"rows": number of rows, "features": number of feature columns, "baseline_r2": ..., "torch_r2": ...}`.

Both R² values should be above **0.9**. On data this simple, the linear baseline is as good as the network, which is the lesson: **always try the simple model first.**

### 🔬 R², step by step

R² = 1 − (the model's squared misses) / (the squared misses of always guessing the average). With real values (10, 20, 30) and predictions (12, 18, 30):

1. The model's misses: −2, 2, 0. Squared and added: 4 + 4 + 0 = 8.
2. The average is 20. Its misses: −10, 0, 10. Squared and added: 100 + 0 + 100 = 200.
3. R² = 1 − 8 / 200 = 1 − 0.04 = **0.96**. `r2_score(y_true, y_pred)` does this for you.

### How to answer

Every line is from this course: lesson 04 (load), 13 (split and score), 02 (standardize), 08 (the loop). Replace the starter's `return` line with:

1. `df = pd.read_csv(io.StringIO(text), sep=";", decimal=",")`
2. `df = pd.get_dummies(df, columns=["Tag"], dtype=float)`
3. `X = df.drop(columns="Umsatz").to_numpy(float)`
4. `y = df["Umsatz"].to_numpy(float)`
5. `X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)`
6. `baseline_model = LinearRegression().fit(X_tr, y_tr)`
7. `baseline = r2_score(y_te, baseline_model.predict(X_te))`
8. `mx = X_tr.mean(0)`
9. `sx = X_tr.std(0) + 1e-8`
10. `my = y_tr.mean()`
11. `sy = y_tr.std()`
12. `Xt = torch.tensor((X_tr - mx) / sx, dtype=torch.float32)`
13. `yt = torch.tensor((y_tr - my) / sy, dtype=torch.float32).unsqueeze(1)`
14. `torch.manual_seed(0)`
15. `net = torch.nn.Sequential(torch.nn.Linear(X.shape[1], 32), torch.nn.ReLU(), torch.nn.Linear(32, 1))`
16. `opt = torch.optim.AdamW(net.parameters(), lr=0.01)`
17. `for step in range(500):`
18. `    opt.zero_grad()`
19. `    loss = torch.nn.functional.mse_loss(net(Xt), yt)`
20. `    loss.backward()`
21. `    opt.step()`
22. `with torch.no_grad():`
23. `    X_test = torch.tensor((X_te - mx) / sx, dtype=torch.float32)`
24. `    scaled = net(X_test).squeeze(1).numpy()`
25. `pred = scaled * sy + my`
26. `return {"rows": len(df), "features": X.shape[1], "baseline_r2": float(baseline), "torch_r2": float(r2_score(y_te, pred))}`

A few new pieces: `df.drop(columns="Umsatz")` is every column except that one, `.to_numpy(float)` turns the table into a NumPy array, `+ 1e-8` (0.00000001) stops a division by zero when a column never changes, and `.squeeze(1)` removes the column axis that `unsqueeze(1)` added.

## Review

<details><summary>What are the four steps of the generation loop?</summary>Crop the context, predict the last position, sample, append.</details>
<details><summary>Why standardize with the training set's mean only?</summary>Using test data to compute it leaks information and makes the test score too optimistic.</details>

## What's next

**AI engineer 2** builds real retrieval (RAG) and evaluations with these tools, and **AI engineer 3** ships them as a tested web service.
