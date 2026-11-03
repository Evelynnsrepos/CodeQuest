def points(f, xs):
    return []


def on_graph(f, point):
    return False


def is_falling(points):
    return False


double = lambda x: 2 * x
print(points(double, [0, 1, 2, 3]))
print(on_graph(double, (3, 6)), on_graph(double, (6, 3)))
print(is_falling([(0, 2.5), (100, 1.8), (200, 1.4)]))
