ON_MY_PC = {
    "prompting": None,
    "rag": None,
    "pretraining": None,
    "full_finetuning": None,
    "lora": None,
    "qlora": None,
    "dpo_with_lora": None,
}

CHANGES_WEIGHTS = {
    "prompting": None,
    "rag": None,
    "pretraining": None,
    "full_finetuning": None,
    "lora": None,
    "qlora": None,
    "dpo_with_lora": None,
}

for method in ON_MY_PC:
    print(f"{method:16} on my PC: {ON_MY_PC[method]!s:5}  changes weights: {CHANGES_WEIGHTS[method]}")
