def to_chatml(messages):
    text = ""
    for message in messages:
        # text = text + "<|im_start|>" + message["role"] + "\n" + message["content"] + "<|im_end|>\n"
        pass
    return text  # change to: return text + "<|im_start|>assistant\n"


chat = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]
print(to_chatml(chat))
