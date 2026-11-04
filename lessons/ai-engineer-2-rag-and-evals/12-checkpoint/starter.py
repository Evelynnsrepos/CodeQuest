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
        self.k1, self.b = k1, b
        self.tokens = [tokenize(d) for d in docs]
        self.tf = [Counter(t) for t in self.tokens]
        self.N = len(docs)
        self.avglen = sum(len(t) for t in self.tokens) / self.N
        self.df = Counter(w for t in self.tokens for w in set(t))

    def score(self, query, i):
        length, total = len(self.tokens[i]), 0.0
        for t in tokenize(query):
            f = self.tf[i].get(t, 0)
            if f:
                n = self.df[t]
                idf = math.log((self.N - n + 0.5) / (n + 0.5) + 1)
                total += idf * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * length / self.avglen))
        return total


class LocalEmbedder:
    def __init__(self, corpus):
        self.vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 4)).fit(corpus)

    def embed(self, texts):
        M = self.vec.transform(texts).toarray()
        n = np.linalg.norm(M, axis=1, keepdims=True)
        return np.divide(M, n, out=np.zeros_like(M), where=n > 0)


def rrf(rankings, k=60):
    score = {}
    for ranking in rankings:
        for rank, doc in enumerate(ranking, 1):
            score[doc] = score.get(doc, 0) + 1 / (k + rank)
    return sorted(score, key=lambda d: (-score[d], d))


IDS = list(NOTES)
TEXTS = [NOTES[i] for i in IDS]


def rank_bm25(question):
    return IDS


def rank_embed(question):
    return IDS


def rank_hybrid(question):
    return IDS


def report():
    return {}


for method, numbers in report().items():
    print(method, numbers)
