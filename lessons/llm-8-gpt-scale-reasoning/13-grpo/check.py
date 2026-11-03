import math
vf, ga = ns.get("verify"), ns.get("group_advantages")
assert vf and ga, "Keep verify and group_advantages."
assert vf("work\nAnswer: 7", "7") == 1.0, "A correct final 'Answer:' line should give 1.0."
assert vf("Answer: 6\nwait, recheck\nAnswer: 7", "7") == 1.0, "Use the LAST 'Answer:' line."
assert vf("Answer: 7\nhmm\nAnswer: 6", "7") == 0.0, "The last 'Answer:' line is 6, so 0.0."
assert vf("the answer is 7", "7") == 0.0, "No 'Answer:' line means wrong format: 0.0."
assert vf("Answer:   7  ", "7") == 1.0, "Strip spaces around the answer."
got = ga([1.0, 0.0, 0.0, 1.0])
assert all(abs(a - b) < 1e-5 for a, b in zip(got, [1, -1, -1, 1])), f"[1, 0, 0, 1] has mean 0.5 and std 0.5, so advantages ±1, got {got!r}."
assert ga([1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0], "When every answer gets the same reward, all advantages are 0."
got = ga([1.0, 0.0, 0.0, 0.0])
want = [(1 - 0.25) / (math.sqrt(0.1875) + 1e-6)] + [(-0.25) / (math.sqrt(0.1875) + 1e-6)] * 3
assert all(abs(a - b) < 1e-9 for a, b in zip(got, want)), "Use the population std (divide by G) plus eps."
