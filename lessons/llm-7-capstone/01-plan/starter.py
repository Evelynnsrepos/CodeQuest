OK_LICENSES = {"apache-2.0", "mit", "llama3.2", "gemma"}

PROJECT = {
    "goal": "",
    "base_model": "",
    "why_finetune": "",
    "success_criteria": [],
}


def pick_base(candidates, max_params_b):
    # best = None
    # for c in candidates:
    #     if c["instruct"] and c["license"] in OK_LICENSES and c["params_b"] <= max_params_b:
    #         if best is None or c["params_b"] > best["params_b"]:
    #             best = c
    # if best is None:
    #     return None
    # return best["name"]
    return None


candidates = [
    {"name": "Qwen/Qwen3-4B", "params_b": 4.0, "instruct": True, "license": "apache-2.0"},
    {"name": "Qwen/Qwen3-4B-Base", "params_b": 4.0, "instruct": False, "license": "apache-2.0"},
    {"name": "meta-llama/Llama-3.2-3B-Instruct", "params_b": 3.2, "instruct": True, "license": "llama3.2"},
    {"name": "some-org/Mystery-7B-Chat", "params_b": 7.0, "instruct": True, "license": "unknown"},
    {"name": "HuggingFaceTB/SmolLM3-3B", "params_b": 3.1, "instruct": True, "license": "apache-2.0"},
]
print("pick:", pick_base(candidates, 4))
print("pick (≤ 3.5B):", pick_base(candidates, 3.5))
