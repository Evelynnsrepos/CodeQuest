import csv, io


def guess_delimiter(text):
    first = text.split("\n", 1)[0]
    return max([",", ";", "\t"], key=first.count)


def read_csv(text):
    if text.startswith("\ufeff"):
        text = text[1:]
    return list(csv.DictReader(io.StringIO(text), delimiter=guess_delimiter(text)))


german = "\ufeffName;Stadt;Betrag\nAda;Berlin;12,50\n\"Smith; John\";Köln;3\n"
print(guess_delimiter(german), read_csv(german))
