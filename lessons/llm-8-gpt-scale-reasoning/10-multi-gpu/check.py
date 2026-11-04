ar, zm = ns.get("all_reduce_mean"), ns.get("zero_memory_gb")
assert ar and zm, "Keep all_reduce_mean and zero_memory_gb."
got = ar([[1.0, 2.0], [3.0, 6.0]])
assert got == [2.0, 4.0], f"all_reduce_mean([[1, 2], [3, 6]]) should be [2.0, 4.0], got {got!r}."
got = ar([[1.0, 0.0, -1.0], [2.0, 0.0, 1.0], [3.0, 3.0, 0.0]])
assert all(abs(a - b) < 1e-12 for a, b in zip(got, [2.0, 1.0, 0.0])), f"Average over 3 GPUs is wrong: {got!r}."
cases = [(0, 16.0), (1, 4 + 12 / 4), (2, 2 + 14 / 4), (3, 4.0)]
for stage, bpp in cases:
    got = zm(1e9, 4, stage)
    assert abs(got - bpp) < 1e-9, f"1B params on 4 GPUs at ZeRO-{stage} should be {bpp} GB per GPU, got {got!r}."
