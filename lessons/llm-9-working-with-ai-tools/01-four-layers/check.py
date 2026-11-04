lo, pi = ns.get("layer_of"), ns.get("pick_integration")
assert lo and pi, "Keep layer_of and pick_integration."
cases = {"Qwen": "model", "Gemma": "model", "Ollama": "runner", "llama.cpp": "runner", "vLLM": "runner",
         "Claude Code": "harness", "Aider": "harness", "Open WebUI": "harness",
         "MCP server": "integration", "skill": "integration", "Hook": "integration", "plugin": "integration"}
for name, want in cases.items():
    assert lo(name) == want, f"layer_of({name!r}) should be {want!r}, got {lo(name)!r}."
assert lo("toaster") == "unknown", "Unknown names → 'unknown'."
assert pi("know how") == "skill" and pi("be able") == "mcp" and pi("always") == "hook", "know how → skill, be able → mcp, always → hook."
