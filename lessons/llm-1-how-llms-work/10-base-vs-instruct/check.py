f = ns.get("to_chatml")
assert f, "Keep the function to_chatml."
got = f([{"role": "user", "content": "Hi"}])
want = "<|im_start|>user\nHi<|im_end|>\n<|im_start|>assistant\n"
assert got == want, f"to_chatml([{{'role': 'user', 'content': 'Hi'}}]) returned {got!r}, expected {want!r}."
got = f([{"role": "system", "content": "Be brief."}, {"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello!"}, {"role": "user", "content": "Bye"}])
want = ("<|im_start|>system\nBe brief.<|im_end|>\n<|im_start|>user\nHi<|im_end|>\n"
        "<|im_start|>assistant\nHello!<|im_end|>\n<|im_start|>user\nBye<|im_end|>\n<|im_start|>assistant\n")
assert got == want, f"A four-message chat came out as {got!r}, expected {want!r}."
assert f([]) == "<|im_start|>assistant\n", "With no messages, to_chatml should return just the open assistant turn."
