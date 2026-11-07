import os
import sys
import pytest

RETRIEVER = """
NOTES = {"nix-gc": "delete old nix generations with nix-collect-garbage",
         "nix-flakes": "flake inputs are pinned in flake.lock",
         "ollama-api": "the ollama api listens on port 11434"}

def retrieve(question, k=3):
    q = set(question.lower().split())
    ranked = []
    for step in range(min(k, len(NOTES))):
        best = None
        best_n = -1
        for i in NOTES:
            if i not in ranked:
                n = len(q & set(NOTES[i].split()))
                if n > best_n:
                    best = i
                    best_n = n
        ranked.append(best)
    return ranked
"""


def write_suite(folder, golden, threshold):
    pass


def run_suite(folder):
    return 1


import tempfile
with tempfile.TemporaryDirectory() as d:
    write_suite(d, [("delete old generations", "nix-gc")], 0.8)
    print("exit code:", run_suite(d))
