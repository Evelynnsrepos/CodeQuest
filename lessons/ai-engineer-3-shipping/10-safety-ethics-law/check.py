rt, di, sr, ff = ns.get("risk_tier"), ns.get("disclose"), ns.get("selection_rates"), ns.get("four_fifths_ok")
assert rt and di and sr and ff, "Keep risk_tier, disclose, selection_rates and four_fifths_ok."
assert rt({"chatbot", "hiring"}) == "high" and rt({"chatbot"}) == "transparency" and rt({"spam_filter"}) == "minimal", "Check the tiers from strictest to mildest."
assert rt({"hiring", "social_scoring"}) == "prohibited", "Prohibited wins over everything."
assert di("Hi") == "[AI-generated] Hi" and di("[AI-generated] Hi") == "[AI-generated] Hi", "disclose: add the label once."
d = [("A", True)] * 50 + [("A", False)] * 50 + [("B", True)] * 30 + [("B", False)] * 70
assert sr(d) == {"A": 0.5, "B": 0.3}, f"selection_rates: {sr(d)!r}."
assert ff(d) is False, "0.3 < 0.8 × 0.5 = 0.4: fails the four-fifths rule."
d2 = [("A", True)] * 50 + [("A", False)] * 50 + [("B", True)] * 42 + [("B", False)] * 58
assert ff(d2) is True, "0.42 ≥ 0.4: passes."
