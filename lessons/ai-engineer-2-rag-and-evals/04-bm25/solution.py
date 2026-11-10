import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[\w-]+", text.lower())


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.tokens = []
        self.tf = []
        for d in docs:
            words = tokenize(d)
            self.tokens.append(words)
            self.tf.append(Counter(words))
        self.N = len(docs)
        total = 0
        for words in self.tokens:
            total = total + len(words)
        self.avglen = total / self.N
        self.df = Counter()
        for words in self.tokens:
            for w in set(words):
                self.df[w] = self.df[w] + 1

    def idf(self, t):
        n = self.df.get(t, 0)
        return math.log((self.N - n + 0.5) / (n + 0.5) + 1)

    def score(self, query, i):
        length = len(self.tokens[i])
        total = 0.0
        for t in tokenize(query):
            f = self.tf[i].get(t, 0)
            if f > 0:
                norm = 1 - self.b + self.b * length / self.avglen
                total = total + self.idf(t) * f * (self.k1 + 1) / (f + self.k1 * norm)
        return total

    def search(self, query, k=3):
        scored = []
        for i in range(self.N):
            s = self.score(query, i)
            if s > 0:
                scored.append((i, s))
        best = []
        for step in range(k):
            if len(scored) == 0:
                break
            top = scored[0]
            for pair in scored:
                if pair[1] > top[1]:
                    top = pair
            best.append(top)
            scored.remove(top)
        return best


docs = ["run nix-collect-garbage -d to free space", "nix flakes pin inputs", "hyprland binds and nix"]
bm = BM25(docs)
print(bm.search("nix-collect-garbage"), bm.search("nix"))
