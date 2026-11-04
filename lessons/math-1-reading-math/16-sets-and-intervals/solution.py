def in_interval(x, text):
    lo, hi = (float(v) for v in text[1:-1].split(","))
    above = lo <= x if text[0] == "[" else lo < x
    below = x <= hi if text[-1] == "]" else x < hi
    return above and below


def is_distribution(ps):
    return all(in_interval(p, "[0, 1]") for p in ps) and abs(sum(ps) - 1) < 1e-9


print(in_interval(1, "[0, 1)"), in_interval(1, "[0, 1]"), in_interval(-0.5, "(-1, 0]"))
print(is_distribution([0.2, 0.3, 0.5]), is_distribution([0.7, 0.7, -0.4]))
