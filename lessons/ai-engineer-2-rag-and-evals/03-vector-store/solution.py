import json
import numpy as np


class VectorStore:
    def __init__(self, dim):
        self.items = []
        self.vectors = np.zeros((0, dim))

    def add(self, items, vectors):
        self.items.extend(items)
        self.vectors = np.vstack([self.vectors, np.asarray(vectors, dtype=float)])

    def search(self, q, k=3, where=None):
        idx = np.arange(len(self.items))
        if where:
            idx = np.array([i for i in idx if all(self.items[i].get(f) == v for f, v in where.items())], dtype=int)
        if len(idx) == 0:
            return []
        scores = self.vectors[idx] @ np.asarray(q, dtype=float)
        order = np.argsort(-scores)[:k]
        return [(self.items[idx[o]], float(scores[o])) for o in order]

    def save(self, path):
        np.save(path + ".npy", self.vectors)
        with open(path + ".json", "w", encoding="utf-8") as f:
            json.dump(self.items, f)

    @classmethod
    def load(cls, path):
        vectors = np.load(path + ".npy")
        store = cls(vectors.shape[1])
        with open(path + ".json", encoding="utf-8") as f:
            store.add(json.load(f), vectors)
        return store


s = VectorStore(2)
s.add([{"id": "a", "tag": "nix"}, {"id": "b", "tag": "git"}, {"id": "c", "tag": "nix"}],
      np.array([[1.0, 0.0], [0.0, 1.0], [0.7071, 0.7071]]))
print(s.search(np.array([1.0, 0.0]), k=2), s.search(np.array([0.0, 1.0]), k=1, where={"tag": "nix"}))
