def conv2d(image, kernel):
    k_h, k_w = len(kernel), len(kernel[0])
    out_h, out_w = len(image) - k_h + 1, len(image[0]) - k_w + 1
    return [[sum(image[i + a][j + b] * kernel[a][b] for a in range(k_h) for b in range(k_w))
             for j in range(out_w)] for i in range(out_h)]


def max_pool(image, size):
    return [[max(image[i + a][j + b] for a in range(size) for b in range(size))
             for j in range(0, len(image[0]), size)] for i in range(0, len(image), size)]


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
