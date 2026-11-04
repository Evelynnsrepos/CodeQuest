import math


def embed(text):
    """Toy embedding: word counts. Real embedding models capture meaning, not just words."""
    counts = {}
    for word in text.lower().replace(".", " ").replace(",", " ").replace("?", " ").split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def cosine(a, b):
    dot = sum(a[w] * b.get(w, 0) for w in a)
    norm = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return dot / norm if norm else 0.0


def chunk(text, size, overlap):
    words = text.split()
    chunks = []
    return chunks


def retrieve(question, chunks, k):
    return []


notes = ("The KV cache stores keys and values for every token. It grows with the context length. "
         "Quantization stores weights in fewer bits. Q4_K_M is a good default. "
         "MCP servers run with your permissions. Keep tool approvals on in LM Studio. "
         "RAG retrieves relevant chunks and adds them to the prompt.")
chunks = chunk(notes, 12, 4)
for c in chunks:
    print("-", c)
print()
for hit in retrieve("Why does the KV cache need more memory with a longer context?", chunks, 2):
    print("HIT:", hit)
