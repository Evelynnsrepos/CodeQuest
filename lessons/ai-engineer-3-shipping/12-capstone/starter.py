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
from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


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


def get_llm():
    def pretend_llm(prompt):
        return "Use the first source [1].", len(prompt) // 4, 8
    return pretend_llm


TRACKER = []


# IDS = list(NOTES)
# TEXTS = []
# for i in IDS:
#     TEXTS.append(NOTES[i])
# BM = BM25(TEXTS)


# def search(q, k=3):
#     scored = []
#     for i in range(len(IDS)):
#         s = BM.score(q, i)
#         if s > 0:
#             scored.append((s, IDS[i]))
#     out = []
#     for step in range(k):
#         if len(scored) == 0:
#             break
#         top = scored[0]
#         for pair in scored:
#             if pair[0] > top[0]:
#                 top = pair
#         out.append(top[1])
#         scored.remove(top)
#     return out


# class SearchBody(BaseModel):
#     q: str = Field(min_length=1)
#     k: int = Field(default=3, ge=1, le=10)


# class AskBody(BaseModel):
#     question: str = Field(min_length=1, max_length=1000)


app = FastAPI()


# @app.get("/health")
# def health():
#     return {"status": "ok", "notes": len(NOTES)}


# @app.post("/search")
# def search_endpoint(body: SearchBody):
#     return {"results": search(body.q, body.k)}


# @app.post("/ask")
# def ask(body: AskBody, llm=Depends(get_llm)):
#     ids = search(body.question, 3)
#     if not ids:
#         return {"answer": "I don't know.", "sources": []}
#     lines = []
#     n = 1
#     for i in ids:
#         lines.append("[" + str(n) + "] (" + i + ") " + NOTES[i])
#         n = n + 1
#     sources = "\n".join(lines)
#     prompt = ("Answer using only the sources. Cite them like [1]. Say \"I don't know\" if they don't help.\n\n"
#               + sources + "\n\nQuestion: " + body.question)
#     try:
#         text, tokens_in, tokens_out = llm(prompt)
#     except RuntimeError:
#         raise HTTPException(503, "model unavailable")
#     TRACKER.append({"tokens_in": tokens_in, "tokens_out": tokens_out})
#     return {"answer": text, "sources": ids}


# @app.get("/eval")
# def evaluate():
#     hits = 0
#     for q, right in GOLDEN:
#         if right in search(q, 3):
#             hits = hits + 1
#     return {"recall@3": hits / len(GOLDEN)}


client = TestClient(app)
print(client.get("/health").json())
