gp, ms = ns.get("gpt2_params"), ns.get("mlp_share")
assert gp and ms, "Keep gpt2_params and mlp_share."
got = gp(50257, 1024, 768, 12)
assert got == 124439808, f"GPT-2 small should have 124,439,808 parameters, got {got:,}. Check each row of the table."
assert gp(50257, 1024, 1024, 24) == 354823168, "GPT-2 medium (d 1024, 24 layers) should have 354,823,168."
assert gp(10, 4, 2, 1) == 10 * 2 + 4 * 2 + (12 * 4 + 26) + 4, "Tiny model count is off. Did you add the final LayerNorm (2d)?"
s = ms(768)
assert abs(s - (8 * 768 ** 2 + 5 * 768) / (12 * 768 ** 2 + 13 * 768)) < 1e-12, f"mlp_share(768) should be about 0.667, got {s!r}."
