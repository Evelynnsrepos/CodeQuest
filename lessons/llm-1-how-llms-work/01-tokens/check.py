encode, decode = ns.get("encode"), ns.get("decode")
assert encode and decode, "Keep the functions encode and decode."
got = encode([" how", " are", " you", " doing", "?"])
assert got == [2, 3, 4, 6, 5], f"encode([' how', ' are', ' you', ' doing', '?']) returned {got!r}, expected [2, 3, 4, 6, 5]."
got = decode([0, 1, 2, 3, 4, 6, 7])
assert got == "Hello, how are you doing!", f"decode([0, 1, 2, 3, 4, 6, 7]) returned {got!r}, expected 'Hello, how are you doing!'. Did you join the pieces with an empty string?"
assert decode(encode(["Hello", "!"])) == "Hello!", "decode(encode(tokens)) should give back the original text."
