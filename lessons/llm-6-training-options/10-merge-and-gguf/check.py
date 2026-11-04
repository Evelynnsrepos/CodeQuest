g = ns.get("gguf_commands")
assert g, "Keep the function gguf_commands."
got = g("out/merged", "pirate-1b", "Q5_K_M")
want = ["python convert_hf_to_gguf.py out/merged --outfile pirate-1b-F16.gguf --outtype f16",
        "llama-quantize pirate-1b-F16.gguf pirate-1b-Q5_K_M.gguf Q5_K_M",
        "lms import pirate-1b-Q5_K_M.gguf"]
for i, (a, b) in enumerate(zip(got + [None] * 3, want)):
    assert a == b, f"Command {i + 1} is {a!r}, expected {b!r}."
assert len(got) == 3, "Return exactly three commands."
assert ns.get("merge_dtype") == "bf16", "merge_dtype: merging into the 4-bit base bakes in quantization error before you quantize again. Load the base in bf16."
