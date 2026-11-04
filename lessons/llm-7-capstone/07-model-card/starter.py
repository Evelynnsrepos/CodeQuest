SECTIONS = ["## Base model", "## Training data", "## Training", "## Evaluation", "## Limitations", "## How to run"]


def make_card(info):
    return ""


def missing_sections(markdown):
    return []


info = {
    "name": "notes-helper-3b",
    "base_model": "Llama-3.2-3B-Instruct",
    "license": "llama3.2",
    "data": "412 question/answer pairs from my own study notes, deduplicated.",
    "training": "QLoRA r=16 alpha=32 lr=2e-4, 3 epochs, max length 512, rented 24 GB GPU, 18 minutes.",
    "evaluation": "Blind win rate vs base 0.71 (0.60-0.82), tool accuracy 0.93 vs 0.95.",
    "limitations": "Only knows my notes; makes things up outside them.",
    "how_to_run": "notes-helper-3b-Q4_K_M.gguf in LM Studio, Llama 3 template.",
}
card = make_card(info)
print(card)
print("missing:", missing_sections(card))
