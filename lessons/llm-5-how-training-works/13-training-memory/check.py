gp, ff, ql = ns.get("gpt_params"), ns.get("full_finetune_gb"), ns.get("qlora_gb")
assert gp and ff and ql, "Keep gpt_params, full_finetune_gb and qlora_gb."
assert gp(2, 10, 100) == 3400, f"gpt_params(2, 10, 100) returned {gp(2, 10, 100)!r}, expected 12·2·100 + 100·10 = 3400."
assert abs(ff(1e9) - 16) < 1e-9, f"full_finetune_gb(1e9) returned {ff(1e9)!r}, expected 16."
assert abs(ql(2e9, 1e8) - 2.6) < 1e-9, f"qlora_gb(2e9, 1e8) returned {ql(2e9, 1e8)!r}, expected (1e9 + 1.6e9) / 1e9 = 2.6."
assert ns.get("full_8b_fits") is False, "full_8b_fits: compare full_finetune_gb(8e9) with 12."
assert ns.get("qlora_8b_fits") is True, "qlora_8b_fits: about 4.6 GB + 3 GB activations. Compare with 12."
