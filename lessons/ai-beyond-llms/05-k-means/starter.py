def dist2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def kmeans(points, centers, iters):
    return centers, [0] * len(points)


points = [(1, 1), (1.5, 2), (1, 0.5), (8, 8), (9, 9.5), (8.5, 7.5), (1, 9), (2, 8.5)]
centers, groups = kmeans(points, [(0, 0), (5, 5), (0, 10)], 5)
print("centers:", [tuple(round(v, 2) for v in c) for c in centers])
print("groups: ", groups)
