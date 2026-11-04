def next_word(counts, word):
    return None


def generate(counts, start, n):
    return start


counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
print(next_word(counts, "a"), "|", generate(counts, "once", 5))
