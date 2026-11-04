import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[\w-]+", text.lower())


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.tokens = [tokenize(d) for d in docs]
        self.tf = [Counter(t) for t in self.tokens]
        self.N = len(docs)
        self.avglen = sum(len(t) for t in self.tokens) / self.N
        self.df = Counter(w for t in self.tokens for w in set(t))

    def idf(self, t):
        n = self.df.get(t, 0)
        return math.log((self.N - n + 0.5) / (n + 0.5) + 1)

    def score(self, query, i):
        length = len(self.tokens[i])
        total = 0.0
        for t in tokenize(query):
            f = self.tf[i].get(t, 0)
            if f:
                total += self.idf(t) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * length / self.avglen))
        return total

    def search(self, query, k=3):
        scored = [(i, self.score(query, i)) for i in range(self.N)]
        scored = [p for p in scored if p[1] > 0]
        return sorted(scored, key=lambda p: -p[1])[:k]


docs = ["run nix-collect-garbage -d to free space", "nix flakes pin inputs", "hyprland binds and nix"]
bm = BM25(docs)
print(bm.search("nix-collect-garbage"), bm.search("nix"))
