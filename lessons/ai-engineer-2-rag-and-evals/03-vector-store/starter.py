import json
import numpy as np


class VectorStore:
    def __init__(self, dim):
        self.items = []
        self.vectors = np.zeros((0, dim))

    def add(self, items, vectors):
        # self.items.extend(items)
        # new = np.asarray(vectors, dtype=float)
        # self.vectors = np.vstack([self.vectors, new])
        pass

    def search(self, q, k=3, where=None):
        # idx = []
        # for i in range(len(self.items)):
        #     ok = True
        #     if where:
        #         for field in where:
        #             if self.items[i].get(field) != where[field]:
        #                 ok = False
        #     if ok:
        #         idx.append(i)
        # if len(idx) == 0:
        #     return []
        # scores = self.vectors[idx] @ np.asarray(q, dtype=float)
        # order = np.argsort(-scores)[:k]
        # out = []
        # for o in order:
        #     out.append((self.items[idx[o]], float(scores[o])))
        # return out
        return []

    def save(self, path):
        # np.save(path + ".npy", self.vectors)
        # with open(path + ".json", "w", encoding="utf-8") as f:
        #     json.dump(self.items, f)
        pass

    @classmethod
    def load(cls, path):
        # vectors = np.load(path + ".npy")
        # store = cls(vectors.shape[1])
        # with open(path + ".json", encoding="utf-8") as f:
        #     store.add(json.load(f), vectors)
        # return store
        return cls(1)


s = VectorStore(2)
s.add([{"id": "a", "tag": "nix"}, {"id": "b", "tag": "git"}, {"id": "c", "tag": "nix"}],
      np.array([[1.0, 0.0], [0.0, 1.0], [0.7071, 0.7071]]))
print(s.search(np.array([1.0, 0.0]), k=2), s.search(np.array([0.0, 1.0]), k=1, where={"tag": "nix"}))
