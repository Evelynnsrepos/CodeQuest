def bowl(p):
    x, y = p
    return x ** 2 + 3 * y ** 2


def numeric_gradient(f, point):
    h = 1e-5
    grad = []
    for i in range(len(point)):
        up, down = list(point), list(point)
        up[i] += h
        down[i] -= h
        grad.append((f(up) - f(down)) / (2 * h))
    return grad


def gradient_descent(f, start, learning_rate, steps):
    point = list(start)
    for _ in range(steps):
        grad = numeric_gradient(f, point)
        point = [p - learning_rate * g for p, g in zip(point, grad)]
    return point


print("gradient at (1, 1):", [round(g, 4) for g in numeric_gradient(bowl, [1.0, 1.0])])
for lr in [0.01, 0.1, 0.4]:
    end = gradient_descent(bowl, [3.0, 2.0], lr, 30)
    print(f"lr={lr}: ended at {[round(v, 4) for v in end]}, loss {bowl(end):.4f}")
