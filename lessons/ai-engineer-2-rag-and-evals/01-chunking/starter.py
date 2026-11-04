import re


def chunk_words(text, size, overlap):
    return [text]


def chunk_sentences(text, max_words):
    return [text]


def with_meta(doc_id, chunks):
    return []


text = "One two three four five six seven eight nine ten"
print(chunk_words(text, 4, 1))
print(chunk_sentences("Short one. This is the second sentence here. Third! And a fourth?", 6))
