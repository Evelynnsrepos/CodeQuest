vocab = {"Hello": 0, ",": 1, " how": 2, " are": 3, " you": 4, "?": 5, " doing": 6, "!": 7}
id_to_token = {i: t for t, i in vocab.items()}  # the same list, the other way round


def encode(tokens):
    ids = []
    for token in tokens:
        pass  # look up the token's ID and append it to ids
    return ids


def decode(ids):
    pieces = []
    # turn every ID back into its token, then join the pieces
    return ""


tokens = ["Hello", ",", " how", " are", " you", "?"]
ids = encode(tokens)
print(ids)
print(decode(ids))
