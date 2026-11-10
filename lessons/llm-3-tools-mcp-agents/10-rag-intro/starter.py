import math


def embed(text):
    """Toy embedding: word counts. Real embedding models capture meaning, not just words."""
    counts = {}
    for word in text.lower().replace(".", " ").replace(",", " ").replace("?", " ").split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def cosine(a, b):
    dot = 0
    for w in a:
        dot = dot + a[w] * b.get(w, 0)
    sum_a = 0
    for w in a:
        sum_a = sum_a + a[w] * a[w]
    sum_b = 0
    for w in b:
        sum_b = sum_b + b[w] * b[w]
    norm = math.sqrt(sum_a) * math.sqrt(sum_b)
    if norm == 0:
        return 0.0
    return dot / norm


def chunk(text, size, overlap):
    words = text.split()
    chunks = []
    # for start in range(0, len(words), size - overlap):
    #     chunks.append(" ".join(words[start:start + size]))
    #     if start + size >= len(words):
    #         break
    return chunks


def retrieve(question, chunks, k):
    # q = embed(question)
    # left = list(chunks)
    # picked = []
    # for turn in range(k):
    #     if len(left) == 0:
    #         break
    #     best = None
    #     best_score = -1
    #     for c in left:
    #         score = cosine(q, embed(c))
    #         if score > best_score:
    #             best = c
    #             best_score = score
    #     picked.append(best)
    #     left.remove(best)
    # return picked
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
