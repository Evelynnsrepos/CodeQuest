def left(total, model):
    return total - model


def fits(model, total):
    return model <= total


def per_program(total, n):
    return total / n


print(left(12, 5), fits(5, 12), fits(16, 12), per_program(12, 3), per_program(7, 2))
