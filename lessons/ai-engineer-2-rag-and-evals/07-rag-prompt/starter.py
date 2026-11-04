import re

HEADER = ("Answer the question using only the sources below. Cite sources like [1]. "
          "If the sources don't contain the answer, say \"I don't know\".")


def tokens(text):
    return len(text) // 4


def build_prompt(question, chunks, budget):
    return "", []


def citations(answer):
    return []


def check_answer(answer, n_sources):
    return "ok"


chunks = [{"id": "nix-gc", "text": "Run nix-collect-garbage -d to delete old generations."},
          {"id": "nix-flakes", "text": "A flake pins its inputs in flake.lock."}]
prompt, used = build_prompt("how do I free disk space?", chunks, budget=40)
print(prompt, used)
print(check_answer("Use nix-collect-garbage -d [1].", 2), check_answer("Do it [3].", 2), check_answer("Easy!", 2))
