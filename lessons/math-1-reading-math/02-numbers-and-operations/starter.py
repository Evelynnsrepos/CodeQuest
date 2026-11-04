def left(total, model):
    return 0


def fits(model, total):
    return False


def per_program(total, n):
    return 0


print(left(12, 5), fits(5, 12), fits(16, 12), per_program(12, 3), per_program(7, 2))
