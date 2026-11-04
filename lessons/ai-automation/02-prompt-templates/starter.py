def fill(template, fields):
    return template


t = "Summarize this note from {date} in {words} words:\n{note}"
print(fill(t, {"date": "Monday", "words": 30, "note": "We agreed to ship on Friday."}))
