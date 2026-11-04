import json
import numpy as np


class VectorStore:
    def __init__(self, dim):
        self.items = []
        self.vectors = np.zeros((0, dim))

    def add(self, items, vectors):
        pass

    def search(self, q, k=3, where=None):
        return []

    def save(self, path):
        pass

    @classmethod
    def load(cls, path):
        return cls(1)


s = VectorStore(2)
s.add([{"id": "a", "tag": "nix"}, {"id": "b", "tag": "git"}, {"id": "c", "tag": "nix"}],
      np.array([[1.0, 0.0], [0.0, 1.0], [0.7071, 0.7071]]))
print(s.search(np.array([1.0, 0.0]), k=2), s.search(np.array([0.0, 1.0]), k=1, where={"tag": "nix"}))
