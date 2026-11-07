def read_gguf_header(data):
    # if data[0:4] != b"GGUF":
    #     raise ValueError("not a GGUF file")
    # result = {}
    # result["version"] = int.from_bytes(data[4:8], "little")
    # result["tensor_count"] = int.from_bytes(data[8:16], "little")
    # result["metadata_kv_count"] = int.from_bytes(data[16:24], "little")
    # return result
    return {}


# the first 24 bytes of a Llama 3.1 8B GGUF (the metadata count depends on who converted it)
sample = b"GGUF" + (3).to_bytes(4, "little") + (292).to_bytes(8, "little") + (29).to_bytes(8, "little")
print(read_gguf_header(sample))
