sees_first_message = False
why_it_forgets = "b"
middle_fact = "b"
keep_instruction = "a"
dropped = 2
explanation = """
The model has no memory between messages: every time, the app sends the whole chat again as tokens.
It can only read a fixed number of tokens at once, called the context window, and the reply must fit too.
When the chat gets longer than that, the oldest messages are dropped, so the model never sees them anymore.
"""
