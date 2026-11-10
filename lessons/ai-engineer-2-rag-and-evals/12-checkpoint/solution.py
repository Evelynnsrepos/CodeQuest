NOTES = {
    "nix-flakes": "A flake is a Nix project with a flake.nix file. Its inputs are pinned in flake.lock, so builds are reproducible. Run nix flake update to move the pins.",
    "nix-gc": "Old generations fill the disk. Run nix-collect-garbage -d to delete them, then rebuild the bootloader entries.",
    "hyprland-binds": "Hyprland keybindings live in hyprland.conf. A bind line is bind = SUPER, Q, exec, kitty. Reload with hyprctl reload.",
    "hyprland-monitors": "Set monitors in hyprland.conf with monitor = DP-1, 2560x1440@144, 0x0, 1. Use hyprctl monitors to list names.",
    "ollama-models": "Ollama downloads models with ollama pull llama3.2. ollama list shows installed models; ollama rm deletes one.",
    "ollama-api": "Ollama serves an API on port 11434. POST /api/chat for chat and /api/embed for embeddings. It also offers an OpenAI-compatible /v1 endpoint.",
    "quantization": "Q4_K_M uses about 4.5 bits per weight. An 8B model needs about 5 GB in Q4_K_M and 16 GB in FP16.",
    "lora": "LoRA trains two small matrices A and B per layer. B starts at zero so training begins from the base model.",
    "kv-cache": "The KV cache stores keys and values of earlier tokens so they are not recomputed. It grows with context length.",
    "git-rebase": "git rebase replays your commits on top of another branch. Never rebase commits others already pulled.",
    "python-venv": "A virtual environment keeps one project's packages separate. Create it with python -m venv .venv and activate it.",
    "codequest-phone": "CodeQuest runs on the PC and the phone opens it in the browser on the same Wi-Fi at port 8000.",
}
GOLDEN = [
    ("how do I delete old nix generations", "nix-gc"),
    ("where are flake inputs pinned", "nix-flakes"),
    ("change a keyboard shortcut in hyprland", "hyprland-binds"),
    ("set the refresh rate of my monitor", "hyprland-monitors"),
    ("download a model with ollama", "ollama-models"),
    ("which port does the ollama api use", "ollama-api"),
    ("how much memory does an 8B model need at 4 bit", "quantization"),
    ("why does lora start from the base model", "lora"),
    ("what does the kv cache store", "kv-cache"),
    ("is it safe to rebase pushed commits", "git-rebase"),
    ("keep packages separate per project", "python-venv"),
    ("open codequest on my phone", "codequest-phone"),
]

import math
import re
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


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

    def rank(self, query):
        scores = []
        for i in range(self.N):
            scores.append(self.score(query, i))
        order = []
        for step in range(self.N):
            best = None
            for i in range(self.N):
                if i not in order:
                    if best is None or scores[i] > scores[best]:
                        best = i
            order.append(best)
        return order


class LocalEmbedder:
    def __init__(self, corpus):
        self.vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 4)).fit(corpus)

    def embed(self, texts):
        M = self.vec.transform(texts).toarray()
        lengths = np.linalg.norm(M, axis=1, keepdims=True)
        lengths[lengths == 0] = 1
        return M / lengths


def rrf(rankings, k=60):
    score = {}
    for ranking in rankings:
        rank = 1
        for doc in ranking:
            score[doc] = score.get(doc, 0) + 1 / (k + rank)
            rank = rank + 1
    ids = sorted(score)
    out = []
    for step in range(len(ids)):
        best = None
        for doc in ids:
            if doc not in out:
                if best is None or score[doc] > score[best]:
                    best = doc
        out.append(best)
    return out


IDS = list(NOTES)
TEXTS = []
for i in IDS:
    TEXTS.append(NOTES[i])

BM = BM25(TEXTS)
EMB = LocalEmbedder(TEXTS)
DOC_VECS = EMB.embed(TEXTS)


def rank_bm25(question):
    out = []
    for i in BM.rank(question):
        out.append(IDS[i])
    return out


def rank_embed(question):
    scores = DOC_VECS @ EMB.embed([question])[0]
    out = []
    for i in np.argsort(-scores, kind="stable"):
        out.append(IDS[i])
    return out


def rank_hybrid(question):
    return rrf([rank_bm25(question), rank_embed(question)])


def report():
    out = {}
    methods = {"bm25": rank_bm25, "embed": rank_embed, "hybrid": rank_hybrid}
    for name in methods:
        rank = methods[name]
        hits = 0
        total = 0.0
        for q, right in GOLDEN:
            ranked = rank(q)
            if right in ranked[:3]:
                hits = hits + 1
            total = total + 1 / (ranked.index(right) + 1)
        out[name] = {"recall@3": hits / len(GOLDEN), "mrr": total / len(GOLDEN)}
    return out


for method, numbers in report().items():
    print(method, numbers)
