import math
cs, ag, ms = ns.get("cosine"), ns.get("angle_degrees"), ns.get("most_similar")
assert cs and ag and ms, "Keep cosine, angle_degrees and most_similar."
assert abs(cs([1, 0], [1, 1]) - 1 / math.sqrt(2)) < 1e-12, f"cosine([1,0], [1,1]) ≈ 0.707, got {cs([1, 0], [1, 1])!r}."
assert abs(cs([2, 0], [5, 0]) - 1) < 1e-12, "Same direction, different lengths: cosine 1."
assert abs(cs([1, 0], [-3, 0]) + 1) < 1e-12, "Opposite: −1."
assert abs(ag([1, 0], [0, 2]) - 90) < 1e-9 and abs(ag([1, 0], [1, 1]) - 45) < 1e-9, "angle_degrees([1,0], [1,1]) should be 45."
assert abs(ag([1, 1, 1], [2, 2, 2])) < 1e-6, "Parallel vectors: 0 degrees (clamp before acos)."
assert ms([1, 0], {"a": [0, 1], "b": [10, 1], "c": [1, 1]}) == "b", "Use cosine (direction), not the dot product."
