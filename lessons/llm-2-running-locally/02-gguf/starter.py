def read_gguf_header(data):
    # check the magic, then read the three numbers
    return {}


# the first 24 bytes of a Llama 3.1 8B GGUF (the metadata count depends on who converted it)
sample = b"GGUF" + (3).to_bytes(4, "little") + (292).to_bytes(8, "little") + (29).to_bytes(8, "little")
print(read_gguf_header(sample))
