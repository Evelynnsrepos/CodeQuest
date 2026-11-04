n, size = ns.get("neuron"), ns.get("model_size_gb")
assert n and size, "Keep the functions neuron and model_size_gb."
got = n([2.0, 3.0], [0.5, -1.0], 0.25)
assert abs(got - (-1.75)) < 1e-9, f"neuron([2.0, 3.0], [0.5, -1.0], 0.25) returned {got!r}, expected -1.75."
got = n([1, 1, 1], [1, 2, 3], -6)
assert abs(got) < 1e-9, f"neuron([1, 1, 1], [1, 2, 3], -6) returned {got!r}, expected 0 (1 + 2 + 3 - 6)."
for args, want in [((8, 16), 16.0), ((7, 4), 3.5), ((70, 16), 140.0), ((14, 8), 14.0)]:
    got = size(*args)
    assert abs(got - want) < 1e-9, f"model_size_gb{args} returned {got!r}, expected {want}."
assert ns.get("fp16_8b_fits_in_12gb") is False, "An 8B model in FP16 is 16 GB. Does that fit in 12 GB of VRAM? Set fp16_8b_fits_in_12gb to True or False."
