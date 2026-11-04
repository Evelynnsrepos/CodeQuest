---
title: CI: tests on every push
xp: 55
---
# A robot that runs your tests

> **Warm-up:** you fixed a bug at midnight and pushed. Did you run all the tests first?

**Continuous integration (CI)** runs your tests automatically on every push and pull request, on a clean machine. On GitHub it's **GitHub Actions**: a YAML file in `.github/workflows/`. The pull request then shows a green ✓ or a red ✗, and you never merge a red one.

```yaml
name: tests
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4            # get the code
      - uses: actions/setup-python@v5        # install Python
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest -q                       # app tests (with fakes, lesson 03) and retrieval evals
```

**YAML** is indentation-based, like Python: two spaces per level, `key: value`, and `- ` for list items.

What to run in CI for an AI app: unit tests with fakes (fast, free, every push), the retrieval eval suite (fast, deterministic), and the LLM-judged evals only on a schedule or by hand (they cost money and need an API key stored as a **repository secret**, used as `${{ secrets.OPENAI_API_KEY }}`, never written in the file).

## Your quest

1. `check_workflow(text)`: parse with `yaml.safe_load` and return a list of problems, in this order: `"trigger"` (not triggered on both `push` and `pull_request`), `"checkout"` (no step uses `actions/checkout`), `"python"` (no step uses `actions/setup-python`), `"tests"` (no `run` step contains `pytest`), `"secret"` (the raw text contains `sk-`, a key pasted into the file). Note: YAML reads the key `on` as the boolean `True`, so look up `data.get("on", data.get(True))`.
2. Write `WORKFLOW` that passes.

**Remember:** green before merge; secrets in repository settings, never in the file.

## Review

<details><summary>Why copy requirements.txt before the rest of the code in a Dockerfile?</summary>So the dependency layer stays cached when only your code changes.</details>
