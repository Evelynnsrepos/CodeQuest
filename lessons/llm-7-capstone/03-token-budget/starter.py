import math


def estimate_tokens(example):
    return 0


def choose_max_len(examples):
    return 256


def too_long(examples, max_len):
    return []


examples = [
    {"prompt": "What is a flake?", "answer": "A Nix project with pinned inputs and a defined set of outputs. " * 3},
    {"prompt": "Explain RoPE.", "answer": "Rotary position embeddings rotate query and key vectors by an angle that depends on position. " * 12},
    {"prompt": "Hi", "answer": "Hey!"},
]
for ex in examples:
    print(estimate_tokens(ex), "tokens:", ex["prompt"])
max_len = choose_max_len(examples)
print("max_seq_length:", max_len)
print("too long for 256:", [ex["prompt"] for ex in too_long(examples, 256)])
