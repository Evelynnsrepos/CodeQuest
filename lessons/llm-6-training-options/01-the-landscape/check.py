pc, cw = ns.get("ON_MY_PC", {}), ns.get("CHANGES_WEIGHTS", {})
why_pc = {"prompting": "Prompting needs nothing but the model you already run.",
          "rag": "RAG only adds an embedding model and a search step; it runs fine locally.",
          "pretraining": "Pretraining a useful model takes trillions of tokens and thousands of GPUs.",
          "full_finetuning": "Full fine-tuning needs ~16 bytes per parameter: ~128 GB for 8B.",
          "lora": "LoRA trains only small matrices; small models fit on one consumer GPU.",
          "qlora": "QLoRA's 4-bit base model is what makes ~8B fit in 12 GB.",
          "dpo_with_lora": "DPO is a fine-tuning loss; with (Q)LoRA it fits like any LoRA run."}
want_pc = {"prompting": True, "rag": True, "pretraining": False, "full_finetuning": False, "lora": True, "qlora": True, "dpo_with_lora": True}
want_cw = {"prompting": False, "rag": False, "pretraining": True, "full_finetuning": True, "lora": True, "qlora": True, "dpo_with_lora": True}
for k, v in want_pc.items():
    assert pc.get(k) is v, f"ON_MY_PC[{k!r}]: {why_pc[k]}"
for k, v in want_cw.items():
    assert cw.get(k) is v, f"CHANGES_WEIGHTS[{k!r}]: " + ("it only changes what goes into the prompt." if not v else "it trains weights (LoRA's add-on matrices count: they become part of the model).")
