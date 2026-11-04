import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[\w-]+", text.lower())


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b

    def idf(self, t):
        return 0.0

    def score(self, query, i):
        return 0.0

    def search(self, query, k=3):
        return []


docs = ["run nix-collect-garbage -d to free space", "nix flakes pin inputs", "hyprland binds and nix"]
bm = BM25(docs)
print(bm.search("nix-collect-garbage"), bm.search("nix"))
