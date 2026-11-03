f = ns.get("rolling_window")
assert f, "Keep the function rolling_window."
chat = [("system", 100), ("user", 50), ("assistant", 50), ("user", 50)]
got = f(chat, 1000)
assert got == chat, f"Everything fits in 1000 tokens, so nothing should be dropped. Got {got!r}."
got = f(chat, 200)
assert got == [("system", 100), ("assistant", 50), ("user", 50)], f"rolling_window(chat, 200) returned {got!r}. Drop the oldest non-system message first and keep the order."
got = f(chat, 120)
assert got == [("system", 100)], f"rolling_window(chat, 120) returned {got!r}, expected only the system prompt."
assert chat == [("system", 100), ("user", 50), ("assistant", 50), ("user", 50)], "Don't change the list that was passed in."
