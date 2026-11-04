f = ns.get("route")
assert f, "Define a function called route."
got = []
h = {"bill": lambda t: ("bill", t), "newsletter": lambda t: ("news", t), "other": lambda t: ("other", t)}
prompts = []
def spy(p):
    prompts.append(p)
    return " Newsletter.\n"
assert f("Weekly digest", spy, h) == ("news", "Weekly digest"), "Clean the reply and call the matching handler with the text."
assert len(prompts) == 1, "Ask the model once."
assert "bill, newsletter, other" in prompts[0] and "Weekly digest" in prompts[0], "The prompt needs the text and the labels."
assert f("x", lambda p: "BILL", h) == ("bill", "x"), "Make the reply lowercase."
assert f("x", lambda p: "an invoice maybe", h) == ("other", "x"), "Unknown replies go to the 'other' handler."
