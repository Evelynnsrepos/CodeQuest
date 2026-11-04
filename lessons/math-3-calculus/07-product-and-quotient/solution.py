def d_product(f, df, g, dg):
    return df * g + f * dg


def d_quotient(f, df, g, dg):
    return (df * g - f * dg) / g ** 2


print(d_product(4, 4, 3, 1), d_quotient(4, 4, 3, 1))
