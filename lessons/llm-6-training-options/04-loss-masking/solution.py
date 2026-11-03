def build_labels(segments):
    input_ids, labels = [], []
    for role, tokens in segments:
        input_ids += tokens
        if role == "assistant":
            labels += tokens
        else:
            labels += [-100] * len(tokens)
    return input_ids, labels


def trained_fraction(labels):
    return sum(1 for x in labels if x != -100) / len(labels)


example = [
    ("system", [1, 15, 16, 2]),
    ("user", [1, 21, 30, 31, 32, 33, 34, 2]),
    ("assistant", [1, 40, 41, 42, 2]),
]
ids, labels = build_labels(example)
print(ids)
print(labels)
print(f"{trained_fraction(labels):.0%} of positions are trained")
