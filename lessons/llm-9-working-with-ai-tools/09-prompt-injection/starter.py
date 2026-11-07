def trifecta(tools):
    # untrusted = False
    # private = False
    # sends = False
    # for t in tools:
    #     if t["reads_untrusted"]:
    #         untrusted = True
    #     if t["private_data"]:
    #         private = True
    #     if t["sends_out"]:
    #         sends = True
    # return untrusted and private and sends
    return False


def least_privilege(tools, needed):
    # kept = []
    # for t in tools:
    #     if t["name"] in needed:
    #         kept.append(t)
    # return kept
    return tools


def safe_plan(tools, needed):
    # kept = least_privilege(tools, needed)
    # if trifecta(kept):
    #     safe = []
    #     for t in kept:
    #         if not t["sends_out"]:
    #             safe.append(t)
    #     return safe
    # return kept
    return tools


TOOLS = [
    {"name": "read_email", "reads_untrusted": True, "private_data": True, "sends_out": False},
    {"name": "send_email", "reads_untrusted": False, "private_data": False, "sends_out": True},
    {"name": "calendar", "reads_untrusted": False, "private_data": True, "sends_out": False},
]
print(trifecta(TOOLS), [t["name"] for t in safe_plan(TOOLS, ["read_email", "send_email"])])
