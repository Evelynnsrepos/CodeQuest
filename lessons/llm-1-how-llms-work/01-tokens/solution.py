vocab = {"Hello": 0, ",": 1, " how": 2, " are": 3, " you": 4, "?": 5, " doing": 6, "!": 7}
id_to_token = {i: t for t, i in vocab.items()}  # the same list, the other way round


def encode(tokens):
    ids = []
    for token in tokens:
        ids.append(vocab[token])
    return ids


def decode(ids):
    pieces = []
    for i in ids:
        pieces.append(id_to_token[i])
    return "".join(pieces)


tokens = ["Hello", ",", " how", " are", " you", "?"]
ids = encode(tokens)
print(ids)
print(decode(ids))
