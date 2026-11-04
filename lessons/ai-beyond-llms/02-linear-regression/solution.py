def fit_line(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return (a, my - a * mx)


def mse(xs, ys, a, b):
    return sum((y - (a * x + b)) ** 2 for x, y in zip(xs, ys)) / len(xs)


sizes = [30, 45, 60, 75, 90]          # square metres
rents = [520, 700, 860, 1040, 1180]   # euros per month
a, b = fit_line(sizes, rents)
print(f"rent ≈ {a:.2f} * size + {b:.1f}")
print("MSE:", round(mse(sizes, rents, a, b), 2))
print("predicted rent for 50 m²:", round(a * 50 + b))
