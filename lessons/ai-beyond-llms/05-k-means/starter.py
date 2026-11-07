def dist2(p, q):
    total = 0
    for i in range(len(p)):
        total = total + (p[i] - q[i]) ** 2
    return total


def kmeans(points, centers, iters):
    # assign = []
    # for step in range(iters):
    #     assign = []
    #     for p in points:
    #         best = 0
    #         for i in range(len(centers)):
    #             if dist2(p, centers[i]) < dist2(p, centers[best]):
    #                 best = i
    #         assign.append(best)
    #     new = []
    #     for i in range(len(centers)):
    #         mine = []
    #         for j in range(len(points)):
    #             if assign[j] == i:
    #                 mine.append(points[j])
    #         if len(mine) == 0:
    #             new.append(tuple(centers[i]))
    #         else:
    #             mean = []
    #             for dim in range(len(mine[0])):
    #                 total = 0
    #                 for p in mine:
    #                     total = total + p[dim]
    #                 mean.append(total / len(mine))
    #             new.append(tuple(mean))
    #     centers = new
    # return centers, assign
    return centers, [0] * len(points)


points = [(1, 1), (1.5, 2), (1, 0.5), (8, 8), (9, 9.5), (8.5, 7.5), (1, 9), (2, 8.5)]
centers, groups = kmeans(points, [(0, 0), (5, 5), (0, 10)], 5)
print("centers:", [tuple(round(v, 2) for v in c) for c in centers])
print("groups: ", groups)
