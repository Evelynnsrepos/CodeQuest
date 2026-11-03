def gguf_commands(merged_dir, name, quant):
    f16 = f"{name}-F16.gguf"
    quantized = f"{name}-{quant}.gguf"
    return [
        f"python convert_hf_to_gguf.py {merged_dir} --outfile {f16} --outtype f16",
        f"llama-quantize {f16} {quantized} {quant}",
        f"lms import {quantized}",
    ]


merge_dtype = "bf16"

for command in gguf_commands("merged", "evelynn-style-4b", "Q4_K_M"):
    print("$", command)
