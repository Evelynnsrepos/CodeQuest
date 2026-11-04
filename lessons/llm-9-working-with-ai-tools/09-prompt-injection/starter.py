def trifecta(tools):
    return False


def least_privilege(tools, needed):
    return tools


def safe_plan(tools, needed):
    return tools


TOOLS = [
    {"name": "read_email", "reads_untrusted": True, "private_data": True, "sends_out": False},
    {"name": "send_email", "reads_untrusted": False, "private_data": False, "sends_out": True},
    {"name": "calendar", "reads_untrusted": False, "private_data": True, "sends_out": False},
]
print(trifecta(TOOLS), [t["name"] for t in safe_plan(TOOLS, ["read_email", "send_email"])])
