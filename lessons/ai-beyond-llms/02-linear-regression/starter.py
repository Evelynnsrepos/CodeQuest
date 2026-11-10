def fit_line(xs, ys):
    # n = len(xs)
    # sum_x = 0
    # sum_y = 0
    # for i in range(n):
    #     sum_x = sum_x + xs[i]
    #     sum_y = sum_y + ys[i]
    # mx = sum_x / n
    # my = sum_y / n
    # top = 0
    # bottom = 0
    # for i in range(n):
    #     top = top + (xs[i] - mx) * (ys[i] - my)
    #     bottom = bottom + (xs[i] - mx) ** 2
    # a = top / bottom
    # b = my - a * mx
    # return (a, b)
    return (0.0, 0.0)


def mse(xs, ys, a, b):
    # total = 0
    # for i in range(len(xs)):
    #     error = ys[i] - (a * xs[i] + b)
    #     total = total + error ** 2
    # return total / len(xs)
    return 0.0


sizes = [30, 45, 60, 75, 90]          # square metres
rents = [520, 700, 860, 1040, 1180]   # euros per month
a, b = fit_line(sizes, rents)
print(f"rent ≈ {a:.2f} * size + {b:.1f}")
print("MSE:", round(mse(sizes, rents, a, b), 2))
print("predicted rent for 50 m²:", round(a * 50 + b))
