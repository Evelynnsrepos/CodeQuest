def parse_number(s, decimal="."):
    return None


print(parse_number("1.234,56 €", decimal=","), parse_number("$1,234.56"), parse_number("12%"), parse_number("abc"))
