def dim(v):
    return 0


def entry(v, i):
    return v[0]


def flat_vector(flat):
    return []


v = [4, -1, 7]
print(dim(v), entry(v, 1), entry(v, 3))
print(flat_vector({"rooms": 3, "floor": 2, "size": 65}))
