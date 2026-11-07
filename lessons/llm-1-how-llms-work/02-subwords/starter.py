VOCAB = [" the", " cat", " sat", " on", " mat", "The", " Die", " Katze", " saß",
         " auf", " der", " Mat", "te", " ", "a", "e", "i", "o", "u", "s", "t", "z", "ß",
         "D", "K", "M", "T", "c", "d", "f", "h", "m", "n", "r", "."]


def tokenize(text):
    tokens, i = [], 0
    while i < len(text):
        # longest vocabulary entry that matches at position i
        match = max((v for v in VOCAB if text.startswith(v, i)), key=len)
        tokens.append(match)
        i += len(match)
    return tokens


def tokens_per_word(text):
    # return len(tokenize(text)) / len(text.split())
    return 0


english = "The cat sat on the mat."
german = "Die Katze saß auf der Matte."
print(tokenize(english))
print(tokenize(german))
print("English:", round(tokens_per_word(english), 2), "tokens per word")
print("German: ", round(tokens_per_word(german), 2), "tokens per word")

german_costs_more = None  # True or False
