import math


def f(x):
    return 3 * x + 2


def average(a, b):
    return (a + b) / 2


def area(r):
    return math.pi * r ** 2


print(f(4), average(3, 8), round(area(2), 3))
