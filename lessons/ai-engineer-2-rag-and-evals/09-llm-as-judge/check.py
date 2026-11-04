pv, pw, ka = ns.get("parse_verdict"), ns.get("pairwise"), ns.get("kappa")
assert pv and pw and ka, "Keep parse_verdict, pairwise and kappa."
assert pv('Sure! {"winner": "B", "reason": "x"}') == "B" and pv('{"winner":"tie"}') == "tie", "parse_verdict: read winner from the JSON."
assert pv("A is better") is None and pv('{"winner": "C"}') is None and pv("{broken json}") is None, "Anything else → None."
first_pos = lambda q, a, b: '{"winner": "A"}'
assert pw(first_pos, "q", "x", "y") == "tie", "A judge that always picks position A must give a tie after swapping."
prefers_long = lambda q, a, b: '{"winner": "%s"}' % ("A" if len(a) > len(b) else "B")
assert pw(prefers_long, "q", "long answer", "short") == "x" and pw(prefers_long, "q", "s", "longer") == "y", "Consistent wins count."
human = ["good", "bad", "good", "good", "bad", "good"]
judge = ["good", "bad", "good", "bad", "bad", "good"]
assert abs(ka(human, judge) - 2 / 3) < 1e-9, f"kappa: p_o = 5/6, p_e = 4/6·3/6 + 2/6·3/6 = 1/2, κ = 2/3. Got {ka(human, judge)!r}."
assert abs(ka(["y", "n"] * 5, ["y", "n"] * 5) - 1) < 1e-9, "Perfect agreement → 1."
assert abs(ka(["y", "y", "n", "n"], ["y", "n", "y", "n"])) < 1e-9, "Chance-level agreement → 0."
