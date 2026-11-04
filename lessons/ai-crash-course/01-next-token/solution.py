def next_word(counts, word):
    if word not in counts:
        return None
    return max(counts[word], key=counts[word].get)


def generate(counts, start, n):
    words = [start]
    for _ in range(n):
        w = next_word(counts, words[-1])
        if w is None:
            break
        words.append(w)
    return " ".join(words)


counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
print(next_word(counts, "a"), "|", generate(counts, "once", 5))
