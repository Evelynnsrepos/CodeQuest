def count_pairs(tokens):
    counts = {}
    # for i in range(len(tokens) - 1):
    #     pair = (tokens[i], tokens[i + 1])
    #     counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(tokens, pair):
    """Replace every occurrence of pair with one joined token."""
    out, i = [], 0
    while i < len(tokens):
        if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
            out.append(tokens[i] + tokens[i + 1])
            i += 2
        else:
            out.append(tokens[i])
            i += 1
    return out


tokens = list(" low low lower lowest newest widest")
for step in range(5):
    counts = count_pairs(tokens)
    if not counts:
        break
    best = max(counts, key=counts.get)  # the most frequent pair
    tokens = merge(tokens, best)
    print(f"merge {step + 1}: {best} -> {best[0] + best[1]!r}")
print(tokens)
