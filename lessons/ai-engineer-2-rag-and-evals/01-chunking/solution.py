import re


def chunk_words(text, size, overlap):
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    chunks = []
    for start in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
    return chunks


def chunk_sentences(text, max_words):
    chunks = []
    current = []
    count = 0
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):
        n = len(sentence.split())
        if len(current) > 0 and count + n > max_words:
            chunks.append(" ".join(current))
            current = []
            count = 0
        current.append(sentence)
        count = count + n
    if len(current) > 0:
        chunks.append(" ".join(current))
    return chunks


def with_meta(doc_id, chunks):
    out = []
    for i in range(len(chunks)):
        out.append({"id": str(doc_id) + "#" + str(i), "doc": doc_id, "text": chunks[i]})
    return out


text = "One two three four five six seven eight nine ten"
print(chunk_words(text, 4, 1))
print(chunk_sentences("Short one. This is the second sentence here. Third! And a fourth?", 6))
