def fill(template, fields):
    try:
        return template.format(**fields)
    except KeyError as e:
        raise ValueError(f"missing field: {e.args[0]}")


t = "Summarize this note from {date} in {words} words:\n{note}"
print(fill(t, {"date": "Monday", "words": 30, "note": "We agreed to ship on Friday."}))
