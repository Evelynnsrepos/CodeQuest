import httpx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def normalize(M):
    M = np.asarray(M, dtype=float)
    n = np.linalg.norm(M, axis=1, keepdims=True)
    return np.divide(M, n, out=np.zeros_like(M), where=n > 0)


def ollama_embed(texts, model="nomic-embed-text", url="http://localhost:11434", client=None):
    post = client.post if client else httpx.post
    r = post(f"{url}/api/embed", json={"model": model, "input": list(texts)}, timeout=60)
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
