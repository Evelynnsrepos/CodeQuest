et, cm, tl = ns.get("estimate_tokens"), ns.get("choose_max_len"), ns.get("too_long")
assert et and cm and tl, "Keep estimate_tokens, choose_max_len and too_long."
assert et({"prompt": "abcd", "answer": "efghi"}) == 23, f"estimate_tokens of 9 characters should be ceil(9/4) + 20 = 23, got {et({'prompt': 'abcd', 'answer': 'efghi'})!r}."
short = {"prompt": "a", "answer": "b"}
long = {"prompt": "x" * 2000, "answer": "y" * 2100}
assert cm([short]) == 256, "Even tiny examples get at least 256."
assert cm([short, long]) == 2048, f"An example of {et(long)} tokens needs 2048, got {cm([short, long])!r}."
edge = {"prompt": "", "answer": "z" * (4 * (512 - 20))}
assert et(edge) == 512 and cm([edge]) == 512, "Exactly 512 tokens fits in 512; don't double it."
assert tl([short, long], 1024) == [long], "too_long should return the examples whose estimate is above max_len."
