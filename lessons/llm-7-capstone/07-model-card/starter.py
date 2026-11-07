SECTIONS = ["## Base model", "## Training data", "## Training", "## Evaluation", "## Limitations", "## How to run"]


def make_card(info):
    # bodies = [
    #     info["base_model"] + "\n\nLicense: " + info["license"],
    #     info["data"],
    #     info["training"],
    #     info["evaluation"],
    #     info["limitations"],
    #     info["how_to_run"],
    # ]
    # parts = ["# " + info["name"]]
    # for i in range(len(SECTIONS)):
    #     parts.append(SECTIONS[i] + "\n\n" + bodies[i])
    # return "\n\n".join(parts) + "\n"
    return ""


def missing_sections(markdown):
    # lines = markdown.splitlines()
    # missing = []
    # for s in SECTIONS:
    #     if s not in lines:
    #         missing.append(s)
    # return missing
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
