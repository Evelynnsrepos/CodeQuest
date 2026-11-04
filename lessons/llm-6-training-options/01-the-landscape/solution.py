ON_MY_PC = {
    "prompting": True,
    "rag": True,
    "pretraining": False,
    "full_finetuning": False,
    "lora": True,
    "qlora": True,
    "dpo_with_lora": True,
}

CHANGES_WEIGHTS = {
    "prompting": False,
    "rag": False,
    "pretraining": True,
    "full_finetuning": True,
    "lora": True,
    "qlora": True,
    "dpo_with_lora": True,
}

for method in ON_MY_PC:
    print(f"{method:16} on my PC: {ON_MY_PC[method]!s:5}  changes weights: {CHANGES_WEIGHTS[method]}")
