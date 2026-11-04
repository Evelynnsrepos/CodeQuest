import os
import sys
import pytest

RETRIEVER = """
NOTES = {"nix-gc": "delete old nix generations with nix-collect-garbage",
         "nix-flakes": "flake inputs are pinned in flake.lock",
         "ollama-api": "the ollama api listens on port 11434"}

def retrieve(question, k=3):
    q = set(question.lower().split())
    return sorted(NOTES, key=lambda i: -len(q & set(NOTES[i].split())))[:k]
"""

TEST = """import pytest
from retriever import retrieve

GOLDEN = {golden}


@pytest.mark.parametrize("question,right", GOLDEN)
def test_right_chunk_in_top3(question, right):
    assert right in retrieve(question, k=3)


def test_overall_recall():
    hits = sum(r in retrieve(q, k=3) for q, r in GOLDEN)
    assert hits / len(GOLDEN) >= {threshold}
"""


def write_suite(folder, golden, threshold):
    with open(os.path.join(folder, "retriever.py"), "w", encoding="utf-8") as f:
        f.write(RETRIEVER)
    with open(os.path.join(folder, "test_rag.py"), "w", encoding="utf-8") as f:
        f.write(TEST.format(golden=repr(golden), threshold=threshold))


def run_suite(folder):
    if folder not in sys.path:
        sys.path.insert(0, folder)
    for name in ("retriever", "test_rag"):
        sys.modules.pop(name, None)  # a previous run's copies would shadow the new files
    return int(pytest.main(["-q", "-p", "no:cacheprovider", "--import-mode=importlib", "--rootdir", folder, folder]))


import tempfile
with tempfile.TemporaryDirectory() as d:
    write_suite(d, [("delete old generations", "nix-gc")], 0.8)
    print("exit code:", run_suite(d))
