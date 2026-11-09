def next_word(counts, word):
    ___
        return None
    ___
    best = None
    best_count = 0
    for w in followers:
        ___
            ___
            ___
    ___


def generate(counts, start, n):
    ___
    for step in range(n):
        last = words[-1]
        ___
        if nxt is None:
            break
        ___
    return " ".join(words)


counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
print(next_word(counts, "a"), "|", generate(counts, "once", 5))
