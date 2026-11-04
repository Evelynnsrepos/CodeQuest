import math
cb, tp, nl, S = ns.get("count_bigrams"), ns.get("to_probs"), ns.get("nll"), ns["STOI"]
assert cb and tp and nl, "Keep count_bigrams, to_probs and nll."
N = cb(["ab", "a"])
assert N[0][S["a"]] == 2, f"'.' → 'a' happens twice in ['ab', 'a'], got {N[0][S['a']]}. Wrap each name as '.' + name + '.'."
assert N[S["a"]][S["b"]] == 1 and N[S["b"]][0] == 1 and N[S["a"]][0] == 1, "Count a→b, b→. and a→. once each."
assert sum(map(sum, N)) == 5, f"['ab', 'a'] has 5 pairs in total, your table counts {sum(map(sum, N))}."
P = tp(N)
assert len(P) == 27 and all(abs(sum(r) - 1) < 1e-9 for r in P), "Every row of to_probs should add up to 1."
assert abs(P[0][S["a"]] - 3 / 29) < 1e-9, f"With add-one smoothing, P['.']['a'] = (2 + 1) / (2 + 27) = 3/29, got {P[0][S['a']]}."
u = [[1 / 27] * 27 for _ in range(27)]
assert abs(nl(u, ["ab", "a"]) - math.log(27)) < 1e-9, "Under a uniform model, the average NLL should be log 27."
assert abs(nl(P, ["ab"]) - (-(math.log(P[0][S['a']]) + math.log(P[S['a']][S['b']]) + math.log(P[S['b']][0])) / 3)) < 1e-9, "nll should average −log P over every pair, including the start and end pairs."
