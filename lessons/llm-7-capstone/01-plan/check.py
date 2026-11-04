P = ns.get("PROJECT", {})
assert len(P.get("goal", "")) >= 15, "Write your capstone goal as one real sentence."
assert "/" in P.get("base_model", ""), "base_model should be a Hugging Face name like Qwen/Qwen3-4B."
assert len(P.get("why_finetune", "")) >= 20, "Explain why fine-tuning (not only RAG or a prompt) fits your goal."
sc = P.get("success_criteria", [])
assert isinstance(sc, list) and len(sc) >= 3 and all(isinstance(s, str) and len(s) >= 10 for s in sc), "Give at least three checkable success criteria."
pb = ns.get("pick_base")
assert pb, "Keep the function pick_base."
c = [{"name": "a", "params_b": 1.0, "instruct": True, "license": "mit"},
     {"name": "b", "params_b": 3.0, "instruct": True, "license": "mit"},
     {"name": "c", "params_b": 3.5, "instruct": False, "license": "mit"},
     {"name": "d", "params_b": 3.8, "instruct": True, "license": "proprietary"},
     {"name": "e", "params_b": 9.0, "instruct": True, "license": "apache-2.0"}]
assert pb(c, 4) == "b", f"pick_base should return 'b' (largest instruct model with an OK license under 4B), got {pb(c, 4)!r}."
assert pb(c, 2) == "a", "With max 2B, only 'a' qualifies."
assert pb(c, 0.5) is None, "When nothing qualifies, return None."
