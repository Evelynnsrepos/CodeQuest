def prob(wanted, total):
    return wanted / total


def complement(p):
    return 1 - p


def is_valid(p):
    return 0 <= p <= 1


print(prob(1, 6), complement(0.92), is_valid(1.5))
