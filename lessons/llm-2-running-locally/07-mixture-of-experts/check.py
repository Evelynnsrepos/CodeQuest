sz, sp = ns.get("size_gb"), ns.get("speed_from_ram")
assert sz and sp, "Keep the functions size_gb and speed_from_ram."
got = sz(30, 8)
assert abs(got - 30) < 1e-9, f"size_gb(30, 8) returned {got!r}, expected 30."
got = sp(4, 4, 50)
assert abs(got - 25) < 1e-9, f"speed_from_ram(4, 4, 50) returned {got!r}, expected 50 / (4 × 4 / 8) = 25."
assert ns.get("faster") == "moe", "Compare the two 'from RAM' lines you printed. Set faster to \"dense\" or \"moe\"."
