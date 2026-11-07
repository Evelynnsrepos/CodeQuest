def conv2d(image, kernel):
    # k_h = len(kernel)
    # k_w = len(kernel[0])
    # out_h = len(image) - k_h + 1
    # out_w = len(image[0]) - k_w + 1
    # out = []
    # for i in range(out_h):
    #     row = []
    #     for j in range(out_w):
    #         total = 0
    #         for a in range(k_h):
    #             for b in range(k_w):
    #                 total = total + image[i + a][j + b] * kernel[a][b]
    #         row.append(total)
    #     out.append(row)
    # return out
    return []


def max_pool(image, size):
    # out = []
    # for i in range(0, len(image), size):
    #     row = []
    #     for j in range(0, len(image[0]), size):
    #         biggest = image[i][j]
    #         for a in range(size):
    #             for b in range(size):
    #                 if image[i + a][j + b] > biggest:
    #                     biggest = image[i + a][j + b]
    #         row.append(biggest)
    #     out.append(row)
    # return out
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
