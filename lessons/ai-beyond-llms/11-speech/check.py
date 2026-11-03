import math
fr, dm, hm = ns.get("frames"), ns.get("dft_magnitudes"), ns.get("hz_to_mel")
assert fr and dm and hm, "Keep frames, dft_magnitudes and hz_to_mel."
got = fr(list(range(10)), 4, 3)
assert got == [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]], f"frames(range(10), 4, 3) gave {got!r}."
assert fr([1, 2, 3], 4, 1) == [], "A signal shorter than one frame has no frames."
m = dm([1.0, 1.0, 1.0, 1.0])
assert len(m) == 3 and abs(m[0] - 4) < 1e-9 and abs(m[1]) < 1e-9 and abs(m[2]) < 1e-9, f"A constant frame has all energy in bin 0: [4, 0, 0], got {m!r}."
N = 8
cos2 = [math.cos(2 * math.pi * 2 * n / N) for n in range(N)]
m = dm(cos2)
assert abs(m[2] - 4) < 1e-9 and all(abs(m[k]) < 1e-9 for k in [0, 1, 3, 4]), f"A cosine with 2 cycles in 8 samples peaks at bin 2 with magnitude 4, got {[round(v, 3) for v in m]!r}."
assert abs(hm(700) - 2595 * math.log10(2)) < 1e-9, "hz_to_mel(700) should be 2595·log10(2) ≈ 781.2."
assert hm(0) == 0, "0 Hz is 0 mel."
