def dim(v):
    return len(v)


def entry(v, i):
    return v[i - 1]


def flat_vector(flat):
    return [flat["size"], flat["rooms"], flat["floor"]]


v = [4, -1, 7]
print(dim(v), entry(v, 1), entry(v, 3))
print(flat_vector({"rooms": 3, "floor": 2, "size": 65}))
