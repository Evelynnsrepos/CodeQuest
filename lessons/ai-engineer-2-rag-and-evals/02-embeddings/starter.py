import httpx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def normalize(M):
    return M


def ollama_embed(texts, model="nomic-embed-text", url="http://localhost:11434", client=None):
    return np.zeros((len(texts), 1))


class LocalEmbedder:
    def __init__(self, corpus):
        self.vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 4)).fit(corpus)

    def embed(self, texts):
        return np.zeros((len(texts), 1))


emb = LocalEmbedder(["nix garbage collection", "hyprland keybinding", "ollama embeddings"])
E = emb.embed(["delete old nix generations", "nix garbage collect", "hyprland bind"])
print((E @ E.T).round(2))
