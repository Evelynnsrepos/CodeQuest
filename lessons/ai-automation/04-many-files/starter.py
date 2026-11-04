def run_batch(files, handle):
    results = {}
    for name, text in files.items():
        results[name] = handle(text)
    return results


def shout(text):
    if "broken" in text:
        raise ValueError("can't read this file")
    return text.upper()


print(run_batch({"a.md": "hello", "b.md": "broken!", "c.md": "   "}, shout))
