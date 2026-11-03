import math


def estimate_tokens(example):
    return math.ceil((len(example["prompt"]) + len(example["answer"])) / 4) + 20


def choose_max_len(examples):
    longest = max(estimate_tokens(ex) for ex in examples)
    size = 256
    while size < longest:
        size *= 2
    return size


def too_long(examples, max_len):
    return [ex for ex in examples if estimate_tokens(ex) > max_len]


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
