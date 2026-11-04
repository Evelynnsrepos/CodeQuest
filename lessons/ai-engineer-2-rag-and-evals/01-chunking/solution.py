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
    chunks, current = [], []
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):
        n = len(sentence.split())
        if current and len(" ".join(current).split()) + n > max_words:
            chunks.append(" ".join(current))
            current = []
        current.append(sentence)
    if current:
        chunks.append(" ".join(current))
    return chunks


def with_meta(doc_id, chunks):
    return [{"id": f"{doc_id}#{i}", "doc": doc_id, "text": c} for i, c in enumerate(chunks)]


text = "One two three four five six seven eight nine ten"
print(chunk_words(text, 4, 1))
print(chunk_sentences("Short one. This is the second sentence here. Third! And a fourth?", 6))
