from datetime import datetime

FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%m/%d/%Y", "%d %b %Y"]


def to_iso(s, formats=FORMATS):
    return None


def bad_dates(values):
    return []


vals = ["04.11.2026", "2026-11-04", "11/04/2026", "4 Nov 2026", "31.02.2026", "", "soon"]
print([to_iso(v) for v in vals], bad_dates(vals))
