g = ns.get("generate")
assert g, "Keep the function generate."
prompt = ["The"]
g(prompt, 5)
assert prompt == ["The"], "generate changed the prompt list that was passed in. Work on a copy (list(prompt))."
got = g([" end"], 5)
assert got == [" end", ".", ], f"generate([' end'], 5) returned {got!r}, expected [' end', '.']: stop when the pick is '<eos>' and don't add it."
