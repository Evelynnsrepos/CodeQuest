def fit_line(xs, ys):
    return (0.0, 0.0)


def mse(xs, ys, a, b):
    return 0.0


sizes = [30, 45, 60, 75, 90]          # square metres
rents = [520, 700, 860, 1040, 1180]   # euros per month
a, b = fit_line(sizes, rents)
print(f"rent ≈ {a:.2f} * size + {b:.1f}")
print("MSE:", round(mse(sizes, rents, a, b), 2))
print("predicted rent for 50 m²:", round(a * 50 + b))
