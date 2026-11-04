def bowl(p):
    x, y = p
    return x ** 2 + 3 * y ** 2


def numeric_gradient(f, point):
    h = 1e-5
    grad = []
    return grad


def gradient_descent(f, start, learning_rate, steps):
    point = list(start)
    return point


print("gradient at (1, 1):", [round(g, 4) for g in numeric_gradient(bowl, [1.0, 1.0])])
for lr in [0.01, 0.1, 0.4]:
    end = gradient_descent(bowl, [3.0, 2.0], lr, 30)
    print(f"lr={lr}: ended at {[round(v, 4) for v in end]}, loss {bowl(end):.4f}")
