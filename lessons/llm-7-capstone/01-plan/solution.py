OK_LICENSES = {"apache-2.0", "mit", "llama3.2", "gemma"}

PROJECT = {
    "goal": "Explain NixOS and LLM concepts in my own casual writing style.",
    "base_model": "Qwen/Qwen3-4B",
    "why_finetune": "A writing style is behaviour, and a system prompt alone doesn't hold it reliably.",
    "success_criteria": [
        "Blind judges prefer the tuned answers on at least 65% of 30 held-out prompts.",
        "Answers stay factually correct on the held-out NixOS questions.",
        "It still calls its MCP tool correctly in 9 of 10 test prompts.",
    ],
}


def pick_base(candidates, max_params_b):
    best = None
    for c in candidates:
        if c["instruct"] and c["license"] in OK_LICENSES and c["params_b"] <= max_params_b:
            if best is None or c["params_b"] > best["params_b"]:
                best = c
    if best is None:
        return None
    return best["name"]


candidates = [
    {"name": "Qwen/Qwen3-4B", "params_b": 4.0, "instruct": True, "license": "apache-2.0"},
    {"name": "Qwen/Qwen3-4B-Base", "params_b": 4.0, "instruct": False, "license": "apache-2.0"},
    {"name": "meta-llama/Llama-3.2-3B-Instruct", "params_b": 3.2, "instruct": True, "license": "llama3.2"},
    {"name": "some-org/Mystery-7B-Chat", "params_b": 7.0, "instruct": True, "license": "unknown"},
    {"name": "HuggingFaceTB/SmolLM3-3B", "params_b": 3.1, "instruct": True, "license": "apache-2.0"},
]
print("pick:", pick_base(candidates, 4))
print("pick (≤ 3.5B):", pick_base(candidates, 3.5))
