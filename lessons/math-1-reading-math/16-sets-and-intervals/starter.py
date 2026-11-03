def in_interval(x, text):
    return False


def is_distribution(ps):
    return True


print(in_interval(1, "[0, 1)"), in_interval(1, "[0, 1]"), in_interval(-0.5, "(-1, 0]"))
print(is_distribution([0.2, 0.3, 0.5]), is_distribution([0.7, 0.7, -0.4]))
