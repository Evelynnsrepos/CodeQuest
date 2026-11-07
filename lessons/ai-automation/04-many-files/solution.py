def run_batch(files, handle):
    results = {}
    errors = {}
    for name, text in files.items():
        if text.strip() == "":
            continue
        try:
            results[name] = handle(text)
        except Exception as e:
            errors[name] = str(e)
    return results, errors


def shout(text):
    if "broken" in text:
        raise ValueError("can't read this file")
    return text.upper()


print(run_batch({"a.md": "hello", "b.md": "broken!", "c.md": "   "}, shout))
