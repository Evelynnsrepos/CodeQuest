def gguf_commands(merged_dir, name, quant):
    return []


merge_dtype = ""

for command in gguf_commands("merged", "evelynn-style-4b", "Q4_K_M"):
    print("$", command)
