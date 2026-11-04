import yaml


def check_workflow(text):
    data = yaml.safe_load(text) or {}
    trigger = data.get("on", data.get(True))
    if isinstance(trigger, str):
        trigger = [trigger]
    steps = [s for job in (data.get("jobs") or {}).values() for s in job.get("steps", [])]
    uses = [s.get("uses", "") for s in steps]
    runs = [s.get("run", "") for s in steps]
    problems = []
    if not trigger or "push" not in trigger or "pull_request" not in trigger:
        problems.append("trigger")
    if not any(u.startswith("actions/checkout") for u in uses):
        problems.append("checkout")
    if not any(u.startswith("actions/setup-python") for u in uses):
        problems.append("python")
    if not any("pytest" in r for r in runs):
        problems.append("tests")
    if "sk-" in text:
        problems.append("secret")
    return problems


WORKFLOW = """name: tests
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
print(check_workflow(WORKFLOW))
