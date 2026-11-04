cw, WF = ns.get("check_workflow"), ns.get("WORKFLOW")
assert cw and WF, "Keep check_workflow and WORKFLOW."
good = """name: tests
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest -q
"""
assert cw(good) == [], f"The good workflow passes. Got {cw(good)!r}."
bad = """name: t
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      OPENAI_API_KEY: sk-abc123
    steps:
      - run: echo hi
"""
assert cw(bad) == ["trigger", "checkout", "python", "tests", "secret"], f"Got {cw(bad)!r}."
assert cw(good.replace("  pull_request:\n", "")) == ["trigger"], "Both push and pull_request are needed."
assert cw(good.replace("on:\n  push:\n  pull_request:", "on: [push, pull_request]")) == [], "The list form of on: works too."
assert cw(WF) == [], f"Your WORKFLOW should pass. Problems: {cw(WF)!r}."
