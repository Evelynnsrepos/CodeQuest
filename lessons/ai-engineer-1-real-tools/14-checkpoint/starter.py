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
    return {"rows": 0, "features": 0, "baseline_r2": 0.0, "torch_r2": 0.0}


print(run(make_csv()))
