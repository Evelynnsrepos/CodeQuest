def next_word(counts, word):
    # Step 1: if word is not in counts, return None
    # Step 2: followers = counts[word]
    # Step 3: best = None and best_count = 0
    # Step 4: for w in followers: ... if followers[w] > best_count: remember w and its count
    # Step 5: after the loop, return best
    return None


def generate(counts, start, n):
    # Step 1: words = [start]
    # Step 2: for step in range(n):
    #             last = words[-1]
    #             nxt = next_word(counts, last)
    #             if nxt is None: break
    #             words.append(nxt)
    # Step 3: return " ".join(words)
    return start


counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
print(next_word(counts, "a"), "|", generate(counts, "once", 5))
