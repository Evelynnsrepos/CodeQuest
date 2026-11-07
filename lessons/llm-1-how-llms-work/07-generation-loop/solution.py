MODEL = {
    "Once": {" upon": 0.9, " more": 0.1},
    " upon": {" a": 0.95, " the": 0.05},
    " a": {" time": 0.7, " hill": 0.3},
    " time": {" there": 0.5, ",": 0.3, "<eos>": 0.2},
    " there": {" was": 0.8, " lived": 0.2},
    " was": {" a": 0.6, " no": 0.4},
    "The": {" end": 0.6, " cat": 0.4},
    " end": {".": 0.9, " of": 0.1},
    ".": {"<eos>": 1.0},
}


def generate(prompt, max_tokens):
    tokens = list(prompt)
    for _ in range(max_tokens):
        dist = MODEL[tokens[-1]]
        best = None
        best_p = -1
        for token in dist:
            if dist[token] > best_p:
                best = token
                best_p = dist[token]
        if best == "<eos>":
            break
        tokens.append(best)
    return tokens


print(generate(["Once"], 7))
print(generate(["Once"], 2))
print(generate(["The"], 10))
