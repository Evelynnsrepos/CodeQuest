ou, lp, lw = ns.get("outer"), ns.get("lora_params"), ns.get("lora_weight")
assert ou and lp and lw, "Keep outer, lora_params and lora_weight."
assert ou([1, 2], [3, 0, 1]) == [[3, 0, 1], [6, 0, 2]], f"outer([1,2], [3,0,1]) should be [[3,0,1],[6,0,2]], got {ou([1, 2], [3, 0, 1])!r}."
assert lp(4096, 4096, 16) == 131072 and lp(10, 20, 2) == 60, f"lora_params(4096, 4096, 16) should be 131,072, got {lp(4096, 4096, 16)!r}."
got = lw([[1, 0], [0, 1]], [[1], [2]], [[0.5, 0.5]], 16, 8)
assert got == [[2.0, 1.0], [2.0, 3.0]], f"W0 + (16/8)·BA should be [[2, 1], [2, 3]], got {got!r}."
assert lw([[1, 2]], [[0]], [[5, 5]], 32, 16) == [[1, 2]], "With B = 0 the weight is exactly W0 (that's how LoRA starts)."
