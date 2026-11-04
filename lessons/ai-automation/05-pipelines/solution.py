def run_pipeline(value, steps):
    for step in steps:
        value = step(value)
        if value is None:
            raise RuntimeError(f"step {step.__name__} gave nothing")
    return value


def extract_total(text):
    for word in text.split():
        if word.startswith("$"):
            return float(word[1:])
    return None


def to_euros(dollars):
    return round(dollars * 0.9, 2)


def write_email(euros):
    return f"Please pay {euros} EUR."


print(run_pipeline("Invoice total: $120 due Friday", [extract_total, to_euros, write_email]))
