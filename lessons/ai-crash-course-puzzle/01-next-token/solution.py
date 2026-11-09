def next_word(counts, word):
    if word not in counts:
        return None
    followers = counts[word]
    best = None
    best_count = 0
    for w in followers:
        if followers[w] > best_count:
            best = w
            best_count = followers[w]
    return best


def generate(counts, start, n):
    words = [start]
    for step in range(n):
        last = words[-1]
        nxt = next_word(counts, last)
        if nxt is None:
            break
        words.append(nxt)
    return " ".join(words)


counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
print(next_word(counts, "a"), "|", generate(counts, "once", 5))
