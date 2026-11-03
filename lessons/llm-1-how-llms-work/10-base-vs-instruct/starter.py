def to_chatml(messages):
    text = ""
    for message in messages:
        pass  # add one block per message
    return text  # don't forget the open assistant turn


chat = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]
print(to_chatml(chat))
