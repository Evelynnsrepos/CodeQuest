co, fc, sp = ns.get("conditional"), ns.get("from_counts"), ns.get("sequence_prob")
assert co and fc and sp, "Keep conditional, from_counts and sequence_prob."
assert abs(co(0.24, 0.3) - 0.8) < 1e-12, f"conditional(0.24, 0.3) should be 0.8, got {co(0.24, 0.3)!r}."
assert abs(co(0.24, 0.4) - 0.6) < 1e-12, "Divide by P(B), the 'given' part."
assert fc(24, 30) == 0.8 and fc(6, 70) == 6 / 70, "from_counts(24, 30) = 0.8."
assert abs(sp([0.05, 0.02, 0.3]) - 0.0003) < 1e-15, f"sequence_prob([0.05, 0.02, 0.3]) = 0.0003, got {sp([0.05, 0.02, 0.3])!r}."
assert sp([]) == 1, "Empty sequence: probability 1."
