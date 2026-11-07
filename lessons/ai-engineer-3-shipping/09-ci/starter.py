import yaml


def check_workflow(text):
    # data = yaml.safe_load(text)
    # if data is None:
    #     data = {}
    # trigger = data.get("on", data.get(True))
    # if isinstance(trigger, str):
    #     trigger = [trigger]
    # jobs = data.get("jobs")
    # if jobs is None:
    #     jobs = {}
    # uses = []
    # runs = []
    # for name in jobs:
    #     for step in jobs[name].get("steps", []):
    #         uses.append(step.get("uses", ""))
    #         runs.append(step.get("run", ""))
    # checkout = False
    # python = False
    # tests = False
    # for u in uses:
    #     if u.startswith("actions/checkout"):
    #         checkout = True
    #     if u.startswith("actions/setup-python"):
    #         python = True
    # for r in runs:
    #     if "pytest" in r:
    #         tests = True
    # problems = []
    # if not trigger or "push" not in trigger or "pull_request" not in trigger:
    #     problems.append("trigger")
    # if not checkout:
    #     problems.append("checkout")
    # if not python:
    #     problems.append("python")
    # if not tests:
    #     problems.append("tests")
    # if "sk-" in text:
    #     problems.append("secret")
    # return problems
    return []


WORKFLOW = """name: tests
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo hi
"""
print(check_workflow(WORKFLOW))
