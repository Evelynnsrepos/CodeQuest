def tidy(s):
    return s


def key(s):
    return s


def distinct(values):
    return 0


print(repr(tidy("  Ber\u200blin \t\n ")), key("STRASSE") == key("Straße"), distinct(["Berlin", "berlin ", " BERLIN", None]))
