import csv, io


def guess_delimiter(text):
    return ","


def read_csv(text):
    return []


german = "\ufeffName;Stadt;Betrag\nAda;Berlin;12,50\n\"Smith; John\";Köln;3\n"
print(guess_delimiter(german), read_csv(german))
