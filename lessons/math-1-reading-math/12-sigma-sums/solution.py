def sigma(f, start, end):
    total = 0
    for i in range(start, end + 1):
        total += f(i)
    return total


def mean(xs):
    return sum(xs) / len(xs)


def mse(ys, preds):
    return sum((y - p) ** 2 for y, p in zip(ys, preds)) / len(ys)


print(sigma(lambda i: i ** 2, 1, 3))
print(mean([2, 4, 9]), mse([1, 2, 3], [1, 0, 6]))
