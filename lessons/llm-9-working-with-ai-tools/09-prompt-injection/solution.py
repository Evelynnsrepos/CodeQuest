def trifecta(tools):
    return all(any(t[k] for t in tools) for k in ("reads_untrusted", "private_data", "sends_out"))


def least_privilege(tools, needed):
    return [t for t in tools if t["name"] in needed]


def safe_plan(tools, needed):
    kept = least_privilege(tools, needed)
    if trifecta(kept):
        return [t for t in kept if not t["sends_out"]]
    return kept


TOOLS = [
    {"name": "read_email", "reads_untrusted": True, "private_data": True, "sends_out": False},
    {"name": "send_email", "reads_untrusted": False, "private_data": False, "sends_out": True},
    {"name": "calendar", "reads_untrusted": False, "private_data": True, "sends_out": False},
]
print(trifecta(TOOLS), [t["name"] for t in safe_plan(TOOLS, ["read_email", "send_email"])])
