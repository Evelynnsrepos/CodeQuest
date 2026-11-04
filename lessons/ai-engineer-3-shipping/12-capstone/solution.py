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


def get_llm():
    def pretend_llm(prompt):
        return "Use the first source [1].", len(prompt) // 4, 8
    return pretend_llm


TRACKER = []
IDS = list(NOTES)
BM = BM25([NOTES[i] for i in IDS])


def search(q, k=3):
    scored = sorted(((BM.score(q, i), IDS[i]) for i in range(len(IDS))), key=lambda p: -p[0])
    return [doc for s, doc in scored if s > 0][:k]


class SearchBody(BaseModel):
    q: str = Field(min_length=1)
    k: int = Field(default=3, ge=1, le=10)


class AskBody(BaseModel):
    question: str = Field(min_length=1, max_length=1000)


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok", "notes": len(NOTES)}


@app.post("/search")
def search_endpoint(body: SearchBody):
    return {"results": search(body.q, body.k)}


@app.post("/ask")
def ask(body: AskBody, llm=Depends(get_llm)):
    ids = search(body.question, 3)
    if not ids:
        return {"answer": "I don't know.", "sources": []}
    sources = "\n".join(f"[{n}] ({i}) {NOTES[i]}" for n, i in enumerate(ids, 1))
    prompt = ("Answer using only the sources. Cite them like [1]. Say \"I don't know\" if they don't help.\n\n"
              + sources + "\n\nQuestion: " + body.question)
    try:
        text, tokens_in, tokens_out = llm(prompt)
    except RuntimeError:
        raise HTTPException(503, "model unavailable")
    TRACKER.append({"tokens_in": tokens_in, "tokens_out": tokens_out})
    return {"answer": text, "sources": ids}


@app.get("/eval")
def evaluate():
    hits = sum(right in search(q, 3) for q, right in GOLDEN)
    return {"recall@3": hits / len(GOLDEN)}


client = TestClient(app)
print(client.get("/health").json())
