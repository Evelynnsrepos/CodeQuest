def dot(a, b):
    if len(a) != len(b):
        raise ValueError("vectors must have the same dimension")
    return sum(x * y for x, y in zip(a, b))


def neuron(w, x, b):
    return dot(w, x) + b


def relation(a, b):
    d = dot(a, b)
    if d > 0:
        return "same direction"
    if d < 0:
        return "opposite"
    return "perpendicular"


print(dot([2, 5, 1], [3, 1, 4]), neuron([0.5, -1], [4, 1], 0.2))
print(relation([1, 2], [3, 4]), relation([1, 2], [2, -1]), relation([1, 0], [-2, 1]))
