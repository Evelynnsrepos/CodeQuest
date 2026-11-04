def dist2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def kmeans(points, centers, iters):
    centers = [tuple(c) for c in centers]
    assign = []
    for _ in range(iters):
        assign = [min(range(len(centers)), key=lambda i: dist2(p, centers[i])) for p in points]
        new = []
        for i, c in enumerate(centers):
            mine = [p for p, a in zip(points, assign) if a == i]
            new.append(tuple(sum(v) / len(mine) for v in zip(*mine)) if mine else c)
        centers = new
    return centers, assign


points = [(1, 1), (1.5, 2), (1, 0.5), (8, 8), (9, 9.5), (8.5, 7.5), (1, 9), (2, 8.5)]
centers, groups = kmeans(points, [(0, 0), (5, 5), (0, 10)], 5)
print("centers:", [tuple(round(v, 2) for v in c) for c in centers])
print("groups: ", groups)
