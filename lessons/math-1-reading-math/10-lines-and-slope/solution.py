def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def line_through(p1, p2):
    m = slope(p1, p2)
    return (m, p1[1] - m * p1[0])


def predict(m, b, x):
    return m * x + b


m, b = line_through((1, 5), (2, 7))
print("slope", slope((1, 5), (2, 7)), "line", (m, b), "10 km costs", predict(m, b, 10))
