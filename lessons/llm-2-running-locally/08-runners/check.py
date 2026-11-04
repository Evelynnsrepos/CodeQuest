P, b = ns.get("PORTS"), ns.get("base_url")
assert P and b, "Keep PORTS and base_url."
for name, want in [("lmstudio", 1234), ("ollama", 11434), ("llamacpp", 8080)]:
    assert P.get(name) == want, f"The default port for {name} isn't {P.get(name)!r}. Look at the table again."
got = b("lmstudio")
assert got == "http://localhost:1234/v1", f"base_url('lmstudio') returned {got!r}, expected 'http://localhost:1234/v1'."
P["test"] = 4242
assert b("test") == "http://localhost:4242/v1", "base_url should look the port up in PORTS, not hard-code it."
