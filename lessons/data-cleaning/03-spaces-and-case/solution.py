def tidy(s):
    if s is None:
        return None
    return " ".join(s.replace("\u200b", "").split())


def key(s):
    t = tidy(s)
    return None if t is None else t.casefold()


def distinct(values):
    return len({key(v) for v in values if v is not None})


print(repr(tidy("  Ber\u200blin \t\n ")), key("STRASSE") == key("Straße"), distinct(["Berlin", "berlin ", " BERLIN", None]))
