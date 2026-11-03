def distance(a, b):
    return abs(a - b)


def mae(ys, preds):
    return sum(abs(y - p) for y, p in zip(ys, preds)) / len(ys)


print(distance(7, 10), mae([10, 10], [7, 13]))
