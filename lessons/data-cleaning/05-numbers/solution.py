def parse_number(s, decimal="."):
    if s is None or s.strip() == "":
        return None
    for ch in ("€", "$", "£", " ", "\xa0"):
        s = s.replace(ch, "")
    if decimal == ",":
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", "")
    percent = s.endswith("%")
    if percent:
        s = s[:-1]
    try:
        value = float(s)
    except ValueError:
        return None
    return value / 100 if percent else value


print(parse_number("1.234,56 €", decimal=","), parse_number("$1,234.56"), parse_number("12%"), parse_number("abc"))
