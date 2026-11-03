def as_percent(part, whole):
    return part / whole * 100


def percent_change(old, new):
    return (new - old) / old * 100


def percent_of(p, x):
    return p / 100 * x


print(round(as_percent(4.9, 12), 1), "% of VRAM")
print(percent_change(2.5, 1.5), "% change in loss")
print(percent_of(20, 50))
