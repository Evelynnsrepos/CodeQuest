from datetime import datetime

FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%m/%d/%Y", "%d %b %Y"]


def to_iso(s, formats=FORMATS):
    if s is None:
        return None
    s = s.strip()
    for f in formats:
        try:
            return datetime.strptime(s, f).date().isoformat()
        except ValueError:
            pass
    return None


def bad_dates(values):
    return [i for i, v in enumerate(values) if v and v.strip() and to_iso(v) is None]


vals = ["04.11.2026", "2026-11-04", "11/04/2026", "4 Nov 2026", "31.02.2026", "", "soon"]
print([to_iso(v) for v in vals], bad_dates(vals))
