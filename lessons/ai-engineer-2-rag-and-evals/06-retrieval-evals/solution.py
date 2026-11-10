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


def recall_at_k(results, golden, k):
    hits = 0
    for q, right in golden:
        if right in results[q][:k]:
            hits = hits + 1
    return hits / len(golden)


def mrr(results, golden):
    total = 0.0
    for q, right in golden:
        if right in results[q]:
            position = results[q].index(right) + 1
            total = total + 1 / position
    return total / len(golden)


def bm25_results(notes, golden):
    ids = list(notes)
    texts = []
    for i in ids:
        texts.append(notes[i])
    bm = BM25(texts)
    results = {}
    for q, right in golden:
        ranked = []
        for i in bm.rank(q):
            ranked.append(ids[i])
        results[q] = ranked
    return results


res = bm25_results(NOTES, GOLDEN)
print("recall@1", recall_at_k(res, GOLDEN, 1), "recall@3", recall_at_k(res, GOLDEN, 3), "MRR", mrr(res, GOLDEN))
