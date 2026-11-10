import io
import numpy as np
import pandas as pd
import torch
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def make_csv(n=400, seed=0):
    """A café's daily sales: warmer and weekend days sell more; rain sells less. German format."""
    rng = np.random.default_rng(seed)
    days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    lines = ["Tag;Temperatur;Regen;Umsatz"]
    for i in range(n):
        day = days[i % 7]
        temp = rng.uniform(-2, 32)
        rain = int(rng.random() < 0.3)
        sales = 300 + 9 * temp + (180 if day in ("Sa", "So") else 0) - 90 * rain + rng.normal(0, 25)
        lines.append(f"{day};{temp:.1f}".replace(".", ",") + f";{rain};" + f"{sales:.2f}".replace(".", ","))
    return "\n".join(lines) + "\n"


def run(text):
    df = pd.read_csv(io.StringIO(text), sep=";", decimal=",")
    df = pd.get_dummies(df, columns=["Tag"], dtype=float)
    X = df.drop(columns="Umsatz").to_numpy(float)
    y = df["Umsatz"].to_numpy(float)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)
    baseline_model = LinearRegression().fit(X_tr, y_tr)
    baseline = r2_score(y_te, baseline_model.predict(X_te))
    mx = X_tr.mean(0)
    sx = X_tr.std(0) + 1e-8
    my = y_tr.mean()
    sy = y_tr.std()
    Xt = torch.tensor((X_tr - mx) / sx, dtype=torch.float32)
    yt = torch.tensor((y_tr - my) / sy, dtype=torch.float32).unsqueeze(1)
    torch.manual_seed(0)
    net = torch.nn.Sequential(torch.nn.Linear(X.shape[1], 32), torch.nn.ReLU(), torch.nn.Linear(32, 1))
    opt = torch.optim.AdamW(net.parameters(), lr=0.01)
    for step in range(500):
        opt.zero_grad()
        loss = torch.nn.functional.mse_loss(net(Xt), yt)
        loss.backward()
        opt.step()
    with torch.no_grad():
        X_test = torch.tensor((X_te - mx) / sx, dtype=torch.float32)
        scaled = net(X_test).squeeze(1).numpy()
    pred = scaled * sy + my
    return {"rows": len(df), "features": X.shape[1], "baseline_r2": float(baseline), "torch_r2": float(r2_score(y_te, pred))}


print(run(make_csv()))
