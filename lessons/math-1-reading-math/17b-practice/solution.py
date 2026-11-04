import math


def percent_change(old, new):
    return (new - old) / old * 100


def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def sigma(f, a, b):
    return sum(f(i) for i in range(a, b + 1))


def halvings(n):
    return math.ceil(math.log2(n))


def in_interval(x, a, b, left_closed, right_closed):
    left = a <= x if left_closed else a < x
    right = x <= b if right_closed else x < b
    return left and right


print(percent_change(2.0, 1.5), slope((0, 3), (2, 7)), sigma(lambda i: i ** 2, 1, 3), halvings(1000), in_interval(1, 0, 1, True, False))
