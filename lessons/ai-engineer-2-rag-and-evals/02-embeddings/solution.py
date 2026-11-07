import httpx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def normalize(M):
    M = np.asarray(M, dtype=float)
    lengths = np.linalg.norm(M, axis=1, keepdims=True)
    lengths[lengths == 0] = 1
    return M / lengths


def ollama_embed(texts, model="nomic-embed-text", url="http://localhost:11434", client=None):
    if client is not None:
        post = client.post
    else:
        post = httpx.post
    payload = {"model": model, "input": list(texts)}
    r = post(url + "/api/embed", json=payload, timeout=60)
    r.raise_for_status()
    return normalize(r.json()["embeddings"])


class LocalEmbedder:
    def __init__(self, corpus):
        self.vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 4)).fit(corpus)

    def embed(self, texts):
        return normalize(self.vec.transform(texts).toarray())


emb = LocalEmbedder(["nix garbage collection", "hyprland keybinding", "ollama embeddings"])
E = emb.embed(["delete old nix generations", "nix garbage collect", "hyprland bind"])
print((E @ E.T).round(2))
