def conv2d(image, kernel):
    return []


def max_pool(image, size):
    return []


image = [
    [0, 0, 0, 9, 9, 9],
    [0, 0, 0, 9, 9, 9],
    [0, 0, 0, 9, 9, 9],
    [0, 0, 0, 9, 9, 9],
]
vertical_edge = [[-1, 1], [-1, 1]]
fmap = conv2d(image, vertical_edge)
for row in fmap:
    print(row)
print("pooled:", max_pool([[1, 3, 2, 0], [4, 2, 1, 5], [0, 1, 7, 2], [3, 2, 1, 1]], 2))
