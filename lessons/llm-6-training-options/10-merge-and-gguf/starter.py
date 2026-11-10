def gguf_commands(merged_dir, name, quant):
    # f16 = name + "-F16.gguf"
    # quantized = name + "-" + quant + ".gguf"
    # convert = "python convert_hf_to_gguf.py " + merged_dir + " --outfile " + f16 + " --outtype f16"
    # shrink = "llama-quantize " + f16 + " " + quantized + " " + quant
    # load = "lms import " + quantized
    # return [convert, shrink, load]
    return []


merge_dtype = ""  # "bf16" or "4bit"

for command in gguf_commands("merged", "evelynn-style-4b", "Q4_K_M"):
    print("$", command)
