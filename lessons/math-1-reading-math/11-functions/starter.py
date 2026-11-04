def compose(f, g):
    return f


def pipeline(fs, x):
    return x


square = lambda x: x ** 2
plus3 = lambda x: x + 3
print(compose(square, plus3)(2), compose(plus3, square)(2))
print(pipeline([plus3, square, str], 2))
