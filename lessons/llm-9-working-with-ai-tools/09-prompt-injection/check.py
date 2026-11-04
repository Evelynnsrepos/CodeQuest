tf, lp, sp = ns.get("trifecta"), ns.get("least_privilege"), ns.get("safe_plan")
assert tf and lp and sp, "Keep trifecta, least_privilege and safe_plan."
T = lambda n, u, p, s: {"name": n, "reads_untrusted": u, "private_data": p, "sends_out": s}
tools = [T("read_email", True, True, False), T("send_email", False, False, True), T("calendar", False, True, False), T("web_fetch", True, False, True)]
assert tf(tools) is True, "Across tools, all three legs are present."
assert tf([T("summarise", True, False, False)]) is False, "Only one leg: safe."
assert tf([T("a", True, False, False), T("b", False, True, False)]) is False, "No outbound leg: safe."
assert [t["name"] for t in lp(tools, ["calendar", "read_email"])] == ["read_email", "calendar"], "Keep the original order."
assert [t["name"] for t in sp(tools, ["read_email", "send_email"])] == ["read_email"], "Trifecta → drop the outbound tools."
assert [t["name"] for t in sp(tools, ["calendar", "send_email"])] == ["send_email", "calendar"], "No trifecta → keep what's needed."
