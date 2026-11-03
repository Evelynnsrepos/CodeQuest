f = ns.get("read_gguf_header")
assert f, "Keep the function read_gguf_header."
data = b"GGUF" + (2).to_bytes(4, "little") + (1234567890123).to_bytes(8, "little") + (7).to_bytes(8, "little") + b"rest"
got = f(data)
want = {"version": 2, "tensor_count": 1234567890123, "metadata_kv_count": 7}
assert got == want, f"read_gguf_header returned {got!r}, expected {want!r}."
try:
    f(b"PK\x03\x04" + bytes(20))
except ValueError:
    pass
else:
    raise AssertionError("A file that doesn't start with b'GGUF' should raise ValueError.")
