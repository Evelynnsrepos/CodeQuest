def slope(p1, p2):
    return 0


def line_through(p1, p2):
    return (0, 0)


def predict(m, b, x):
    return 0


m, b = line_through((1, 5), (2, 7))
print("slope", slope((1, 5), (2, 7)), "line", (m, b), "10 km costs", predict(m, b, 10))
