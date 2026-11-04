def points(f, xs):
    return [(x, f(x)) for x in xs]


def on_graph(f, point):
    return abs(point[1] - f(point[0])) < 1e-9


def is_falling(points):
    return all(b[1] < a[1] for a, b in zip(points, points[1:]))


double = lambda x: 2 * x
print(points(double, [0, 1, 2, 3]))
print(on_graph(double, (3, 6)), on_graph(double, (6, 3)))
print(is_falling([(0, 2.5), (100, 1.8), (200, 1.4)]))
